import time
import unittest
import subprocess
from bs4 import BeautifulSoup


class MyTestCase(unittest.TestCase):
     uname = "Matthew"
     pword = "test"
     twofa = "123456789"


    #Test Case Verifies Register Form returned by verifying
     def test_register_form(self):
        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', 'http://127.0.0.1:5000/register'], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        output = process.stdout

        soup = BeautifulSoup(output, features='html.parser')
        self.assertIsNotNone(soup.find(id='uname'))
        self.assertIsNotNone(soup.find(id='pword'))
        self.assertIsNotNone(soup.find(id='2fa'))
        self.assertEqual('User Registration', soup.title.string)

        # Test Case Verifies Register Failure
        def test_register_failure(self):
            process = subprocess.run(
                ['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', 'http://127.0.0.1:5000/register'], check=True,
                stdout=subprocess.PIPE,
                universal_newlines=True)
            output = process.stdout

            soup = BeautifulSoup(output, features='html.parser')
            self.assertEqual('User Registration', soup.title.string)

            csrfToken = soup.find(id='csrf_token')['value']
            postString = "uname=" + self.uname + "2&pword=" + self.pword + "&2fa=" + self.twofa + "&csrf_token=" + csrfToken

            process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', '-d', postString,
                                      'http://127.0.0.1:5000/register'],
                                     check=True, stdout=subprocess.PIPE,
                                     universal_newlines=True)

            process = subprocess.run(
                ['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', 'http://127.0.0.1:5000/register'], check=True,
                stdout=subprocess.PIPE,
                universal_newlines=True)
            output = process.stdout

            soup = BeautifulSoup(output, features='html.parser')
            self.assertEqual('User Registration', soup.title.string)

            csrfToken = soup.find(id='csrf_token')['value']
            postString = "uname=" + self.uname + "2&pword=" + self.pword + "&2fa=" + self.twofa + "&csrf_token=" + csrfToken

            process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', '-d', postString,
                                      'http://127.0.0.1:5000/register'],
                                     check=True, stdout=subprocess.PIPE,
                                     universal_newlines=True)

            output = process.stdout
            soup = BeautifulSoup(output, features='html.parser')
            success = soup.find(id='success')
            self.assertIsNotNone(success)
            self.assertEqual("failure", success.get_text().lower().strip())

     #Test Case Verifies Register Success
     def test_register_success(self):
        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', 'http://127.0.0.1:5000/register'], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        output = process.stdout

        soup = BeautifulSoup(output, features='html.parser')
        self.assertEqual('User Registration', soup.title.string)

        csrfToken = soup.find(id='csrf_token')['value']
        postString = "uname=" + self.uname + "&pword=" + self.pword + "&2fa=" + self.twofa + "&csrf_token=" + csrfToken

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', '-d', postString,
                                  'http://127.0.0.1:5000/register'],
                                 check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)

        output = process.stdout
        soup = BeautifulSoup(output, features='html.parser')
        success = soup.find(id='success')
        self.assertIsNotNone(success)
        self.assertEqual("success", success.get_text().lower().strip())

#Test Case Verifies Login Success
     def test_login_success(self):
        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', 'http://127.0.0.1:5000/register'], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        output = process.stdout

        soup = BeautifulSoup(output, features='html.parser')

        csrfToken = soup.find(id='csrf_token')['value']
        postString = "uname=" + self.uname + "3&pword=" + self.pword + "&2fa=" + self.twofa + "&csrf_token=" + csrfToken

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', '-d', postString,
                                  'http://127.0.0.1:5000/register'],
                                 check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', 'http://127.0.0.1:5000/login'],
                              check=True, stdout=subprocess.PIPE,
                              universal_newlines=True)

        output = process.stdout
        soup = BeautifulSoup(output, features='html.parser')
        csrfToken = soup.find(id='csrf_token')['value']
        self.assertEqual('User Login', soup.title.string)

        postString = "uname=" + self.uname + "3&pword=" + self.pword + "&2fa=" + self.twofa + "&csrf_token=" + csrfToken

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', '-d', postString,
                                  'http://127.0.0.1:5000/login'],
                                 check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)

        output = process.stdout
        soup = BeautifulSoup(output, features='html.parser')

        success = soup.find(id='result')
        self.assertEqual('Login Result Display', soup.title.string)
        self.assertIsNotNone(success)
        self.assertEqual("success", success.get_text().lower().strip())

     #Test Case Verifies Spell Check Success
     def test_login_spell_check_successs(self):
        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', 'http://127.0.0.1:5000/register'], check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        output = process.stdout

        soup = BeautifulSoup(output, features='html.parser')

        csrfToken = soup.find(id='csrf_token')['value']
        postString = "uname=" + self.uname + "4&pword=" + self.pword + "&2fa=" + self.twofa + "&csrf_token=" + csrfToken

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', '-d', postString,
                                  'http://127.0.0.1:5000/register'],
                                 check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', 'http://127.0.0.1:5000/login'],
                              check=True, stdout=subprocess.PIPE,
                              universal_newlines=True)

        output = process.stdout
        soup = BeautifulSoup(output, features='html.parser')
        csrfToken = soup.find(id='csrf_token')['value']
        self.assertEqual('User Login', soup.title.string)

        postString = "uname=" + self.uname + "4&pword=" + self.pword + "&2fa=" + self.twofa + "&csrf_token=" + csrfToken

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', '-d', postString,
                                  'http://127.0.0.1:5000/login'],
                                 check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)

        output = process.stdout
        soup = BeautifulSoup(output, features='html.parser')

        success = soup.find(id='result')
        self.assertEqual('Login Result Display', soup.title.string)
        self.assertIsNotNone(success)
        self.assertEqual("success", success.get_text().lower().strip())

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt',
                          'http://127.0.0.1:5000/spell_check'],
                         check=True, stdout=subprocess.PIPE,
                         universal_newlines=True)

        output = process.stdout
        soup = BeautifulSoup(output, features='html.parser')
        csrfToken = soup.find(id='csrf_token')['value']
        self.assertEqual('Spell Check', soup.title.string)

        postString = "inputtext=Take a sad sogn and make it betta&csrf_token=" + csrfToken

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt', '-d', postString,
                                  'http://127.0.0.1:5000/spell_check'],
                                 check=True, stdout=subprocess.PIPE,
                                 universal_newlines=True)
        output = process.stdout
        soup = BeautifulSoup(output, features='html.parser')
        self.assertEqual('Spell Check Results', soup.title.string)

        misspelled = soup.find(id='misspelled')
        self.assertIsNotNone(misspelled)
        self.assertEqual("sogn, betta", misspelled.get_text().strip())

        textout = soup.find(id='textout')
        self.assertIsNotNone(textout)
        self.assertEqual("Take a sad sogn and make it betta", textout.get_text().strip())

     #Test Case Verifies Spell Check Fail No Login
     def test_login_spell_check_fail_no_login(self):

        process = subprocess.run(['curl', '-b', 'cookies.txt', '-c', 'cookies.txt',
                          'http://127.0.0.1:5000/spell_check'],
                         check=True, stdout=subprocess.PIPE,
                         universal_newlines=True)

        output = process.stdout
        soup = BeautifulSoup(output, features='html.parser')
        self.assertEqual('Redirecting...', soup.title.string)

if __name__ == '__main__':
    unittest.main()
