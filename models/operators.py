#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column

class Operator(Base, BaseModel):
    __tablename__ = 'operators'
