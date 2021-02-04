import unittest

# Import the function(s) to test, e.g.:
# from kata import some_function

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

if __name__ == '__main__':
    unittest.main()

# Run the test with any of these options:
# - python test.py
# - python -m unittest test
# - python -m unittest -v test
# - python -m unittest discover