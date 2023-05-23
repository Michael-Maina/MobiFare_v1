#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column

class Vehicle(Base, BaseModel):
    __tablename__ = 'vehicles'
