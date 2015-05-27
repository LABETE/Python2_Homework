import unittest
import mysql.connector
from database import login_info
from classFactory import build_row

class DBTest(unittest.TestCase):
    
    def setUp(self):
        C = build_row("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])   
        self.condition = 'id=1'
        self.lstexpected = ["user_record(1, 'Frank', 'frank@gmail.com')", "user_record(2, 'Michael', 'michael@gmail.com')"]
        self.lstexpected2 = ["user_record(1, 'Frank', 'frank@gmail.com')"]
        self.lstactual = []
        
    def test_atributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
    
    def test_repr(self):
        self.assertEqual(repr(self.c), "user_record(1, 'Steve Holden', 'steve@holdenweb.com')")
    
    def test_retrieve(self):
        db = mysql.connector.Connect(**login_info)
        self.cursor = db.cursor()
        result = self.c.retrieve(self.cursor) 
        for x in result:
            self.lstactual.append(str(x))
        self.assertEqual(self.lstexpected, self.lstactual)
            
    def test_retrieve_condition(self):
        db = mysql.connector.Connect(**login_info)
        self.cursor = db.cursor()
        result = self.c.retrieve(self.cursor, self.condition) 
        for x in result:
            self.lstactual.append(str(x))
        self.assertEqual(self.lstexpected2, self.lstactual)
            
if __name__ == "__main__":
    unittest.main()