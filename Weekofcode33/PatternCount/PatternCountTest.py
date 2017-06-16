import unittest
import PatternCount

class PatternCountTest(unittest.TestCase):
    
    def test1(self):
        s = "100001abc101"
        self.assertEqual(PatternCount.patternCount(s), 2)
        
    def test2(self):
        s = "1001ab010abc01001"
        self.assertEqual(PatternCount.patternCount(s), 2)
        
    def test3(self):
        s = "1001010001"
        self.assertEqual(PatternCount.patternCount(s), 3)
    
    def test4(self):
        s = "12232190014310101"
        self.assertEqual(PatternCount.patternCount(s), 2)
        
    def test5(self):
        s = "12232190a014310af1011111901001210b1"
        self.assertEqual(PatternCount.patternCount(s), 2)
        
    def test6(self):
        s = "1001"
        self.assertEqual(PatternCount.patternCount(s), 0)
        
suite = unittest.TestLoader().loadTestsFromTestCase(PatternCountTest)
unittest.TextTestRunner(verbosity=2).run(suite)