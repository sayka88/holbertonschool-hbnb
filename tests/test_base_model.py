#!/usr/bin/python3
"""Importing required libraries for unittesting of our base model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Base Model Test class"""
    def test_id(self):
        model = BaseModel()
        self.asserIsInstance(model.id, str)

    def test_created_at(self):
        model = BaseModel()
        self.assertEqual(model.created_at, datetime)

    def test_updated_at(self):
        model = BaseModel()
        self.assertEqual(model.updated_at, model.created_at)

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.update_at, old_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.tp_dict()
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
