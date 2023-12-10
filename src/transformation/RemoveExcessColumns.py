# Databricks notebook source
# Update user.csv to collect only ID and username

import pandas as pd

user = pd.read_csv("../ingestion/user.csv")

user_details = user[['username', 'user_id']]

user_details.to_csv("user_details.csv")

# COMMAND ----------

# Update roster.csv to collect ownerId and players

roster = pd.read_csv("../ingestion/roster.csv")

roster_final = roster[['owner_id', 'players']]

roster_final['players'] = roster_final['players'].replace({'\'':''}, regex=True)
roster_final['players'] = roster_final['players'].replace({'\]':''}, regex=True)
roster_final['players'] = roster_final['players'].replace({'\[':''}, regex=True)

roster_final[['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10', 'player11', 'player12', 'player13', 'player14', 'player15', 'player16']] = roster_final['players'].str.split(',',expand=True)

roster_final = roster_final.drop(columns='players')

roster_final.to_csv('rosters.csv')
