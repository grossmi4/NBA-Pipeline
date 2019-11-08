from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from .config import db_config, engine

Base = declarative_base()

class Game(Base):
    __tablename__ = 'game'
    id = Column('GameId', Integer, primary_key=True)
    TeamHome = Column(Integer)
    TeamAway = Column(Integer)
    Season = Column(String(20))
    Winner = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)