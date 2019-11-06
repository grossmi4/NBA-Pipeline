from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

db_config = {
    'drivername':'mysql+pymysql',
    'host':'localhost',
    'username':'admin',
    'password':'thisisapassword',
    'database':'NBA',
    'port':3306
}

engine = create_engine(URL(**db_config), echo=True)