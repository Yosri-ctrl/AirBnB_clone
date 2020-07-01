import unittest
"""
Test For BaseModel
"""
from models.base_model import BaseModel
import uuid
import datetime


class TestStringMethods(unittest.TestCase):
    """
    Test BaseModel class
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

    def test_str(self):
        test = BaseModel()
        r = test.__str__()
        f = "[{}] ({}) {}".format(type(test).__name__, test.id, test.__dict__)
        self.assertEqual(r, f)

    def test_update_time(self):
        test = BaseModel()
        r = test.created_at
        f = test.updated_at
        self.assertNotEqual(r, f)

    def test_kwargs(self):
        test = BaseModel()
        test.name = "hi"
        test.number = 99
        id = str(uuid.uuid4())
        test_dict = test.to_dict()

        f = {'id': test.id,
        'created_at': test.created_at,
        'updated_at': test.updated_at,
        'name': test.name,
        'number': test.number,
        '__class__': type(test).__name__}

        self.assertNotEqual(test.id, id)
        self.assertEqual(test.name, "hi")
        self.assertEqual(test.number, 99)
        self.assertEqual(test_dict, f)


if __name__ == '__main__':
    unittest.main()
