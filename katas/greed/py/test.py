import unittest

# Import the function(s) to test, e.g.:
from greed import Greed

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

    def test_case_scores(self):
        """
        Test Case scores
        """
        play = Greed()
        test_cases = [
            ([1], 100),
            ([1, 0], 100),
            ([5, 0], 50),
            ([5, 1], 150),
            ([4, 1, 3, 5, 6], 150),
            ([1, 1, 3, 4, 6], 0),
            ([1, 1, 1, 4, 6], 1000),
            ([1, 1, 2, 2, 2], 200),
            ([1, 3, 3, 3, 6], 400),
            ([1, 3, 5, 5, 5], 600),
            ([1, 6, 6, 5, 6], 750),
        ]
        for test in test_cases:
            result = play.score(test[0])
            self.assertEqual(result, test[1])


if __name__ == "__main__":
    unittest.main()

# Run the test with any of these options:
# - python test.py
# - python -m unittest test
# - python -m unittest -v test
# - python -m unittest discover