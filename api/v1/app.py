#!/usr/bin/env python3

from flask import Flask


app = Flask(__name__)

from api.v1.users import *
from api.v1.operators import *
from api.v1.owners import *
from api.v1.vehicles import *
from api.v1.payments import *
from api.v1.reviews import *

if __name__ == '__main__':
    app.run(debug=True)
