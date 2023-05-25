#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.vehicles import Vehicle


@app.route('/vehicles')
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

    return jsonify({'status':'ok'})
