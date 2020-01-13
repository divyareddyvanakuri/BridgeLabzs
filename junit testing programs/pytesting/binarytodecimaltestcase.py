import unittest
import sys
sys.path.append('/home/user/Desktop/programming/junit testing programs/')
import binarytodecimal
class Decimal(unittest.TestCase):
    def test_decimalconversion(self):
        result = binarytodecimal.decimalconversion(60)
        self.assertEqual(result,195)
if __name__ == "__main__":
    unittest.main()