"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""

import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
    
    def test_1(self):
        set_files = set(["this.txt", "that.txt", "the_other.txt"])
        
        "Verify creation of files is possible"
        for filename in set_files:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
            set_dir = set(os.listdir(self.dirname))
        self.assertEqual(set_files, set_dir, "The files are not the equal {0}, {1}".format(set_files,set_dir))
            
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
    
    def test_3(self):
        "Verify bytes in a file"
        path_file = "million.txt"
        f = open(path_file, "wb")
        million_bytes = b'X'*1000000
        f.write(million_bytes)
        f.close()
        self.assertTrue(f.closed)
        self.assertEqual(os.stat(path_file).st_size,len(million_bytes),
                         "The size of the file is not the expected, "
                         + "expected result: {0}, actual: {1}".format(len(million_bytes),os.stat(path_file).st_size))
        
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
if __name__ == "__main__":
    unittest.main()
        