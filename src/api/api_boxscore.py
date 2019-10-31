import requests

def boxscoretraditionalv2(GameID,StartPeriod,EndPeriod,StartRange,EndRange,RangeType):
    url = "https://stats.nba.com/stats/boxscoretraditionalv2/"
    querystring = {"GameID":GameID,
                   "StartPeriod":StartPeriod,
                   "EndPeriod":EndPeriod,
                   "StartRange":StartRange,
                   "EndRange":EndRange,
                   "RangeType":RangeType
                  }
    headers = {
        'User-Agent': "Postman/7.13.0",
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()
