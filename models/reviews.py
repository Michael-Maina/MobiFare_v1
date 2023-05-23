#!/usr/bin/env python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import String, Column

class Review(Base, BaseModel):
    __tablename__ = 'reviews'
