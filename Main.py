import pandas as pd

import camelot

#Extract tables from websites

haneyBoxingRecord = pd.read_html("https://en.wikipedia.org/wiki/Devin_Haney")

simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes")

#Read csv file from website
df_epl21 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E0.csv")

#Rename columns
df_epl21.rename(columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)

#Read table from pdf

tables = camelot.read_pdf('foo.pdf', pages='1')

print(tables)

#Write to a csv file
tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')