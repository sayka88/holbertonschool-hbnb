#!/usr/bin/python3

import unittest
import json
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.app.post('/users', data=json.dumps({
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
    
    def test_get_user(self):
        response = self.app.post('/users', data=json.dumps({
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }), content_type='application/json')
        user_id = json.loads(response.data)['id']
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.app.post('/users', data=json.dumps({
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }), content_type='application/json')
        user_id = json.loads(response.data)['id']
        response = self.app.put(f'/users/{user_id}', data=json.dumps({
            'email': 'test@example.com',
            'first_name': 'Jane',
            'last_name': 'Doe'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = self.app.post('/users', data=json.dumps({
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }), content_type='application/json')
        user_id = json.loads(response.data)['id']
        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
