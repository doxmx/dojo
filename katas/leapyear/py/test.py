import unittest

# Import the function(s) to test, e.g.:
from kata import is_leap_year

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

    def test_disivisible_by_400_is_leap(self):
        """
        All years divisible by 400 ARE leap years
        """
        years = [400, 800, 1200, 1600, 2000]
        for year in years:
            result = is_leap_year(year)
            self.assertEqual(result, True)

    def test_disivisible_by_100_and_not_by_400_is_not_leap(self):
        """
        All years divisible by 100 but not by 400 are NOT leap years
        """
        years = [300, 900, 1300, 1500, 1900]
        for year in years:
            result = is_leap_year(year)
            self.assertEqual(result, False)


    def test_divisible_by_4_and_not_by_100_is_leap(self):
        """
        All years divisible by 4 but not by 100 ARE leap years
        """
        years = [ 1996, 2004, 2008, 2012, 2016, 2020, 2024 ]
        for year in years:
            result = is_leap_year(year)
            self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

# Run the test with any of these options:
# - python test.py
# - python -m unittest test
# - python -m unittest -v test
# - python -m unittest discover