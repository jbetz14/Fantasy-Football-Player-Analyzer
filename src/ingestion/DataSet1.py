# DataSet1.py - script to extract data from its source and load into ADLS.

print("Sleeper ingestion")

spark.conf.set(
    "fs.azure.account.key.playerpickerpredictor.dfs.core.windows.net",
    dbutils.secrets.get(scope="PlayerPickerPredictorScope", key="ppp-key"))

uri = "abfss://football-data@playerpickerpredictor.dfs.core.windows.net/"

# User ID and League ID hard coded... Input your user_id and league_id
user_id = "1002785068257038336"
league_id = "1002773406472851456"

import requests
import json
import pandas as pd

print("Getting user data")
user_api_response = requests.get("https://api.sleeper.app/v1/user/" + user_id)
user_content = user_api_response.content
user_data = json.loads(user_content)
user_df = pd.json_normalize(user_data)
user_df = pd.DataFrame(user_df)

print("Getting league data")
league_api_response = requests.get("https://api.sleeper.app/v1/league/" + league_id)
league_content = league_api_response.content
league_data = json.loads(league_content)
league_df = pd.json_normalize(league_data)
league_df = pd.DataFrame(league_df)

print("Getting roster data")
rosters_api_response = requests.get(
    "https://api.sleeper.app/v1/league/" + league_id + "/rosters"
)
rosters_content = rosters_api_response.content
rosters_data = json.loads(rosters_content)
rosters_df = pd.json_normalize(rosters_data)
rosters_df = pd.DataFrame(rosters_df)

print("Getting projection data")
projection_api_response = requests.get("https://api.sleeper.app/v1/projections/nfl/regular/2024")
projection_content = projection_api_response.content
projection_data = json.loads(projection_content)
projection_df = pd.json_normalize(projection_data)
projection_df = pd.DataFrame(projection_df)

print(projection_df)

print("Getting weekly projection data")

num_weeks = range(1,19)
for week in num_weeks:
    print(week)
    weekly_projection_api_response = requests.get("https://api.sleeper.app/v1/projections/nfl/regular/2023/{}".format(str(week)))
    weekly_projection_content = weekly_projection_api_response.content
    weekly_projection_data = json.loads(weekly_projection_content)
    weekly_projection_df = pd.json_normalize(weekly_projection_data)
    weekly_projection_df = pd.DataFrame(weekly_projection_df)
    weekly_projection_df.to_csv("week_{}_projections.csv".format(week))


# You only have to run this once to get all players, vary large dataset
players_api_response = requests.get("https://api.sleeper.app/v1/players/nfl")
print("Getting player data")
players_content = players_api_response.content
players_data = json.loads(players_content)
players_df = pd.json_normalize(players_data)
players_df = pd.DataFrame(players_df)

projection_df.to_csv("projections.csv")
user_df.to_csv("user.csv")
league_df.to_csv("league.csv")
rosters_df.to_csv("roster.csv")
players_df.to_csv("players.csv")