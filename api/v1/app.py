#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_response, redirect, url_for
from flask_cors import CORS
from models import storage
from models.users import User
from models.owners import Owner
from models.operators import Operator
from api.v1.auth import bp
from api.v1 import app_views

SECRET_KEY = "752a138157bb5c953d4affed3c12d71a314e65399139b1723e5e9f66e80106ec"

app = Flask(__name__)
CORS(app)
app.register_blueprint(bp)
app.register_blueprint(app_views)

# @app.teardown_appcontext
# def close_db(td):
#     storage.close()

from api.v1.reviews import *
from api.v1.payments import *
from api.v1.vehicles import *
from api.v1.owners import *
from api.v1.operators import *
from api.v1.users import *


if __name__ == '__main__':
    app.run(debug=True)
