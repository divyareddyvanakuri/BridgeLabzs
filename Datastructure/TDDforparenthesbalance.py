import unittest
import simplebalanceprogram 
class Check(unittest.TestCase):
    def test_whenGivenUnbalancedExpression_Then_ShouldReturnUnbalancedResult(self):
        result = simplebalanceprogram.is_expression_balanced(60)
        self.assertFalse(result)
        result = simplebalanceprogram.is_expression_balanced('{]')
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()