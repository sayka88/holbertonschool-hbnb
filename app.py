#!/usr/bin/python3

from flask import Flask, request, jsonify
from persistence.data_manager import DataManager
import re

app = Flask(__name__)
data_manager = DataManager()

def validate_user(data):
    if 'email' not in data or not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return False
    if 'first_name' not in data or not isinstance(data['first_name'], str) or not data['first_name']:
        return False
    if 'last_name' not in data or not isinstance(data['last_name'], str) or not data['last_name']:
        return False
    return True

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not validate_user(data):
        return jsonify({'error': 'Invalid data'}), 400
    new_user = data_manager.save(data)
    return jsonify(new_user), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = data_manager.get_all()
    return jsonify(users), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not validate_user(data):
        return jsonify({'error': 'Invalid data'}), 400
    updated_user = data_manager.update(user_id, data)
    if updated_user:
        return jsonify(updated_user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = data_manager.delete(user_id)
    if result:
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
