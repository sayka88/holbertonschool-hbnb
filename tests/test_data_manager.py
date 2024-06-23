#!/usr/bin/python3
import unittest
from unittest.mock import patch, MagicMock
from data_manager import DataManager
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from models.amenity import Amenity
from models.city import City
from models.country import Country
from models.place import Place
from models.review import Review
from models.user import User
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

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

if _name_ == '_main_':
    unittest.main()
