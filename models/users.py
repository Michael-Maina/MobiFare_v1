#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column

class User(Base, BaseModel):
    __tablename__ = 'users'

    # username = Column(String(60), nullable=False)
    # first_name = Column(String(128), nullable=False)
    # last_name = Column(String(128), nullable=False)
    # phone_number = Column(String(60), nullable=False)
    # email_address = Column(String(60), nullable=False)
    # password = Column(String(60), nullable=False)
