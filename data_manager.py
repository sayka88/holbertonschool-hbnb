# data_manager.py

import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.amenity import Amenity
from models.city import City
from models.country import Country
from models.place import Place
from models.review import Review
from models.user import User

class DataManager:
    def __init__(self, storage_file='data.json'):
        self.storage_file = storage_file
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump({}, f)

        with open(self.storage_file, 'r') as f:
            self.data = json.load(f)

    def _save(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.data, f)

    # Methods for User
    def save(self, entity):
        entity_id = str(uuid.uuid4())
        entity['id'] = entity_id
        self.data[entity_id] = entity
        self._save()
        return entity

    def get(self, entity_id):
        return self.data.get(entity_id, None)

    def update(self, entity_id, new_data):
        if entity_id in self.data:
            self.data[entity_id].update(new_data)
            self._save()
            return self.data[entity_id]
        return None

    def delete(self, entity_id):
        if entity_id in self.data:
            del self.data[entity_id]
            self._save()
            return True
        return False

    def get_all(self):
        return list(self.data.values())

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    # Test methods follow...
    
    # Methods for City
    @patch.object(DataManager, 'save_city')
    def save_city(self, city):
        city_id = str(uuid.uuid4())
        city['id'] = city_id
        self.data['cities'][city_id] = city
        self._save()
        return city
        
    @patch.object(DataManager, 'get_city')
    def get_city(self, city_id):
        return self.data['cities'].get(city_id)

    @patch.object(DataManager, 'update_city')
    def update_city(self, city_id, new_data):
        if city_id in self.data['cities']:
            self.data['cities'][city_id].update(new_data)
            self._save()
            return self.data['cities'][city_id]
        return None

    @patch.object(DataManager, 'delete_city')
    def delete_city(self, city_id):
        if city_id in self.data['cities']:
            del self.data['cities'][city_id]
            self._save()
            return True
        return False

    @patch.object(DataManager, 'get_all_cities')
    def get_all_cities(self):
        return list(self.data['cities'].values())

# Tests for Country
@patch.object(DataManager, 'save_country')
def test_save_country(self, mock_save_country):
    mock_save_country.return_value = 1
    country_data = {'name': 'France'}
    country_id = self.data_manager.save_country(country_data)
    self.assertEqual(country_id, 1)
    mock_save_country.assert_called_once_with(country_data)

@patch.object(DataManager, 'get_country')
def test_get_country(self, mock_get_country):
    mock_country = Country(name='France')
    mock_get_country.return_value = mock_country
    result = self.data_manager.get_country(1)
    self.assertEqual(result.name, 'France')
    mock_get_country.assert_called_once_with(1)

@patch.object(DataManager, 'get_all_countries')
def test_get_all_countries(self, mock_get_all_countries):
    mock_countries = [Country(name='France'), Country(name='England')]
    mock_get_all_countries.return_value = mock_countries
    result = self.data_manager.get_all_countries()
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0].name, 'France')
    self.assertEqual(result[1].name, 'England')
    mock_get_all_countries.assert_called_once()

@patch.object(DataManager, 'update_country')
def test_update_country(self, mock_update_country):
    mock_update_country.return_value = True
    updated_data = {'name': 'New France'}
    result = self.data_manager.update_country(1, updated_data)
    self.assertTrue(result)
    mock_update_country.assert_called_once_with(1, updated_data)

@patch.object(DataManager, 'delete_country')
def test_delete_country(self, mock_delete_country):
    mock_delete_country.return_value = True
    result = self.data_manager.delete_country(1)
    self.assertTrue(result)
    mock_delete_country.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()
