import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(300), nullable=False)
    password = Column(String(300), nullable=False)

    favorites = relationship("Favorites", back_populates="user")


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    home_planet = Column(String(250))
    eye_color = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="character")

    def to_dict(self):
        return {}
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    weather = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="planet")

    def to_dict(self):
        return {}
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
