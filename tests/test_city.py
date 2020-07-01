#!/usr/bin/python3
"""
Test For city
"""
import unittest
from models.city import City


class TestCityMethod(unittest.TestCase):
    """
    test city class
    """

    def test_city(self):
        """
        test city
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.name, str)


if __name__ == '__main__':
    unittest.main()
