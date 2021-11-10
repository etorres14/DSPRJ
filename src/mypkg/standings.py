
import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2022.html#per_game-team'
df = pd.read_html(url, header = 0)

east_standings = df[0]
west_standings = df[1]

def west():
    return west_standings

def east():
    return east_standings
