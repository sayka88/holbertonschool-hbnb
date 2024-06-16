#!/usr/bin/python3
"""Importing Libraries"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Place Test"""
    def test_place_creation(self):
        place = Place(
            name="Test Place", description="A nice place",
            address="123 Test St", city_id="1",
            latitude=12.34, longitude=56.78,
            host_id="2", number_of_rooms=3,
            number_of_bathrooms=2, price_per_night=100.0,
            max_guests=4
        )
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "A nice place")
        self.assertEqual(place.address, "123 Test St")
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.latitude, 12.34)
        self.assertEqual(place.longitude, 56.78)
        self.assertEqual(place.host_id, "2")
        self.assertEqual(place.number_of_rooms, 3)
        self.assertEqual(place.number_of_bathrooms, 2)
        self.assertEqual(place.price_per_night, 100.0)
        self.assertEqual(place.max_guests, 4)


if __name__ == '__main__':
    unittest.main()
