#!/usr/bin/python3

import unittest
from model.place import Place # Make sure you import the Place class correctly

class TestPlace(unittest.TestCase):

 def setUp(self):
 # Create an instance of Place for use in testing
 self.place = Place(
 name="Cozy Apartment",
 description="A comfortable apartment in the city center.",
 address="123 Main St",
 city_id="123456",
 latitude=40.7128,
 longitude=-74.0060,
 host_id="host123",
 number_of_rooms=2,
 number_of_bathrooms=1,
 price_per_night=100,
 max_guests=4,
 amenity_ids=["wifi", "kitchen"]
 )

 def test_creation_place(self):
 # Verify that the place was created with the correct attributes
 self.assertEqual(self.place.name, "Cozy Apartment")
 self.assertEqual(self.place.description, "A comfortable apartment in the city center.")
 self.assertEqual(self.place.address, "123 Main St")
 self.assertEqual(self.place.city_id, "123456")
 self.assertEqual(self.place.latitude, 40.7128)
 self.assertEqual(self.place.longitude, -74.0060)
 self.assertEqual(self.place.host_id, "host123")
 self.assertEqual(self.place.number_of_rooms, 2)
 self.assertEqual(self.place.number_of_bathrooms, 1)
 self.assertEqual(self.place.price_per_night, 100)
 self.assertEqual(self.place.max_guests, 4)
 self.assertEqual(self.place.amenity_ids, ["wifi", "kitchen"])
 self.assertEqual(self.place.reviews, [])

 def test_add_review(self):
 # Add a review and check that it is correctly added to the reviews list
 review = “Great place to stay!”
 self.place.add_review(review)
 self.assertIn(review, self.place.reviews)

 def test_calculate_total_price(self):
 # Check that the calculation of the total price is correct for a given number of nights
 total_price = self.place.calculate_total_price(3)
 self.assertEqual(total_price, 300)

 def test_list_amenities(self):
 # Check that the list of amenities is correctly returned
 amenities = self.place.list_amenities()
 self.assertEqual(amenities, ["wifi", "kitchen"])

 # You can add other tests for other methods of the Place class here...

if __name__ == '__main__':
 unittest.main()
