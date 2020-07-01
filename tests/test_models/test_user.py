#!/usr/bin/python3
"""
Test For User
"""
from models import storage
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    test the user class
    """

    def test_user(self):
        """
        test user
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_first_name(self):
        """
        first name
        """
        user = User()
        self.assertIsInstance(user.first_name, str)

    def test_last_name(self):
        """
        last name
        """
        user = User()
        self.assertIsInstance(user.last_name, str)

    def test_email(self):
        """
        test email
        """
        user = User()
        self.assertIsInstance(user.email, str)

    def test_root(self):
        """
        test user
        """
        user = User()
        self.assertIsInstance(user.password, str)

if __name__ == '__main__':
    unittest.main()
