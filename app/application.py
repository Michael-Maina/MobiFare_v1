#!/usr/bin/env python3

from flask import Flask, render_template
from models import storage
from models.users import User
import uuid
import auth


app = Flask(__name__)
app.register_blueprint(auth.bp)


@app.route('/')
def home():
    return render_template("landing_page.html", cache_id=uuid.uuid4())


@app.route('/users/<id>')
def user_dashboard(id):
    user_obj = storage.get(User, id)

    name = user_obj.first_name + ' ' + user_obj.last_name

    return render_template("user.html", cache_id=uuid.uuid4(), name=name)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
