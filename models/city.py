#!/usr/bin/python3
"""Importing BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
        self.country_id = kwargs.get('country_id', '')
