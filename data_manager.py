#!/usr/bin/python3
# data_manager.py

import uuid
import json
import os
import sys
from unittest.mock import patch

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

    # Methods for Country
    def save_country(self, country):
        country_code = country['code']
        self.data['countries'][country_code] = country
        self._save()

    def get_country(self, country_code):
        return self.data['countries'].get(country_code)

    def get_all_countries(self):
        return list(self.data['countries'].values())

    # Methods for City
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
