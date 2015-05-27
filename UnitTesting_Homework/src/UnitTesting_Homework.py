import unittest

def title(s):
    "How close is this function to str.title()?"
    new_title = ""
    for word in s.split():
        new_title += word[0].upper()+word[1:].lower()+" "
    return new_title.strip()

class test_title(unittest.TestCase):
    
    def testing_upper_and_lower(self):
        for string_title in ["the LorD of the rings", "Pirates of the Caribbean 3", "aVenGers 2"]:
            self.assertEqual(title(string_title), string_title.title(), "The created function is not supporting the functionality of the string.title() function")
    
    def bad_input(self):
        self.assertRaises(TypeError,title,9)
        
if __name__ == "__main__":
    unittest.main()