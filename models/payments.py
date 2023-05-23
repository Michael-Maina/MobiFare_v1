#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column, ForeignKey, Integer

class Payment(Base, BaseModel):
    __tablename__ = 'payments'

    user_id = Column(String(60), ForeignKey('users.id'))
    vehicle_id = Column(String(60), ForeignKey('vehicles.id'))
    amount = Column(Integer)
