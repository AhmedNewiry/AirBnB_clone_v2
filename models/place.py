#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models


if models.st_type == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"), primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.st_type == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)

    else:

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if models.st_type != "db":
        @property
        def reviews(self):
            """returns the list of Review instances with
               place_id equals to the current Place.id
            """
            req_rev = []
            reviews = models.storage.all(Review).values
            for review in reviews:
                if review.place_id == self.id:
                    req_rev.append(review)
            return req_rev

        @property
        def amenities(self):
            """ returns the list of Amenity instances based on the
                attribute amenity_ids that contains all
                Amenity.id linked to the Place
            """
            req_amen = []
            amenities = models.storage.all(Amenity).values
            for amenity in amenities:
                if amenity.id in self.amenity_ids:
                    req_amen.append(amenity)
            return req_amen

        @amenities.setter
        def amenities(self, value):
            """ handles append method for adding an
                Amenity.id to the attribute amenity_ids
            """
            if isinstance(value, Amenity) and value.id not in amenity_ids:
                self.amenity_ids.append(value.id)

    def __init__(self, *args, **kwargs):
        """Place class initialization"""
        super().__init__(*args, **kwargs)
