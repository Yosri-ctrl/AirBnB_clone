#!/usr/bin/python3
"""
Test For review
"""
import unittest
from models.review import Review


class TestReviewMethod(unittest.TestCase):
    """
    test review class
    """

    def test_Review(self):
        """
        test review
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.text, str)


if __name__ == '__main__':
    unittest.main()
