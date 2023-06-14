#!/usr/bin/env python3

from flask import Flask, render_template
from models import storage
from models.users import User
import uuid


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("landing_page.html", cache_id=uuid.uuid4())


@app.route('/users/<id>')
def user_dashboard(id):
    user_obj = storage.get(User, id)

    name = user_obj.first_name + ' ' + user_obj.last_name

    return render_template("user.html", cache_id=uuid.uuid4(), name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
