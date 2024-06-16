#!/usr/bin/python3
"""Importing libraries and packages"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity Test"""
    def test_amenity_creation(self):
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")


if __name__ == '__main__':
    unittest.main()
