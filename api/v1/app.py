#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from models import storage
from models.users import User
from models.owners import Owner
from models.operators import Operator
from werkzeug.security import generate_password_hash, check_password_hash
from authenticate import token_required

SECRET_KEY = "752a138157bb5c953d4affed3c12d71a314e65399139b1723e5e9f66e80106ec"

app = Flask(__name__)

from api.v1.users import *
from api.v1.operators import *
from api.v1.owners import *
from api.v1.vehicles import *
from api.v1.payments import *
from api.v1.reviews import *

'''
@app.route('/pay', methods=['POST'])
def no_login():
    data = request.get_json()
    phone_number = data.get("phone_number")
'''


classes = {'User': User, 'Owner': Owner, 'Operator': Operator}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    '''
    email_address = request.get('email_address')
    password = request.form.get('password')
    app_user = request.form.get('user_type')
    '''

    if not email or not password:
        return make_response("No information was entered", 401)

    '''
    all_users = storage.all(User).values()
    all_operators = storage.all(Operator).values()
    all_owners = storage.all(Owner).values()

    for user in all_users:
        if user.email_address == email_address:
            current_member = user

    for operator in all_operators:
        if operator.email_address == email_address:
            current_member = operator

    for owner in all_owners:
        if owner.email_address == email_address:
            current_member = owner
    '''
    all_members = storage.all(classes.get(app_user)).values()

    for member in all_members:
        if member.email_address == data.get("email_address"):
            new_member = member

    if not current_member:
        return redirect(url_for("signup"))

    if check_password_hash(current_member.password, password):
        payload = {"email_address": email_address, "user_type": app_user}
        token = jwt.encode(payload, SECRET_KEY)

        return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)

    return make_response("Wrong password", 403)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    '''
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email_address = request.form.get('email_address')
    password = request.form.get('password')
    phone_number = request.form.get('phone_number')
    app_user = request.form.get('user_type')

    data = {}
    data.update({
        'first_name': first_name,
        'last_name': last_name,
        'email_address': email_address,
        'password': password,
        'phone_number': phone_number
    })
    '''

    '''
    all_members = storage.all(classes.get(app_user)).values()

    for member in all_members:
        if member.email_address == data.get("email_address"):
            new_member = member
    '''
    all_users = storage.all(User).values()
    for user in all_users:
        if user.email_address == data.get("email_address"):
            new_member = user

    if not new_member:
        #new_member = classes.get(app_user)(**data)
        new_member = User(**data)

        return redirect("localhost:5000/users/" + new_member.id)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
