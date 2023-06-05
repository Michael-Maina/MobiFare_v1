#!/usr/bin/env python3

from flask import Flask, render_template
import uuid

app = Flask(__name__)

from app.auth import auth
app.register_blueprint(auth.bp)

@app.route('/')
def home():
    return render_template("landing_page.html", cache_id=uuid.uuid4())

@app.route('/users/<id>')
def user_dashboard(id):
    return render_template("user.html", cache_id=uuid.uuid4())

if __name__ == '__main__':
    app.run(port=3000, debug=True)
