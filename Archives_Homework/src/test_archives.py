import unittest
import zipfile
import os
import shutil
import tempfile
import archivesziped

class testingfiles(unittest.TestCase):
    
    def setUp(self):
        self.oripath = os.getcwd()
        self.newpath = tempfile.mkdtemp("Archives")
        self.newpath = os.path.join(self.newpath,"archive_me")
        os.mkdir(self.newpath)
        self.basename_newpath = os.path.basename(self.newpath)
        #self.zip_file = os.path.join(self.newpath, self.basename_newpath+".zip")
        #self.zip_file = os.path.join(self.newpath, self.basename_newpath)
        os.chdir(self.newpath)
        files_to_zip = ["groucho", "harpo", "chico"]
        for file in files_to_zip:
            f = open(file, "w")
            f.close()
        os.chdir(self.oripath)
    
    def testzipfiles(self):
        observed = archivesziped.zippedfiles(self.newpath)
        expected = [os.path.join(self.basename_newpath,"groucho"), os.path.join(self.basename_newpath,"harpo"), os.path.join(self.basename_newpath,"chico")]
        self.assertEqual(set(observed), set(expected), "Data doesn't match: observed: {0}, expected: {1}".format(set(observed),set(expected))) 
    
    def test_mentor_test(self): 
        archivesziped.zippedfiles(self.newpath)       
        zf = zipfile.ZipFile(os.path.join(self.oripath, self.basename_newpath)+".zip", 'r')
        observed = zf.namelist()
        zf.close()
        expected = ["archive_me/groucho", "archive_me/harpo", "archive_me/chico"]
        self.assertEqual(set(expected), set(observed), "mentor test fails")

    
    def tearDown(self):
        os.chdir(self.oripath)
        shutil.rmtree(self.newpath)

if __name__ == "__main__":
    unittest.main()