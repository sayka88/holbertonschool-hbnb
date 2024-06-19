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
        self.data_manager = DataManager

    def tearDown(self):
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')

    def test_save_entity(self):
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
    @patch.object(DataManager, 'save_city')
    def test_save_city(self, mock_save_city):
        mock_save_city.return_value = 1
        city_data = {'name': 'Paris', 'country_id': 1}
        city_id = self.data_manager.save_city(city_data)
        self.assertEqual(city_id, 1)
        mock_save_city.assert_called_once_with(city_data)

    @patch.object(DataManager, 'get_city')
    def test_get_city(self, mock_get_city):
        mock_city = City(name='Paris', country_id=1)
        mock_get_city.return_value = mock_city
        result = self.data_manager.get_city(1)
        self.assertEqual(result.name, 'Paris')
        mock_get_city.assert_called_once_with(1)

    @patch.object(DataManager, 'get_all_cities')
    def test_get_all_cities(self, mock_get_all_cities):
        mock_cities = [City(name='Paris', country_id=1), City(name='London', country_id=2)]
        mock_get_all_cities.return_value = mock_cities
        result = self.data_manager.get_all_cities()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, 'Paris')
        self.assertEqual(result[1].name, 'London')
        mock_get_all_cities.assert_called_once()

    @patch.object(DataManager, 'update_city')
    def test_update_city(self, mock_update_city):
        mock_update_city.return_value = True
        updated_data = {'name': 'New Paris'}
        result = self.data_manager.update_city(1, updated_data)
        self.assertTrue(result)
        mock_update_city.assert_called_once_with(1, updated_data)

    @patch.object(DataManager, 'delete_city')
    def test_delete_city(self, mock_delete_city):
        mock_delete_city.return_value = True
        result = self.data_manager.delete_city(1)
        self.assertTrue(result)
        mock_delete_city.assert_called_once_with(1)
