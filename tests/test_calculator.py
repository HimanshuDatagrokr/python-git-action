import unittest
from Calculator import add_Numbers

class TestCalculator(unittest.TestCase):

    def test_add_numbers(self):
        result = add_Numbers(2,3)
        self.assertEqual(result,5)


if __name__ == '__main__':
    unittest.main()