#!/usr/bin/python3
"""
Test For place
"""
import unittest
from models.place import Place


class TestPlaceMethod(unittest.TestCase):
    """
    test place class
    """

    def test_Place(self):
        """
        test place
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.name, str)


if __name__ == '__main__':
    unittest.main()
