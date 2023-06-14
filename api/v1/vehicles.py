#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.vehicles import Vehicle


@app.route('/vehicles', methods=['GET'])
def vehicles():
    vehicles_list = storage.all(Vehicle).values()
    list_vehicles = []
    for vehicle in vehicles_list:
        list_vehicles.append(vehicle.to_dict())

    return jsonify(list_vehicles)


@app.route('/vehicles', methods=['POST'])
def post_vehicles():
    data = request.get_json()
    print(data)
    new = Vehicle(**data)
    new.save()

    return jsonify({'status': 'ok'})

@app.route('/vehicles/<id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = storage.get(Vehicle, id)

    if vehicle:
        storage.delete(vehicle)
        return jsonify({'status': 'ok'})

    return jsonify([])


@app.route('/vehicles/<id>', methods=['GET'])
def get_vehicle(id):
    vehicle = storage.get(Vehicle, id)
    if vehicle:
        return jsonify(vehicle.to_dict())

    return jsonify([])


@app.route('/vehicles/<id>/reviews', methods=['GET'])
def get_reviews(id):
    vehicle = storage.get(Vehicle, id)
    new = []
    if vehicle:
        reviews_list = vehicle.reviews

        for review in reviews_list:
            new.append(review.to_dict())

        return jsonify(new)

    return jsonify([])

@app.route('/vehicles/<id>/payments', methods=['GET'])
def get_payments(id):
    vehicle = storage.get(Vehicle, id)
    new = []
    if vehicle:
        payment_list = vehicle.payments

        for payment in payment_list:
            new.append(payment.to_dict())

        return jsonify(new)

    return jsonify([])
