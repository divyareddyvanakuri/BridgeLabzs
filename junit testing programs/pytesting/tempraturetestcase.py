import unittest
import sys
sys.path.append('/home/user/Desktop/programming/junit testing programs/')
import tempratureconversion
class tempraturetestcase(unittest.TestCase):
    def test_fcon(self):
        result = tempratureconversion.fcon(10)
        self.assertEqual(result,50)
    def test_ccon(self):
        result = tempratureconversion.ccon(50)
        self.assertEqual(result,10)
if __name__=='__main__':
    unittest.main()
