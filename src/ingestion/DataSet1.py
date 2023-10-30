# DataSet1.py - script to extract data from its source and load into ADLS.

print("Sleeper ingestion")

spark.conf.set(
    "fs.azure.account.key.playerpickerpredictor.dfs.core.windows.net",
    dbutils.secrets.get(scope="PlayerPickerPredictorScope", key="ppp-key"))

uri = "abfss://football-data@playerpickerpredictor.dfs.core.windows.net/"

league_id = "1002773406472851456"

import requests
import json
import pandas as pd

players_api_response = requests.get("https://api.sleeper.app/v1/players/nfl")
league_api_response = requests.get("https://api.sleeper.app/v1/league/" + league_id)
rosters_api_response = requests.get(
    "https://api.sleeper.app/v1/league/" + league_id + "/rosters"
)

print("Getting league data")
league_content = league_api_response.content
league_data = json.loads(league_content)
league_df = pd.json_normalize(league_data)
league_df = pd.DataFrame(league_df)

print("Getting roster data")
rosters_content = rosters_api_response.content
rosters_data = json.loads(rosters_content)
rosters_df = pd.json_normalize(rosters_data)
rosters_df = pd.DataFrame(rosters_df)

print("Getting player data")
players_content = players_api_response.content
players_data = json.loads(players_content)
players_df = pd.json_normalize(players_data)
players_df = pd.DataFrame(players_df)

league_df.to_csv("league.csv")
rosters_df.to_csv("roster.csv")
players_df.to_csv("players.csv")