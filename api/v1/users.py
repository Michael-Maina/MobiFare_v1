#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.users import User


@app.route('/users', methods=['GET'])
def get_users():
    user_list = storage.all(User).values()
    list_users = []
    for user in user_list:
        list_users.append(user.to_dict())

    return jsonify(list_users)


@app.route('/users', methods=['POST'])
def post_users():
    data = request.get_json()
    print(data)
    new = User(**data)
    new.save()

    return jsonify({'status': 'ok'})


@app.route('/users/<id>')
def user_id(id):
    user_list = storage.all(User).values()

    for user in user_list:
        if user.to_dict()['id'] == id:
            return jsonify(user.to_dict())

    return jsonify([])


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = storage.get(User, id)

    if user:
        storage.delete(user)
    return jsonify({'status': 'ok'})


@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = storage.get(User, id)

    data = request.get_json()

    if user:
        for key, value in data.items():
            setattr(user, key, value)

        storage.save()
    return jsonify({'status': 'ok'})
