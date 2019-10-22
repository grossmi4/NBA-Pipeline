import nba_api
import csv
import json
from database import database
import pandas as pd
import sqlalchemy as db

# Creates dictionary of teams and their keys from csv file in assets
with open('assets/team_key.csv', mode='r') as team_key_csv:
    reader = csv.reader(team_key_csv)
    team_dict = {rows[0]:rows[1] for rows in reader}

# Establlish session with Database
DBSession = db.orm.sessionmaker(bind=database.engine)
session = DBSession()

# Pulls 2018-19 Regular Season for each team
team_keys = team_dict.values()
for team in team_keys:
    current_team = nba_api.teamgamelog(team,"2018-19","Regular Season")
    data_rowset = current_team["resultSets"][0]["rowSet"]
    data_params = current_team["parameters"]
    for game in data_rowset:
        game.insert(0,data_params["SeasonType"])
        game.insert(0,data_params["Season"])
        new_game = database.TeamGameLog(
            season = game[0],
            season_type = game[1],
            teamId = game[2],
            gameId = game[3],
            game_date = game[4],
            matchup = game[5],
            win_loss = game[6],
            season_wins = game[7],
            season_losses = game[8],
            season_win_percent = game[9],
            minutes = game[10],
            field_goals_made = game[11],
            field_goals_attempts = game[12],
            field_goals_percent = game[13],
            field_goals_3_made = game[14],
            field_goals_3_attempts = game[15],
            field_goals_3_percent = game[16],
            free_throws_made = game[17],
            free_throws_attempts = game[18],
            free_throws_percent = game[19],
            o_rebounds = game[20],
            d_rebounds = game[21],
            rebounds = game[22],
            assists = game[23],
            steals = game[24],
            blocks = game[25],
            turnovers = game[26],
            personal_fouls = game[27],
            points = game[28]
        )
        session.add(new_game)
        session.commit()





 