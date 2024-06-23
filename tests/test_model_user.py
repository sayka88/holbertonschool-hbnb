#!/usr/bin/python3

import unittest
from model.user import User


class TestUser(unittest.TestCase):

 def setUp(self):
 # Create an instance of User for use in testing
 self.user = User(
 username="john_doe",
 email="john@example.com",
 password="password123"
 )

 def test_creation_user(self):
 # Verifies that the user was created with the correct attributes
 self.assertTrue(self.user.user_id)
 self.assertEqual(self.user.username, "john_doe")
 self.assertEqual(self.user.email, "john@example.com")
 self.assertEqual(self.user.password, "password123")

 # Verify that the creation and update timestamps
 # day are defined and they are close in time
 self.assertIsNotNone(self.user.created_at)
 self.assertIsNotNone(self.user.updated_at)
 self.assertAlmostEqual(
 (self.user.updated_at - self.user.created_at).total_seconds(),
 0, delta=1)

 def test_add_review(self):
 # Add a review and check that it is
 # correctly added to the reviews list
 review = {"review_id": "review123", "rating": 5,
 "comment": "Great experience!"}
 self.user.add_review(review)
 self.assertIn(review, self.user.reviews)

 def test_to_dict(self):
 # Check that the to_dict method returns
 # a dictionary containing the correct keys
 user_dict = self.user.to_dict()
 self.assertIsInstance(user_dict, dict)
 self.assertIn('user_id', user_dict)
 self.assertIn('username', user_dict)
 self.assertIn('email', user_dict)
 self.assertIn('created_at', user_dict)
 self.assertIn('updated_at', user_dict)
 self.assertIn('reviews', user_dict)

 # Check that dictionary values
 # match user attributes
 self.assertEqual(user_dict['username'], self.user.username)
 self.assertEqual(user_dict['email'], self.user.email)
 self.assertEqual(user_dict['user_id'], self.user.user_id)
 self.assertEqual(user_dict['created_at'],
 self.user.created_at.isoformat())
 self.assertEqual(user_dict['updated_at'],
 self.user.updated_at.isoformat())


if __name__ == '__main__':
 unittest.main()
