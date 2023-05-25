#!/usr/bin/env python3

from api.v1.app import app
from flask import jsonify
from flask import request
from models import storage
from models.reviews import Review


@app.route('/reviews')
def reviews():
    reviews_list = storage.all(Review).values()
    list_reviews = []
    for review in reviews_list:
        list_reviews.append(review.to_dict())

    return jsonify(list_reviews)
