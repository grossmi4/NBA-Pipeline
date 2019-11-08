from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from .config import db_config

Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'
    TeamName = Column(String)
    TeamID = Column(Integer, primary_key=True)

engine = create_engine(URL(**db_config), echo=True)