#!/usr/bin/python3
"""Importing Linraries"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review class"""
    def test_review_creation(self):
        review = Review(
            place_id="1", user_id="2",
            text="Great place!", rating=5
        )
        self.assertEqual(review.place_id, "1")
        self.assertEqual(review.user_id, "2")
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.rating, 5)


if __name__ == '__main__':
    unittest.main()
