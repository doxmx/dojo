import unittest

# Import the function(s) to test, e.g.:
from kata import print_fizz_buzz


# Implement tests here
class TestTemplate(unittest.TestCase):
    # Define as many tests cases as needed
    def test_case(self):
        """
        Test Case 0
        """
        data = [True]
        result = data[0]
        self.assertEqual(result, data[0])

    def test_is_divisible_by_3_returns_fizz(self):
        """
        Given a number return fizz if it is divisible by 3
        """
        numbers = {6: "Fizz", 9: "Fizz", 12: "Fizz"}
        for number in numbers:
            value = print_fizz_buzz(number)
            self.assertEqual(value, numbers[number])

    def test_is_divisible_by_5_returns_fizz(self):
        """
        Given a number return fizz if it is divisible by 5
        """
        numbers = {5: "Buzz", 10: "Buzz", 80: "Buzz"}
        for number in numbers:
            value = print_fizz_buzz(number)
            self.assertEqual(value, numbers[number])

    def test_is_divisible_by_5_and_3_returns_fizzbuzz(self):
        """
        Given a number return fizzbuzz if it is divisible by 5 and 3
        """
        numbers = {15: "FizzBuzz", 30: "FizzBuzz", 90: "FizzBuzz"}
        for number in numbers:
            value = print_fizz_buzz(number)
            self.assertEqual(value, numbers[number])

    def test_is_not_divisible_by_5_and_3_returns_number(self):
        """
        Given a number return it if it is not divisible by either 5 and 3
        """
        numbers = {1: "1", 2: "2", 7: "7"}
        for number in numbers:
            value = print_fizz_buzz(number)
            self.assertEqual(value, numbers[number])


if __name__ == "__main__":
    unittest.main()

# Run the test with any of these options:
# - python test.py
# - python -m unittest test
# - python -m unittest -v test
# - python -m unittest discover
