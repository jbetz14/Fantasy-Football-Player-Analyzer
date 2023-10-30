# ExploratoryAnalysis.py - script to do EDA (exploratory data analysis) on the two primary data sets for the project. 

# Note - alternative approaches can be used besides local Python code.  Large datasets may require Databricks.  
# You can also use ChatGPT or similar language model for this step. 

import pandas as pd

players_df = pd.read_csv("players.csv")
league_df = pd.read_csv("league.csv")
roster_df = pd.read_csv("roster.csv")

passing_df = pd.read_csv("passing.csv")
rushing_df = pd.read_csv("rushing.csv")
receiving_df = pd.read_csv("receiving.csv")

display(league_df)
display(roster_df)
display(passing_df)
display(rushing_df)
display(receiving_df)