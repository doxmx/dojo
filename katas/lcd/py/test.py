import unittest

# Import the function(s) to test, e.g.:
from kata import number_to_matrix, DIGITS

# Implement tests here
class TestTemplate(unittest.TestCase):
    # Define as many tests cases as needed
    def test_case(self):
        """
        Test Case 1
        """
        data = [True]
        result = data[0]
        self.assertEqual(result, data[0])

    def test_case_single_digit(self):
        """
        Test Case 2 testing 1
        """
        data = {
            1: DIGITS[1],
            1: DIGITS[9],
        }
        for digit in data:
            result = number_to_matrix(digit)
            self.assertEqual(result, data[digit])


if __name__ == "__main__":
    unittest.main()

# Run the test with any of these options:
# - python test.py
# - python -m unittest test
# - python -m unittest -v test
# - python -m unittest discover