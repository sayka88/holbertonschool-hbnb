#!/usr/bin/python3
"""Importing BaseModel class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class named Place"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.address = kwargs.get('address', '')
        self.city_id = kwargs.get('city_id', '')
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.host_id = kwargs.get('host_id', '')
        self.number_of_rooms = kwargs.get('number_of_rooms', 0)
        self.number_of_bathrooms = kwargs.get('number_of_bathrooms', 0)
        self.price_per_night = kwargs.get('price_per_night', 0.0)
        self.max_guests = kwargs.get('max_guests', 0)
        self.amenities = kwargs.get('amenities', [])
