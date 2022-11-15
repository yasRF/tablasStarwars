import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(String(250), ForeignKey("user.id"))
    post_id = Column(String(250), ForeignKey("post.id"))


class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey("user.id"))


class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(String(250), ForeignKey("post.id"))


class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(String(250), ForeignKey("user.id"))

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')