#!/usr/bin/env python3

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    __tablename__ = 'users'

    username = Column(String(60))
    first_name = Column(String(128))
    last_name = Column(String(128))
    phone_number = Column(String(60))
    email_address = Column(String(60))
    password = Column(String(60))

    payments = relationship('Payment', backref='user', cascade='all')
    reviews = relationship("Review", backref="user", cascade="all")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    @property
    def payments(self):
        """getter attribute returns the list of payment instances"""
        from models.payments import Payment
        payments_list = []
        all_payments = models.storage.all(Payment)
        for payment in all_payments.values():
            if payment.user_id == self.id:
                payments_list.append(payment)
        return payments_list

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        from models.reviews import Review
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.user_id == self.id:
                review_list.append(review)
        return review_list
