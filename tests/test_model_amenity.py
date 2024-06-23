#!/usr/bin/python3
import unittest
from model.amenity import Amenity # Make sure you import the Amenity class correctly
import uuid
from datetime import datetime

class TestAmenity(unittest.TestCase):

 def test_creation_amenity(self):
 # Create a valid instance of Amenity
 amenity_name = "Swimming Pool"
 amenity = Amenity(amenity_name)

 # Check if the instance was created with the correct attributes
 self.assertEqual(amenity.name, amenity_name)

 # Check if amenity ID is a valid UUID string
 self.assertTrue(uuid.UUID(amenity.amenity_id))

 # Check if creation and update timestamps are set
 self.assertIsInstance(amenity.created_at, datetime)
 self.assertIsInstance(amenity.updated_at, datetime)

 def test_to_dict(self):
 # Create an Amenity instance
 amenity = Amenity("Gym")

 # Call the to_dict method
 amenity_dict = amenity.to_dict()

 # Check if the to_dict method returns a dictionary with the correct keys and values
 self.assertIsInstance(amenity_dict, dict)
 self.assertIn('amenity_id', amenity_dict)
 self.assertIn('name', amenity_dict)
 self.assertIn('created_at', amenity_dict)
 self.assertIn('updated_at', amenity_dict)
 self.assertEqual(amenity_dict['name'], amenity.name)
 self.assertEqual(amenity_dict['amenity_id'], amenity.amenity_id)
 self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
 self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())

if __name__ == '__main__':
 unittest.main()
