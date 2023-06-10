#!/usr/bin/env python3

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

class Owner(BaseModel, Base):
    __tablename__ = 'owners'

    first_name = Column(String(128))
    last_name = Column(String(128))
    phone_number = Column(String(60), unique=True)
    email_address = Column(String(60), unique=True)
    password = Column(String(255))
    payment_mode = Column(String(60))
    short_code = Column(String(60))
    account_number = Column(String(60), unique=True)

    vehicles = relationship('Vehicle', backref='owner', cascade='all')


    @property
    def vehicles(self):
        """getter attribute returns the list of vehicle instances"""
        from models.vehicles import Vehicle
        vehicle_list = []
        all_vehicles = models.storage.all(Vehicle)
        for vehicle in all_vehicles.values():
            if vehicle.owner_id == self.id:
                vehicle_list.append(vehicle)
        return vehicle_list
