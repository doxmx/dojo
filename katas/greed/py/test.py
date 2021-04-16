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
            ([1, 1, 1, 1], 2000),
            ([1, 1, 1, 1, 2], 2000),
            ([2, 2, 2, 2], 400),
            ([3, 3, 3, 3], 600),
            ([4, 4, 4, 4], 800),
            ([5, 5, 5, 5], 1000),
            ([6, 6, 6, 6], 1200),
            ([1, 1, 1, 1, 1], 4000),
            ([2, 2, 2, 2, 2], 800),
            ([3, 3, 3, 3, 3], 1200),
            ([4, 4, 4, 4, 4], 1600),
            ([5, 5, 5, 5, 5], 2000),
            ([6, 6, 6, 6, 6], 2400),
            ([1, 1, 1, 1, 1, 1], 8000),
            ([2, 2, 2, 2, 2, 2], 1600),
            ([3, 3, 3, 3, 3, 3], 2400),
            ([4, 4, 4, 4, 4, 4], 3200),
            ([5, 5, 5, 5, 5, 5], 4000),
            ([6, 6, 6, 6, 6, 6], 4800),
            ([2, 3, 4, 2, 3, 4], 800),
            ([2, 2, 4, 4, 6, 6], 800),
            ([1, 1, 5, 5, 6, 6], 800),
            ([1, 2, 3, 4, 5, 6], 1200),
            ([6, 5, 3, 1, 2, 4], 1200),
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