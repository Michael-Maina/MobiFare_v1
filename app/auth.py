#!/usr/bin/env python3

from flask import render_template, jsonify, redirect, request
from flask import Blueprint, g, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from models import storage
from models.users import User
from models.owners import Owner
from models.operators import Operator

bp = Blueprint('auth', __name__, url_prefix='/auth')

classes = {'User': User, 'Owner': Owner, 'Operator': Operator}


@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email_address')
    password = data.get('password')
    f_name = data.get('first_name')
    l_name = data.get('last_name')
    p_number = data.get('phone_number')
    user_type = classes.get(data.get('user_type'))

    all_users = storage.all(user_type).values()
    check = False

    for user in all_users:
        if user.email_address == email:
            check = True
            return redirect(url_for('auth.login'))

    if not check:
        data.update({'password': generate_password_hash(password)})
        new_user = user_type(**data)
        session.clear()
        session['user_id'] = new_user.id
        return redirect('localhost:5000/users/' + new_user.id)


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email_address')
    password = data.get('password')
    user_type = classes.get(data.get('user_type'))

    all_users = storage.all(user_type).values()
    check = False

    for user in all_users:
        if user.email_address == email:
            if check_password_hash(user.password, password):
                check = True
                session.clear()
                session['user_id'] = user.id
                return redirect('localhost:5000/users/' + user.id)
            else:
                flash('Incorrect password')
                return render_template('auth/login.html')

    if not check:
        flash('User does not exist')
        return redirect(url_for('auth.signup'))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect('localhost:5000/')


'''
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = storage.get(user_id)
'''