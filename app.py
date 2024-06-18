#!/usr/bin/python3

from flask import Flask, request, jsonify
from persistence.data_manager import DataManager

app = Flask(__name__)
data_manager = DataManager()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # Логика валидации и сохранения пользователя
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
    updated_user = data_manager.update(user_id, data)
    return jsonify(updated_user), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = data_manager.delete(user_id)
    if result:
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
