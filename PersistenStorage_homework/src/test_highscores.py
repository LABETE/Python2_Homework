import unittest
import HighScores
import tempfile
import shutil
import glob
import os

class TestHighScores(unittest.TestCase):
    
    def setUp(self):
        self.oripath = os.getcwd()
        self.newpath = tempfile.mkdtemp("high_scores")
        os.chdir(self.newpath)
        
    def testNewScore(self):
        observed = HighScores.highscore('Roger', -50)
        expected = -50
        self.assertEqual(observed, expected, 'Results are not the expected, expected: {0}, actual: {1}'.format(expected,observed))
        
    def testNewHighScore(self):
        HighScores.highscore('Dilbert', 200)
        observed = HighScores.highscore('Dilbert', 789)
        expected = 789
        self.assertEqual(observed, expected, 'Results are not the expected, expected: {0}, actual: {1}'.format(expected,observed))
    
    def testLowScore(self):
        HighScores.highscore('Francis', 789)
        observed = HighScores.highscore('Francis', 500)
        expected = 789
        self.assertEqual(observed, expected, 'Results are not the expected, expected: {0}, actual: {1}'.format(expected,observed))
        
    def testEqualScore(self):
        HighScores.highscore('Frank', 789)
        observed = HighScores.highscore('Frank', 789)
        expected = 789
        self.assertEqual(observed, expected, 'Results are not the expected, expected: {0}, actual: {1}'.format(expected,observed))            
    
    def tearDown(self):
        for file in glob.glob("*"):
            file.remove()
        os.chdir(self.oripath)
        shutil.rmtree(self.newpath)
        
if __name__ == "__main__":
    unittest.main()