# hbnb_evolution/app.py
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models.data_manager import DataManager
from models.user import User
import re

app = Flask(__name__)
api = Api(app)
data_manager = DataManager()

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = data_manager.get(user_id, 'user')
            if not user:
                return {"error": "User not found"}, 404
            return jsonify(user)
        else:
            users = data_manager._load_entities('user')
            return jsonify(list(users.values()))

    def post(self):
        data = request.get_json()
        email = data.get('email')
        if not validate_email(email):
            return {"error": "Invalid email format"}, 400
        if any(user['email'] == email for user in data_manager._load_entities('user').values()):
            return {"error": "Email already exists"}, 409

        try:
            user = User.from_dict(data)
            data_manager.save(user)
            return jsonify(user.to_dict()), 201
        except Exception as e:
            return {"error": str(e)}, 400

    def put(self, user_id):
        user_data = data_manager.get(user_id, 'user')
        if not user_data:
            return {"error": "User not found"}, 404

        data = request.get_json()
        if 'email' in data and not validate_email(data['email']):
            return {"error": "Invalid email format"}, 400

        for key, value in data.items():
            if key in user_data:
                user_data[key] = value

        user_data['updated_at'] = datetime.now().isoformat()
        user = User.from_dict(user_data)
        data_manager.update(user)
        return jsonify(user.to_dict())

    def delete(self, user_id):
        user = data_manager.get(user_id, 'user')
        if not user:
            return {"error": "User not found"}, 404
        data_manager.delete(user_id, 'user')
        return '', 204

api.add_resource(UserResource, '/users', '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)

