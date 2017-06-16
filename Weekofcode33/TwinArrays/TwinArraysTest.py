import unittest
import TwinArrays

class TwinArraysTest(unittest.TestCase):
    
    def test1(self):
        ar1 = [3,1,4,2]
        ar2 = [6,7,8,9]
        self.assertEqual(TwinArrays.twinArrays(ar1, ar2), 7)
        
    def test2(self):
        ar1 = [2,1]
        ar2 = [5,6,3,7]
        self.assertEqual(TwinArrays.twinArrays(ar1, ar2), 4)
        
    def test3(self):
        ar1 = [1,5,6]
        ar2 = [1,5,6]
        self.assertEqual(TwinArrays.twinArrays(ar1, ar2), 6)
        
    def test4(self):
        ar1 = [5,4,1,7,9]
        ar2 = [8,9,1,5,2]
        self.assertEqual(TwinArrays.twinArrays(ar1, ar2), 3)
        
    def test5(self):
        ar1 = [5,4,1,7,9]
        ar2 = [8,9,1,1,2]
        self.assertEqual(TwinArrays.twinArrays(ar1, ar2), 2)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TwinArraysTest)
unittest.TextTestRunner(verbosity=2).run(suite)