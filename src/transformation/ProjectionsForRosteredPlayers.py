# Databricks notebook source
import pandas as pd

rostered_players = pd.read_csv("rostered_players.csv")

players = rostered_players['id']

req_columns = []

weeks = range(1,19)

final_df = pd.DataFrame()

for week in weeks:

    week_projected_cols = pd.read_csv("../ingestion/week_{}_projections.csv".format(week), nrows=0).columns.tolist()

    for player in players:
        col_name = f"{player}.pts_ppr"
        if col_name in week_projected_cols:
            req_columns.append(col_name)

    player_projections = pd.read_csv("../ingestion/week_{}_projections.csv".format(week), usecols=list(set(req_columns)))

    melted_df = pd.melt(player_projections, id_vars=None, value_vars=req_columns, var_name='variable', value_name='value')

    melted_df[['id', 'type']] = pd.DataFrame(melted_df['variable'].apply(lambda x: x.split('.') if '.' in x else [x, None]).tolist(),
                                              columns=['id', 'type'])
    result_df = melted_df.pivot(index='id', columns='type', values='value').reset_index()

    result_df.columns.name = None
    result_df.columns = ['id', 'week_{}_pts_ppr'.format(week)]

    req_columns = []

    if final_df.empty:
        final_df = result_df
    else:
        final_df = pd.concat([final_df, result_df.drop(columns=['id'])], axis=1)

final_df.to_csv("weekly_point_ppr.csv")
