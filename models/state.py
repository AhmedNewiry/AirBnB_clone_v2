#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models.st_type == "db":
        __tablename__ = "states"
        name = Column(String(128),nullable=False)
        cities = relationship("City", backref="state", cascade="delete")


    else:
        name = ""

        @property
        def cities():
            req_cities = []
            cities = models.storage.all(City).values()
            for city in cities:
                if city.state_id == self.id:
                    req_cities.append(city)
            return req_cities

    def __init__(self, *args, **kwargs):
        """state class initialization"""
        super().__init__(*args, **kwargs)
