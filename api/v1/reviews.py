#!/usr/bin/env python3

from flask import jsonify
from flask import request
from models import storage
from models.reviews import Review
from api.v1 import app_views


@app_views.route('/reviews')
def reviews():
    reviews_list = storage.all(Review).values()
    list_reviews = []
    for review in reviews_list:
        list_reviews.append(review.to_dict())

    return jsonify(list_reviews)


@app_views.route('/reviews', methods=['POST'])
def post_reviews():
    data = request.get_json()

    new_instance = Review(**data)
    new_instance.save()

    return jsonify(new_instance.to_dict())
