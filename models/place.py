#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models import storage
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id',
           String(60),
           ForeignKey('places.id'),
           primary_key=True,
           nullable=False),
    Column('amenity_id',
           String(60),
           ForeignKey('amenities.id'),
           primary_key=True,
           nullable=False)
    )


class Place(BaseModel, Base):
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        back_populates="place_amenities",
        viewonly=False
        )

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="user", cascade="delete")

    @property
    def reviews(self):
        from models import storage
        return [review for review in storage.all("Review").values()
                if review.place_id == self.id]

    @property
    def amenities(self):
        return [storage.all()['Amenity'][amenity_id] \
            for amenity_id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity):
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
