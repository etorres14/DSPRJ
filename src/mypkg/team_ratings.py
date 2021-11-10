import pandas as pd

from player import compare_player

url_2 = 'https://www.basketball-reference.com/leagues/NBA_2022_ratings.html'
df_2 = pd.read_html(url_2, header = 1)

df_2 = df_2[0]
df_2


def rating(team):
    team_1 = team.strip().title()
    team_rating = df_2[df_2['Team'].str.contains(f'{team_1}')]
    return team_rating.T.iloc[0:]


def compare_rating(team_1, team_2):
    team_1 = team_1.strip().title()
    team_2 = team_2.strip().title()
    team_rating = df_2[df_2['Team'].str.contains(f'{team_1}|{team_2}')]
    return team_rating.T.iloc[0:]


rating("lakers")