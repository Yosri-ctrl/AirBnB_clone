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
        user.first_name = "hello"
        self.assertIsInstance(user.first_name, str)
        self.assertEqual(user.first_name, "hello")

    def test_last_name(self):
        """
        last name
        """
        user = User()
        user.last_name = "world"
        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.last_name, "world")

    def test_email(self):
        """
        test email
        """
        user = User()
        user.email = "airbnb@helloworld.com"
        self.assertIsInstance(user.email, str)
        self.assertEqual(user.email, "airbnb@helloworld.com")

    def test_root(self):
        """
        test user
        """
        user = User()
        user.password = "root"
        self.assertIsInstance(user.password, str)
        self.assertEqual(user.password, "root")

if __name__ == '__main__':
    unittest.main()
