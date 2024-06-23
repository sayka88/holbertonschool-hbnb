import json
import uuid
import os

from models.amenity import Amenity
from models.city import City
from models.country import Country
from models.place import Place
from models.review import Review
from models.user import User

class DataManager:
    def _init_(self, storage_file='data.json'):
        self.storage_file = storage_file
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump({'cities': {}, 'countries': {}}, f)
        
        with open(self.storage_file, 'r') as f:
            self.data = json.load(f)
    
    def _save(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.data, f)

    # Methods for City
    def save_city(self, city):
        city_id = str(uuid.uuid4())
        city['id'] = city_id
        self.data['cities'][city_id] = city
        self._save()
        return city_id

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

    # Methods for Country
    def save_country(self, country):
        country_id = str(uuid.uuid4())
        country['id'] = country_id
        self.data['countries'][country_id] = country
        self._save()
        return country_id

    def get_country(self, country_id):
        return self.data['countries'].get(country_id)

    def update_country(self, country_id, new_data):
        if country_id in self.data['countries']:
            self.data['countries'][country_id].update(new_data)
            self._save()
            return self.data['countries'][country_id]
        return None

    def delete_country(self, country_id):
        if country_id in self.data['countries']:
            del self.data['countries'][country_id]
            self._save()
            return True
        return False

    def get_all_countries(self):
        return list(self.data['countries'].values())
