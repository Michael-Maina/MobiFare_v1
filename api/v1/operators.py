#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.operators import Operator


@app.route('/operators')
def operators():
    operators_list = storage.all(Operator).values()
    list_operators = []
    for operator in operators_list:
        list_operators.append(operator.to_dict())

    return jsonify(list_operators)
