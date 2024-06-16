#!/usr/bin/python3
"""Importing packs and libs"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Testcity class"""
    def test_city_creation(self):
        city = City(name="Nakhchivan", country_id="1")
        self.assertEqual(city.name, "Nakhchivan")
        self.assertEqual(city.country_id, "1")


if __name__ == '__main__':
    unittest.main()
