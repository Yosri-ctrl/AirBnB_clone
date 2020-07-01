#!/usr/bin/python3
"""
Test For amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenityMethod(unittest.TestCase):
    """
    test amenity class
    """

    def test_amenity(self):
        """
        test amenity
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
