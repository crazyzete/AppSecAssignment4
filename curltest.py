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



if __name__ == '__main__':
    unittest.main()
