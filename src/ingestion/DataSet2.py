# DataSet2.py - script to extract data from its source and load into ADLS.

print("Pro-Football-Reference ingestion")

import pandas as pd

url_pass = 'https://www.pro-football-reference.com/years/2023/passing.htm'
passing_df = pd.read_html(url_pass)[0]

url_rush = 'https://www.pro-football-reference.com/years/2023/rushing.htm'
rushing_df = pd.read_html(url_rush)[0]
rushing_df.columns = [c[1] for c in rushing_df.columns]

url_receive = 'https://www.pro-football-reference.com/years/2023/receiving.htm'
receiving_df = pd.read_html(url_receive)[0]

url_def = 'https://www.pro-football-reference.com/years/2023/opp.htm'
defense_df = pd.read_html(url_def)[0]

defense_df.columns = [c[0] + " - " + c[1] for c in defense_df.columns]

passing_df.to_csv("passing.csv")
rushing_df.to_csv("rushing.csv")
receiving_df.to_csv("receiving.csv")
defense_df.to_csv("defense.csv")