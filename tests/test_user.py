#!/usr/bin/python3
"""Importing Libraries"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test User class"""
    def test_user_creation(self):
        user = User(
            email="test@example.com",
            password="pass",
            first_name="Test",
            last_name="User"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "pass")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")


if __name__ == '__main__':
    unittest.main()
