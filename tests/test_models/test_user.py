#!/usr/bin/python3
"""
Test For User
"""
from models import storage
from models.base_model import BaseModel
from models.user import User
import uuid
import datetime
from models import storage
import unittest


class TestUser(unittest.TestCase):
    """
    test the user class
    """
    def test_user(self):
        user = User()
        user.first_name = "hello"
        user.last_name = "world"
        user.email = "airbnb@helloworld.com"
        user.password = "root"
        user.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, "hello")
        self.assertEqual(user.last_name, "world")
        self.assertEqual(user.email, "airbnb@helloworld.com")
        self.assertEqual(user.password, "root")
        

if __name__ == '__main__':
    unittest.main()
