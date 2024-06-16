#!/usr/bin/python3
"""Importing BaseModel class"""
from models.base_model import BaseModel


class Country(BaseModel):
    """Country Class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
