#!/usr/bin/python3
"""class definition of a State and an instance Base"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ base class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
