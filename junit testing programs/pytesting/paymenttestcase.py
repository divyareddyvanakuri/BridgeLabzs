import unittest
import sys
sys.path.append('/home/user/Desktop/programming/junit testing programs/')
import calmonthlypayment
class MonthlyPayment(unittest.TestCase):
    def test_payment(self):
        result = calmonthlypayment.payment(2,2,1)
        self.assertEqual(result,0)
if __name__=='__main__':
    unittest.main()