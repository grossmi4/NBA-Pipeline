# 🏀NBA - Data Pipeline

# Dimensional Model
## Player Game
- Player ID
- Game ID
- Team ID
- FG Attempts
- FG Makes
- **FG %**
- 3PA
- **3PM**
- 3P %
- **TO**
- **Steals**
- **Blocks**
- FTA
- FTM
- **FT%**
- **Rebounds**
- **Assists**
- **Points**
## Player
- Player ID
- First Name
- Last Name
- Team
- Height?
- Weight?
- Years Played?
## Game
- Date
- Time
- Location
- Home Team
- Away Team
- Division Matchup
- Conference Matchup


## Team
- Team ID
- Team Name
- Team Abbreviation
- City
- State
- Country


## Team Chemistry
- Team ID
- Current Average Tenure


## Player Chemistry
- Player ID - Player ID
- Count of Games together
# NBA API Endpoints
## Teamgamelog
- TeamID
- Season
- SeasonType
-  https://stats.nba.com/stats/teamgamelog/?TeamID=1610612748&Season=2018-19&SeasonType=Regular%20Season
## Boxscoretraditionalv2
- GameID
- StartPeriod
- EndPeriod
- StartRange
- EndRange
- RangeType
- https://stats.nba.com/stats/boxscoretraditionalv2/?GameID=0021801221&StartPeriod=1&EndPeriod=4&StartRange=1&EndRange=0&RangeType=0
# NBA API Parameters
## **LeagueID**

NBA: 00 ABA: 01

## **TeamID**

Current Teams

| **Team name**          | **TeamID** |
| ---------------------- | ---------- |
| Atlanta Hawks          | 1610612737 |
| Boston Celtics         | 1610612738 |
| Brooklyn Nets          | 1610612751 |
| Charlotte Hornets      | 1610612766 |
| Chicago Bulls          | 1610612741 |
| Cleveland Cavaliers    | 1610612739 |
| Dallas Mavericks       | 1610612742 |
| Denver Nuggets         | 1610612743 |
| Detroit Pistons        | 1610612765 |
| Golden State Warriors  | 1610612744 |
| Houston Rockets        | 1610612745 |
| Indiana Pacers         | 1610612754 |
| Los Angeles Clippers   | 1610612746 |
| Los Angeles Lakers     | 1610612747 |
| Memphis Grizzlies      | 1610612763 |
| Miami Heat             | 1610612748 |
| Milwaukee Bucks        | 1610612749 |
| Minnesota Timberwolves | 1610612750 |
| New Orleans Pelicans   | 1610612740 |
| New York Knicks        | 1610612752 |
| Oklahoma City Thunder  | 1610612760 |
| Orlando Magic          | 1610612753 |
| Philadelphia 76ers     | 1610612755 |
| Phoenix Suns           | 1610612756 |
| Portland Trail Blazers | 1610612757 |
| Sacramento Kings       | 1610612758 |
| San Antonio Spurs      | 1610612759 |
| Toronto Raptors        | 1610612761 |
| Utah Jazz              | 1610612762 |
| Washington Wizards     | 1610612764 |

## **Season:**

Format: NNNN-NN (eg. 1995-96)

## **Game ID:**

Format: 002"YY-1""Game Number" (eg. 0021600001, 2017 Season First Game)

## **SeasonType:**

One of: "Regular Season", "Pre Season", "Playoffs", "All-Star", "All Star", "Preseason"

## **PerMode**

"Totals", "PerGame", "Per36"

## **Scope**

One of: "RS", "S", "Rookies"

