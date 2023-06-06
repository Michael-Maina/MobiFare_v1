#!/usr/bin/env python3

from flask import Flask, render_template
from flask_cors import CORS
from models import storage
from models.owners import Owner
from models.users import User
import uuid

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("landing_page.html", cache_id=uuid.uuid4())

@app.route('/users/<id>')
def user_dashboard(id):
    user_obj = storage.get(User, id)

    name = user_obj.first_name + ' ' + user_obj.last_name

    return render_template("user.html", cache_id=uuid.uuid4(), name=name)

@app.route('/owners/<id>')
def owner_dashboard(id):
    owner_obj = storage.get(Owner, id)

    name = owner_obj.first_name + ' ' + owner_obj.last_name

    return render_template("owner.html", cache_id=uuid.uuid4(), name=name)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
