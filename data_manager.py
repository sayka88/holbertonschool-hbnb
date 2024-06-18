#!/usr/bin/python3
# DataManager Implementation

import uuid
import json
import os

class DataManager:
    def __init__(self, storage_file='data.json'):
        self.storage_file = storage_file
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump({}, f)

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
