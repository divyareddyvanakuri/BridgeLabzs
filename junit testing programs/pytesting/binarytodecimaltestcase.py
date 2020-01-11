import unittest
import binarytodecimal
class Decimal(unittest.TestCase):
    def test_decimalconversion(self):
        result = binarytodecimal.decimalconversion(60)
        self.assertEqual(result,195)
if __name__ == "__main__":
    unittest.main()