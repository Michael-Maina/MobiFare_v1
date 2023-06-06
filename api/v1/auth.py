#!/usr/bin/env python3

from flask import render_template, jsonify, flash, redirect, request
from flask import Blueprint, g, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from models import storage
from models.users import User
from models.owners import Owner
from models.operators import Operator

bp = Blueprint('auth', __name__, url_prefix='')

classes = {'user': User, 'owner': Owner, 'operator': Operator}


@bp.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
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
                new_user.save()
                #session.clear()
                #session['user_id'] = new_user.id
                return redirect('http://localhost:3000/users/' + new_user.id, 301)
    return redirect('http://localhost:3000/', 301)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
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
                    return redirect('localhost:3000/users/' + user.id, 301)
                else:
                    flash('Incorrect password')
                    return jsonify({'error': 'wrong password'})

                if not check:
                    flash('User does not exist')
                    return redirect(url_for('auth.signup'), 301)

    return redirect('http://localhost:3000/', 301)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect('localhost:5000/')
