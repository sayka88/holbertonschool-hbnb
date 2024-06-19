#!/usr/bin/python3

import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.amenity import Amenity
from models.city import City
from models.country import Country
from models.place import Place
from models.review import Review
from models.user import User
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager(storage_file='test_data.json')

    def tearDown(self):
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')

    def test_save_entity(s    elf):
        entity = {'name': 'Test'}
        saved_entity = self.data_manager.save(entity)
        self.assertEqual(saved_entity['name'], 'Test')
        self.assertIn('id', saved_entity)

    def test_get_entity(self):
        entity = {'name': 'Test'}
        saved_entity = self.data_manager.save(entity)
        fetched_entity = self.data_manager.get(saved_entity['id'])
        self.assertEqual(fetched_entity, saved_entity)

    def test_update_entity(self):
        entity = {'name': 'Test'}
        saved_entity = self.data_manager.save(entity)
        self.data_manager.update(saved_entity['id'], {'name': 'Updated Test'})
        updated_entity = self.data_manager.get(saved_entity['id'])
        self.assertEqual(updated_entity['name'], 'Updated Test')

    def test_delete_entity(self):
        entity = {'name': 'Test'}
        saved_entity = self.data_manager.save(entity)
        self.data_manager.delete(saved_entity['id'])
        self.assertIsNone(self.data_manager.get(saved_entity['id']))

    def test_get_all_entities(self):
        entity1 = {'name': 'Test1'}
        entity2 = {'name': 'Test2'}
        self.data_manager.save(entity1)
        self.data_manager.save(entity2)
        all_entities = self.data_manager.get_all()
        self.assertEqual(len(all_entities), 2)

    # Tests for City
    def setUp(self):
        self.data_manager = DataManager(file_name='test_data.json')
        self.data_manager.data = {'countries': {}, 'cities': {}}
        self.data_manager._save()

    def tearDown(self):
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')

    def test_save_and_get_country(self):
        country = {'code': 'US', 'name': 'United States'}
        self.data_manager.save_country(country)
        self.assertEqual(self.data_manager.get_country('US'), country)

    def test_save_and_get_city(self):
        country = {'code': 'US', 'name': 'United States'}
        self.data_manager.save_country(country)
        city = {'name': 'New York', 'country_code': 'US'}
        saved_city = self.data_manager.save_city(city)
        self.assertIn('id', saved_city)
        self.assertEqual(self.data_manager.get_city(saved_city['id']), saved_city)

if __name__ == '__main__':
    unittest.main()
