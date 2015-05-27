import unittest
import os
import shutil
import tempfile
import newarchive

class TestCreateDirectory(unittest.TestCase):
    
    def setUp(self):
        self.oripath = os.getcwd()
        self.newpath = tempfile.mkdtemp("archives")
        self.archive_file = os.path.join(self.newpath,"archive_me")
        self.zip_file = os.path.join(self.archive_file,"archive_me_zf.zip")
        os.mkdir(self.archive_file)
        os.chdir(self.archive_file)
        self.new_files = ["groucho", "harpo", "chico"]
        for file in self.new_files:
            f = open(file, "w")
            f.close()
        self.sub_file = "test"
        os.mkdir(self.sub_file)
        os.chdir(self.sub_file)
        f = open("groucho2", "w")
        f.close()
        os.chdir(self.archive_file)    
        
    def testarchivezip(self):        
        observed = newarchive.newarchivedirectory(self.zip_file)
        expected = ["archive_me\\groucho", "archive_me\\harpo", "archive_me\\chico"]
        expected.sort()
        self.assertEqual(expected, observed, "Data don't match, expected files: {0}, actual files: {1}".format(expected,observed))
        
    def tearDown(self):
        os.chdir(self.oripath)
        shutil.rmtree(self.newpath)

if __name__ == "__main__":
    unittest.main()