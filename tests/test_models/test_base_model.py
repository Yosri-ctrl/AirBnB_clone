import unittest
"""
Test For BaseModel
"""
from models.base_model import BaseModel
import uuid
import datetime


class TestStringMethods(unittest.TestCase):
    """
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """

    def test_creation_base_model(self):
        """
        creation of a base model
        """
        test = BaseModel()
        self.assertIsInstance(test, BaseModel)

    def test_id_base_model(self):
        """
        different id of a base model
        """
        test1 = BaseModel()
        test2 = BaseModel()
        self.id = str(uuid.uuid4())
        self.assertNotEqual(test1.id, self.id)
        self.assertNotEqual(test1.id, test2.id)

    def test_created_base_model(self):
        """
        date of creation of a base model
        """
        test1 = BaseModel()
        test2 = BaseModel()
        self.assertNotEqual(test1.created_at, test2.created_at)
        self.assertIsInstance(test1.created_at, datetime.datetime)

    def test_updeted_base_model(self):
        """
        date of update of a base model
        """
        test1 = BaseModel()
        test2 = BaseModel()
        self.assertNotEqual(test1.updated_at, test2.updated_at)
        self.assertIsInstance(test1.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
