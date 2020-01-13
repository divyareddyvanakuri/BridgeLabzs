import unittest
import sys
sys.path.insert(0,'\home\user\Desktop\programming\junit testing programs')
import tobinary
class Binaryconversion(unittest.TestCase):
    def test_Tobinary(self):
        result = tobinary.Tobinary(106)
        self.assertEqual(result,'1101010')
if __name__=="__main__":
    unittest.main()