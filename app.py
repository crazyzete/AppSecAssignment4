from flask import Flask, request
import subprocess
import os
import threading

app = Flask(__name__)

usrlock = threading.Lock()
userCount = 0
userDict = {}


@app.route('/')
def index():
    f = open("tempUserInput", "w")
    f.write("Matthew, the big brown dkcu si in the huouse.")
    f.close()

    process = subprocess.run(['./a.out', 'tempUserInput',
                              'wordlist.txt'], check=True,
                             stdout=subprocess.PIPE, universal_newlines=True)
    output = process.stdout

    os.remove("tempUserInput")

    formatOutput = output.replace("\n", ", ").strip().strip(',')

    return formatOutput


@app.route('/add')
def add():
    global userCount
    global userDict
    global usrlock

    usrlock.acquire()
    userCount = userCount + 1
    userDict[userCount] = str(userCount)

    userStr = str(userCount) + ": "
    for key in userDict:
        userStr = userStr + userDict[key]

    usrlock.release()
    return userStr


if __name__ == '__main__':
    app.run(debug=True)




