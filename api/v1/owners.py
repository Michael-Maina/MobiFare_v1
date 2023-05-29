#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.owners import Owner
from models.vehicles import Vehicle


@app.route('/owners', methods=['GET'])
def owners():
    owners_list = storage.all(Owner).values()
    list_owners = []
    for owner in owners_list:
        list_owners.append(owner.to_dict())

    return jsonify(list_owners)


@app.route('/owners/<id>', methods=['GET'])
def get_owner(id):
    owner = storage.get(Owner, id)

    if owner:
        return jsonify(owner.to_dict())

    return jsonify([])


@app.route('/owners', methods=['POST'])
def post_owner():
    data = request.get_json()

    new_instance = Owner(**data)
    new_instance.save()

    return jsonify(new_instance.to_dict())


@app.route('/owners/<id>/vehicles', methods=['GET'])
def owner_vehicles(id):
    owner = storage.get(Owner, id)
    new = []
    vehicles = owner.vehicles
    for vehicle in vehicles:
        new.append(vehicle.to_dict())

    return jsonify(new)


@app.route('/owners/<id>/vehicles', methods=['POST'])
def post_vehicle(id):
    data = request.get_json()

    new_instance = Vehicle(**data)
    new_instance.owner_id = id
    new_instance.save()

    return jsonify(new_instance.to_dict())
