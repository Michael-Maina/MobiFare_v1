#!/usr/bin/env python3

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship

class Vehicle(BaseModel, Base):
    __tablename__ = 'vehicles'

    number_plate = Column(String(60))
    owner_id = Column(String(60), ForeignKey('owners.id'))
    operator_id = Column(String(60), ForeignKey('operators.id'))
    reviews = relationship("Review", backref="vehicle", cascade="all")
    payments = relationship('Payment', backref='vehicle', cascade='all')

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        from models.reviews import Review
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.vehicle_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def payments(self):
        """getter attribute returns the list of payment instances"""
        from models.payments import Payment
        payments_list = []
        all_payments = models.storage.all(Payment)
        for payment in all_payments.values():
            if payment.vehicle_id == self.id:
                payments_list.append(payment)
        return payments_list
