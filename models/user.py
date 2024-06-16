#!/usr/bin/python3

"""Import BaseModel class"""
from models.base_model.py import BaseModel


class User(BaseModel):
    """Creating User Classs"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
