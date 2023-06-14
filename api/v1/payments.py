#!/usr/bin/env python3

from flask import jsonify
from flask import request
from models import storage
from models.owners import Owner
from models.payments import Payment
from models.vehicles import Vehicle
from api.v1.payment_app import send_stk_push
from api.v1 import app_views

@app_views.route('/payments')
def payments():
    payments_list = storage.all(Payment).values()
    list_payments = []
    for payment in payments_list:
        list_payments.append(payment.to_dict())

    return jsonify(list_payments)

@app_views.route('/payments', methods=['POST'])
def post_payments(): # Note this has a bug suggested fix: trigger stk push from client side the have this as the route for confirmation url
    data = request.get_json()
    print(data)
    amount = data.get("amount")
    number = data.get("phone_number")
    number_plate = data.get("number_plate") # get vehicle number plate

    vehicles = storage.all(Vehicle).values() # loop throught all vehicles looking for match
    for vehicle in vehicles:
        if vehicle.to_dict().get('number_plate') == number_plate:
            vehicle_id = vehicle.to_dict().get('id')
            owner_id = vehicle.to_dict().get('owner_id')   # retrive owner_id

            owner = storage.get(Owner, owner_id) # get owner object to get shortcode
            print(owner)
            shortcode = owner.to_dict().get("short_code")
            print(shortcode)

            data['vehicle_id'] = vehicle_id

            print('here')
            response = send_stk_push(amount, number, shortcode) #trigger stkpush

            if response.get("ResponseCode") == '0':
                data["MerchantRequestID"] = response["MerchantRequestID"]
                data['status'] = "pending"
                new = Payment(**data)
                new.save()

            return jsonify({'status': 'ok'})

    return jsonify({"error":"vehicle doesn't exist"})


@app_views.route('/confirmation', methods=['POST'])#This is the confirmation URL for confirming the stk push
def confirm_payments():
    data = request.get_json()

    payments = storage.all(Payment).values()
    MerchantRequestID = data['Body']['stkCallback']['MerchantRequestID']

    for payment in payments:
        if payment.to_dict().get('MerchantRequestID') == MerchantRequestID:
            if data['Body']['stkCallback']['ResultCode'] == 0:
                setattr(payment, 'status', 'completed')
            else:
                setattr(payment, 'status', 'cancelled')

            break

    return jsonify([])
