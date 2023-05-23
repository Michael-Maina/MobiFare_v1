#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column

class Payment(Base, BaseModel):
    __tablename__ = 'payments'
