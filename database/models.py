from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import config as cfg

Base = declarative_base()

class TeamGameLog(Base):
    __tablename__ = 'teamgamelog'
    id = Column('idTeamGameLog',Integer, primary_key=True)
    season = Column(String(10))
    season_type = Column(String(45))
    teamId = Column(String(10))
    gameId = Column(String(10))
    game_date_text = Column(String(14))
    game_date = Column(Date)
    matchup = Column(String(20))
    win_loss = Column(String(10))
    season_wins = Column(Integer)
    season_losses = Column(Integer)
    season_win_percent = Column(Float)
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
    record_insert_date = Column(DateTime)

engine = create_engine(URL(**cfg.db_config), echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
