#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.owners import Owner


@app.route('/owners')
def owners():
    owners_list = storage.all(Owner).values()
    list_owners = []
    for owner in owners_list:
        list_owners.append(owner.to_dict())

    return jsonify(list_owners)
