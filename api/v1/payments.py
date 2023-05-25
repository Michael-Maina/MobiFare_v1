#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.payments import Payment


@app.route('/payments')
def payments():
    payments_list = storage.all(Payment).values()
    list_payments = []
    for payment in payments_list:
        list_payments.append(payment.to_dict())

    return jsonify(list_payments)
