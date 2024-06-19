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

#Cities

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = data_manager.get_all_countries()
    return jsonify(countries), 200

@app.route('/countries/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = data_manager.get_country(country_code)
    if not country:
        abort(404)
    return jsonify(country), 200

@app.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_country_cities(country_code):
    country = data_manager.get_country(country_code)
    if not country:
        abort(404)
    cities = [city for city in data_manager.get_all_cities() if city['country_code'] == country_code]
    return jsonify(cities), 200

@app.route('/cities', methods=['POST'])
def create_city():
    city = request.json
    if 'country_code' not in city or 'name' not in city:
        abort(400, 'country_code and name are required')
    country = data_manager.get_country(city['country_code'])
    if not country:
        abort(400, 'Invalid country_code')
    cities = data_manager.get_all_cities()
    if any(c['name'] == city['name'] and c['country_code'] == city['country_code'] for c in cities):
        abort(409, 'City name must be unique within the same country')
    new_city = data_manager.save_city(city)
    return jsonify(new_city), 201

@app.route('/cities', methods=['GET'])
def get_cities():
    cities = data_manager.get_all_cities()
    return jsonify(cities), 200

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = data_manager.get_city(str(city_id))
    if not city:
        abort(404)
    return jsonify(city), 200

@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    city = data_manager.get_city(str(city_id))
    if not city:
        abort(404)
    new_data = request.json
    updated_city = data_manager.update_city(str(city_id), new_data)
    return jsonify(updated_city), 200

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    if data_manager.delete_city(str(city_id)):
        return '', 204
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)
