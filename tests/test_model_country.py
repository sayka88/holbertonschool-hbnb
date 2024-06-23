#!/usr/bin/python3

import unittest
from datetime import datetime
from model.country import Country # Make sure you import the Country class correctly

class TestCountry(unittest.TestCase):

 def setUp(self):
 # Create an instance of Country for use in testing
 self.country = Country("France")

 def test_creation_country(self):
 # Check that the country was created with the correct name
 self.assertEqual(self.country.name, "France")

 # Check that the country has a non-empty identifier
 self.assertTrue(self.country.country_id)

 # Verify that the creation and update timestamps are set and that they are close in time
 self.assertIsInstance(self.country.created_at, datetime)
 self.assertIsInstance(self.country.updated_at, datetime)
 self.assertAlmostEqual((self.country.updated_at - self.country.created_at).total_seconds(), 0, delta=1)

 def test_to_dict(self):
 # Check that the to_dict method returns a dictionary containing the correct keys
 country_dict = self.country.to_dict()
 self.assertIsInstance(country_dict, dict)
 self.assertIn('country_id', country_dict)
 self.assertIn('name', country_dict)
 self.assertIn('created_at', country_dict)
 self.assertIn('updated_at', country_dict)

 # Check that the dictionary values ​​correspond to the country attributes
 self.assertEqual(country_dict['name'], self.country.name)
 self.assertEqual(country_dict['country_id'], self.country.country_id)
 self.assertEqual(country_dict['created_at'], self.country.created_at.isoformat())
 self.assertEqual(country_dict['updated_at'], self.country.updated_at.isoformat())

if __name__ == '__main__':
 unittest.main()
