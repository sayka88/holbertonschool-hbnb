#!/usr/bin/python3
"""Importing Packages and required Libraries"""
import uniitest
import json
from app import app, data_manager


class UserApiTestCase(unittest.TestCase):
    """User Api Class"""
    def setup(self):
        self.client = app.test_client()
        self.client.testing = True
        self.test_user = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'password'
        }

    def test_create_user(self):
        response = self.client.post(
            '/users', data=json.dumps(self.test_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_all_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.client.post(
            '/users', data=json.dumps(self.test_user),
            content_type='application/json'
        )
        user_id = json.loads(response.data)['id']
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.client.post(
            '/users', data=json.dumps(self.test_user),
            content_type='application/json'
        )
        user_id = json.loads(response.data)['id']
        updated_data = {'first_name': 'Updated'}
        response = self.client.put(
            f'/users/{user_id}',
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['first_name'], 'Updated')

    def test_delete_user(self):
        response = self.client.post(
            '/users', data=json.dumps(self.test_user),
            content_type='application/json'
        )
        user_id = json.loads(response.data)['id']
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
