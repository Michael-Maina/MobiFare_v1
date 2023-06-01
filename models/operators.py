#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column

class Operator(BaseModel, Base):
    __tablename__ = 'operators'


    first_name = Column(String(128))
    last_name = Column(String(128))
    phone_number = Column(String(60), unique=True)
    email_address = Column(String(60), unique=True)
    password = Column(String(60))
