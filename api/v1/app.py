#!/usr/bin/env python3

from models import storage
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600


@app.teardown_appcontext
def close_db(td):
    storage.close()

from api.v1.reviews import *
from api.v1.payments import *
from api.v1.vehicles import *
from api.v1.owners import *
from api.v1.operators import *
from api.v1.users import *

if __name__ == '__main__':
    app.run(debug=True)
