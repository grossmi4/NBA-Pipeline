from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import config as cfg

Base = declarative_base()

class BoxScore(Base):
    __tablename__ = 'boxscore'
    # id = Column('idBoxScore',Integer, primary_key=True)
    gameId = Column(String(10),primary_key=True)
    teamId = Column(String(10))
    team_abbreviation = Column(String(3))
    team_city = Column(String(20))
    playerId = Column(String(10),primary_key=True)
    player_name = Column(String(50))
    start_pos = Column(String(3))
    comment = Column(String(100))
    minutes = Column(Integer)
    field_goals_made = Column(Integer)
    field_goals_attempts = Column(Integer)
    field_goals_percent = Column(Float)
    field_goals_3_made = Column(Integer)
    field_goals_3_attempts = Column(Integer)
    field_goals_3_percent = Column(Float)
    free_throws_made = Column(Integer)
    free_throws_attempts = Column(Integer)
    free_throws_percent = Column(Float)
    o_rebounds = Column(Integer)
    d_rebounds = Column(Integer)
    rebounds = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    turnovers = Column(Integer)
    personal_fouls = Column(Integer)
    points = Column(Integer)
    plus_minus = Column(Integer)

engine = create_engine(URL(**cfg.db_config), echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
