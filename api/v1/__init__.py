#!/usr/bin/python3
"""
Initialization File
"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/")

from api.v1.reviews import *
from api.v1.payments import *
from api.v1.vehicles import *
from api.v1.owners import *
from api.v1.operators import *
from api.v1.users import *
