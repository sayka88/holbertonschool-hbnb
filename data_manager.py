#!/usr/bin/python3
# DataManager Implementation

import uuid
import json
import os

from models.amenity import Amenity
from models.city import City
from models.country import Country
from models.place import Place
from models.review import Review
from models.user import User
from data_manager import DataManager

class DataManager:
    def __init__(self, storage_file='data.json'):
        self.storage_file = storage_file
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump({}, f)
    
    # Methods for User
    def save(self, entity):
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
        
        entity_id = str(len(data) + 1)
        entity['id'] = entity_id
        data[entity_id] = entity

        with open(self.storage_file, 'w') as f:
            json.dump(data, f)
        
        return entity

    def get(self, entity_id):
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
        
        return data.get(entity_id, None)

    def update(self, entity_id, new_data):
        with open(self.storage_file, 'r') as f:
            data = json.load(f)

        if entity_id in data:
            data[entity_id].update(new_data)
            with open(self.storage_file, 'w') as f:
                json.dump(data, f)
            return data[entity_id]
        return None

    def delete(self, entity_id):
        with open(self.storage_file, 'r') as f:
            data = json.load(f)

        if entity_id in data:
            del data[entity_id]
            with open(self.storage_file, 'w') as f:
                json.dump(data, f)
            return True
        return False

    def get_all(self):
        with open(self.storage_file, 'r') as f:
            data = json.load(f)
        return list(data.values())

# Methods for Country
class DataManager:
    def __init__(self, file_name='data.json'):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as f:
                json.dump({'countries': {}, 'cities': {}}, f)
        else:
            with open(self.file_name, 'r') as f:
                self.data = json.load(f)

    def save_country(self, country):
        self.data['countries'][country['code']] = country
        self._save()

    def get_country(self, country_code):
        return self.data['countries'].get(country_code)

    def get_all_countries(self):
        return list(self.data['countries'].values())

    def save_city(self, city):
        city_id = str(len(self.data['cities']) + 1)
        city['id'] = city_id
        self.data['cities'][city_id] = city
        self._save()
        return city

    def get_city(self, city_id):
        return self.data['cities'].get(city_id)

    def update_city(self, city_id, new_data):
        if city_id in self.data['cities']:
            self.data['cities'][city_id].update(new_data)
            self._save()
            return self.data['cities'][city_id]
        return None

    def delete_city(self, city_id):
        if city_id in self.data['cities']:
            del self.data['cities'][city_id]
            self._save()
            return True
        return False

    def get_all_cities(self):
        return list(self.data['cities'].values())

    def _save(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f)
