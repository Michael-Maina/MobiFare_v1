#!/usr/bin/python3
"""
Initialization File
"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/")
