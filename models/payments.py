#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column, ForeignKey, Integer

class Payment(BaseModel, Base):
    __tablename__ = 'payments'

    user_id = Column(String(60), ForeignKey('users.id'))
    vehicle_id = Column(String(60), ForeignKey('vehicles.id'))
    number_plate = Column(String(60))
    amount = Column(Integer)
    status = Column(String(60))
    MerchantRequestID = Column(String(60))


