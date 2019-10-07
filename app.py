from flask import Flask, request, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import secrets
import subprocess
import os

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(24)

csrf = CSRFProtect(app)

userDict = {}


class UserForm(FlaskForm):
    uname = StringField('User Name:', validators=[DataRequired()])
    pword = StringField('Password: ', validators=[DataRequired()])
    twofa = StringField('2FA Token:', validators=[], id='2fa')


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = UserForm()
    if form.validate_on_submit():
        #return redirect('/success')

        global userDict

        user = form.uname.data
        pword = form.pword.data
        twofa = form.twofa.data

        if (user in userDict) or (not user) or (not pword):
            return render_template('registrationResult.html', success="Failure")
        else:
            userDict[user] = {'pword' : pword, '2fa' : twofa}
            return render_template('registrationResult.html', success="Success")

    return render_template('registerForm.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = UserForm()
    if form.validate_on_submit():
        # return redirect('/success')

        global userDict

        user = form.uname.data
        pword = form.pword.data
        twofa = form.twofa.data

        if (user in userDict):

            userInfo = userDict[user]
            if (userInfo['pword'] == pword):
                if (userInfo['2fa'] == twofa):
                    return render_template('loginResult.html', result="Success")
                else:
                    return render_template('loginResult.html', result="Two-factor Failure")
            else:
                return render_template('loginResult.html', result="Incorrect")
        else:
            return render_template('loginResult.html', result="Incorrect")

    return render_template('userLoginForm.html', form=form)


class spellCheckForm(FlaskForm):
    inputtext = TextAreaField(u'Text to Check', [DataRequired()], render_kw={"rows": 40, "cols": 100})


@app.route('/spell_check', methods=('GET', 'POST'))
def spellcheck():

    form = spellCheckForm()

    if form.validate_on_submit():
        # return redirect('/success')

        text = form.inputtext.data

        # TODO: If can get a user info, append that to file
        f = open("tempUserInput", "w")
        f.write(text)
        f.close()

        process = subprocess.run(['./a.out', 'tempUserInput', 'wordlist.txt'], check=True, stdout=subprocess.PIPE,
             universal_newlines=True)
        output = process.stdout

        os.remove("tempUserInput")

        misspelledOut = output.replace("\n", ", ").strip().strip(',')

        return render_template('spellCheckResult.html', misspelled=misspelledOut, textout=text)

    else:
        return render_template('spellCheckForm.html', form=form)


# @app.route('/')
# def index():
#    f = open("tempUserInput", "w")
#    f.write("Matthew, the big brown dkcu si in the huouse.")
#    f.close()

#    process = subprocess.run(['./a.out', 'tempUserInput',
#                              'wordlist.txt'], check=True,
#                             stdout=subprocess.PIPE, universal_newlines=True)
#    output = process.stdout

#    os.remove("tempUserInput")

#    formatOutput = output.replace("\n", ", ").strip().strip(',')

#   return formatOutput


# @app.route('/add')
# def add():
#    global userCount
#    global userDict
#    global usrlock

#    usrlock.acquire()
#    userCount = userCount + 1
#    userDict[userCount] = str(userCount)

#    userStr = str(userCount) + ": "
#    for key in userDict:
#        userStr = userStr + userDict[key]

#    usrlock.release()
#   return userStr


if __name__ == '__main__':
    app.run(debug=True)
