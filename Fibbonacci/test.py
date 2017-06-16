import unittest
import fibbonacci

class FibTest(unittest.TestCase):
    
    def testFib(self):
        fib = fibbonacci
        self.assertEqual(fib.get(5), 5)
        self.assertEqual(fib.get(10), 55)

suite = unittest.TestLoader().loadTestsFromTestCase(FibTest)
unittest.TextTestRunner(verbosity=2).run(suite)