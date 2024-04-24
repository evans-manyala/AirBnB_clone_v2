#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import Base

class State(BaseModel, Base):
    """This class defines the State model"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # Add relationship to City model
    cities = relationship("City", backref='state',
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """
        returns the list of City instances with state_id equals
        to the current State.id
        """
        from models import storage
        related_cities = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                related_cities.append(city)
        return related_cities
