import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Favorite (Base):
    __tablename__ = 'favorite'
    favoriteID = Column(Integer, primary_key=True)
    characterID = Column(Integer, ForeignKey('character.characterID'))
    nicknameID = Column(Integer, ForeignKey('register.registerID'))


class Register (Base):
    __tablename__ = 'register'
    registerID = Column(Integer,primary_key=True) 
    name = Column(String(50),nullable=False)
    password = Column(String(12),nullable=False)
    email = Column (String(50), nullable=True, unique=True)
    register = relationship('Favorite')

class Character(Base):
    __tablename__ = 'character'
    characterID = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    status = Column(String(50),nullable=False)
    episode = Column(String(50),nullable=False)
    location = Column(String(50),nullable=False)
    favoriteID = relationship('Favorite')
    Dimension = relationship ('Dimension')

class Episode(Base):
    __tablename__ = 'episode'
    episodeID = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    episode = Column(String(700),nullable=False)
    character = Column(Integer, ForeignKey('character.characterID'))
    favoriteID = relationship('Favorite')

class Dimension (Base):
    __tablename__ = 'dimension'
    dimensionID = Column(Integer, primary_key=True)
    character = Column(Integer, ForeignKey('character.characterID'))
    favoriteID = relationship('Favorite')

    
# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')