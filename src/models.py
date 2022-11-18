import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class USER(Base):
    __tablename__ = 'USER'
    user_id = Column(Integer, primary_key=True)
    Password = Column(String(8))


class PLANETAS(Base):
    __tablename__ = 'PLANETS'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250))


class PERSONAS(Base):
    __tablename__ = 'PERSONAS'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250))


class FAVORITOS(Base):
    __tablename__ = 'FAVORITOS'
    user_id(Integer, ForeignKey("user.id"))
    Planet_fav(String, ForeignKey("planetas.id"))
    Personas_fav(String, ForeignKey("personas.id"))



class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(String(250), ForeignKey("user.id"))

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')