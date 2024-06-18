#!/usr/bin/python3

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = []
user_id_counter = 1

@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    user = request.json
    user['id'] = user_id_counter
    users.append(user)
    user_id_counter += 1
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        abort(404)
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        abort(404)
    new_data = request.json
    user.update(new_data)
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
