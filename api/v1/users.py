#!/usr/bin/env python3

from flask import jsonify, redirect, url_for, render_template
from flask import request
from hashlib import sha256
from models import storage
from models.users import User
from api.v1 import app_views


@app_views.route('/users', methods=['GET'])
def get_users():
    user_list = storage.all(User).values()
    list_users = []
    for user in user_list:
        list_users.append(user.to_dict())

    return jsonify(list_users)


@app_views.route('/users', methods=['POST'])
def post_users():
    data = request.get_json()
    print(data)
    passhash = sha256(data["password"].encode())
    data.update({"password": passhash.hexdigest()})
    new = User(**data)
    new.save()

    return jsonify(new.to_dict())


@app_views.route('/users/<id>')
def user_id(id):
    user_list = storage.all(User).values()

    for user in user_list:
        if user.to_dict()['id'] == id:
            return jsonify(user.to_dict())

    return jsonify([])


@app_views.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = storage.get(User, id)

    if user:
        storage.delete(user)
    return jsonify({'status': 'ok'})


@app_views.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = storage.get(User, id)

    data = request.get_json()

    if user:
        for attr, value in data.items():
            setattr(user, attr, value)

        user.save()
        return jsonify({'status': 'ok'})

    return jsonify([])


@app_views.route('/users/<id>/payments', methods=['GET'])
def user_payments(id):
    user = storage.get(User, id)
    new = []
    if user:
        payments_list = user.payments

        for payment in payments_list:
            new.append(payment.to_dict())

        return jsonify(new)

    return jsonify([])
