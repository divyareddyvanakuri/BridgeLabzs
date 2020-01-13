import unittest
import sys
sys.path.append('/home/user/Desktop/programming/junit testing programs/')
import dayofweek
class Dayofweek(unittest.TestCase):
    def test_DayOfWeek(self):
        result = dayofweek.DayOfWeek(2020,1,11)
        self.assertEqual(result,5)
if __name__ == "__main__":
    unittest.main()