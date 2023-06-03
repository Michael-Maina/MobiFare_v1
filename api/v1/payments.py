#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.owners import Owner
from models.payments import Payment
from models.vehicles import Vehicle
from api.v1.payment_app import send_stk_push

@app.route('/payments')
def payments():
    payments_list = storage.all(Payment).values()
    list_payments = []
    for payment in payments_list:
        list_payments.append(payment.to_dict())

    return jsonify(list_payments)

@app.route('/payments', methods=['POST'])
def post_payments(): # Note this has a bug suggested fix: trigger stk push from client side the have this as the route for confirmation url
    data = request.get_json()
    print(data)
    amount = data.get("amount")
    number = data.get("phone_number")
    # shortcode = data.get("shortcode")
    number_plate = data.get("number_plate") # get vehicle number plate

    vehicles = storage.all(Vehicle).values() # loop throught all vehicles looking for match
    for vehicle in vehicles:
        if vehicle.to_dict().get('number_plate') == number_plate:
            owner_id = vehicle.to_dict().get('owner_id')   # retrive owner_id

            owner = storage.get(Owner, owner_id) # get owner object to get shortcode
            print(owner)
            shortcode = owner.to_dict().get("short_code")
            print(shortcode)

            response = send_stk_push(amount, number, shortcode) #trigger stkpush
            if response.get("ResponseCode") == '0':
                new = Payment(**data)
                new.save()

            return jsonify({'status': 'ok'})

    return jsonify({"error":"vehicle doesn't exist"})
