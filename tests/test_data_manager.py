import os
import unittest
from persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager(storage_file='test_data.json')
        # Ensure the test data file is empty before each test
        self.data_manager.data = {}
        self.data_manager._save_data()

    def tearDown(self):
        # Remove the test data file after each test
        os.remove('test_data.json')

    def test_save_entity(self):
        entity = {'name': 'Test Entity'}
        saved_entity = self.data_manager.save(entity)
        self.assertIn('id', saved_entity)
        self.assertEqual(saved_entity['name'], 'Test Entity')

    def test_get_entity(self):
        entity = {'name': 'Test Entity'}
        saved_entity = self.data_manager.save(entity)
        retrieved_entity = self.data_manager.get(saved_entity['id'])
        self.assertEqual(retrieved_entity, saved_entity)

    def test_update_entity(self):
        entity = {'name': 'Test Entity'}
        saved_entity = self.data_manager.save(entity)
        updated = self.data_manager.update(saved_entity['id'], {'name': 'Updated Entity'})
        self.assertTrue(updated)
        retrieved_entity = self.data_manager.get(saved_entity['id'])
        self.assertEqual(retrieved_entity['name'], 'Updated Entity')

    def test_delete_entity(self):
        entity = {'name': 'Test Entity'}
        saved_entity = self.data_manager.save(entity)
        deleted = self.data_manager.delete(saved_entity['id'])
        self.assertTrue(deleted)
        retrieved_entity = self.data_manager.get(saved_entity['id'])
        self.assertIsNone(retrieved_entity)

    def test_get_all_entities(self):
        entity1 = {'name': 'Entity 1'}
        entity2 = {'name': 'Entity 2'}
        self.data_manager.save(entity1)
        self.data_manager.save(entity2)
        all_entities = self.data_manager.get_all()
        self.assertEqual(len(all_entities), 2)

if __name__ == '__main__':
    unittest.main()
