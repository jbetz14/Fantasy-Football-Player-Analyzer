# Databricks notebook source
import pandas as pd

roster = pd.read_csv("../ingestion/roster.csv")

rosters = roster['players']

all_players = []

for roster in rosters:
    roster = roster.replace('[', '')
    roster = roster.replace(']', '')
    roster = roster.replace(',', '')
    roster = roster.replace('\'', '')
    roster = roster.replace('\/', '')
    players = roster.split()
    for player in players:
        player = "".join(filter(str.isdigit, player))
        all_players.append(player)

req_columns = []

valid_players = []

for player in all_players:
    if player != '':
        req_columns.append('{}.first_name'.format(player))
        req_columns.append('{}.last_name'.format(player))
        valid_players.append(player)

print(req_columns)


# COMMAND ----------

df = pd.read_csv("../ingestion/players.csv", usecols=req_columns)

melted_df = pd.melt(df, id_vars=None, value_vars=[f'{id}.first_name' for id in valid_players] + [f'{id}.last_name' for id in valid_players], var_name='variable', value_name='value')

melted_df[['id', 'type']] = melted_df['variable'].str.split('.', expand=True)

result_df = melted_df.pivot(index='id', columns='type', values='value').reset_index()

result_df.columns.name = None
result_df.columns = ['id', 'first_name', 'last_name']

display(result_df)

result_df.to_csv("rostered_players.csv")
