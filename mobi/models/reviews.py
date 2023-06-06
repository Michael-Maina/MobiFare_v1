#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column, ForeignKey

class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    comment = Column(String(1024))
    user_id = Column(String(60), ForeignKey('users.id'))
    vehicle_id = Column(String(60), ForeignKey('vehicles.id'))
