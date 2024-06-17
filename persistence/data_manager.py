#!/usr/bin/python3
# DataManager Implementation

import json
import os
import uuid
from persistence.ipersistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, storage_file='data.json'):
        self.storage_file = storage_file
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.storage_file):
            return {}
        with open(self.storage_file, 'r') as file:
            return json.load(file)

    def _save_data(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.data, file)

    def save(self, entity):
        entity_id = str(uuid.uuid4())
        entity['id'] = entity_id
        self.data[entity_id] = entity
        self._save_data()
        return entity

    def get(self, entity_id):
        return self.data.get(entity_id, None)

    def update(self, entity_id, new_data):
        if entity_id in self.data:
            self.data[entity_id].update(new_data)
            self._save_data()
            return True
        return False

    def delete(self, entity_id):
        if entity_id in self.data:
            del self.data[entity_id]
            self._save_data()
            return True
        return False

    def get_all(self):
        return list(self.data.values())

