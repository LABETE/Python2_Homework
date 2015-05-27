import unittest
import EmailFunction

class EmailTest(unittest.TestCase):
    
    def setUp(self):
        self.email_address = "eddie.valv@gmail.com"
        self.body = "Text for the email body"
        self.attachments = ['v:/workspace/Email_Homework/src/python-logo.png', 'v:/workspace/Email_Homework/src/Text.txt']
        
    def testEmailFunction(self):
        observed = EmailFunction.sendEmail(self.email_address, self.body, self.attachments)
        expected = ''
        self.assertEqual(observed, expected)
        
if __name__ == "__main__":
    unittest.main()
    
