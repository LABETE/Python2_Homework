import unittest
import os
import tempfile
import CountFiles
import shutil

class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.oripath = os.getcwd()
        self.path = tempfile.mkdtemp("Documents")
        os.chdir(self.path)
        self.files = ["test.txt","Document.doc","book.xlsx","otherdocument.doc"]
        for file in self.files:
            f = open(os.path.join(self.path, file), "w")
            f.close()     
    
    def test_counted_files(self):
        """Test if the dictionary bring the correct extensions and the number of extension in the path"""
        dict_expected = {"txt":1,"doc":2,"xlsx":1}
        dict_actual = CountFiles.CountFilesInDirectory()
        self.assertEqual(dict_expected,dict_actual,"The dictionaries are not equal expected: {0}, actual: {1}".format(dict_expected,dict_actual))
    
    def tearDown(self):
        os.chdir(self.oripath)
        shutil.rmtree(self.path)
        
if __name__ == "__main__":
    unittest.main()
    