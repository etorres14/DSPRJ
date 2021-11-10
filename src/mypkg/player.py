import pandas as pd

url_1 = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'
df2022 = pd.read_html(url_1, header = 0)
df2022 = df2022[0]

def player_stat(player):
  stats = df2022[df2022['Player'].str.contains(f'{player.strip().title()}|{player}')]
  return stats

def compare_player(player_1, player_2):
  player1 = player_1.strip().title()
  player2 = player_2.strip().title()
  s = df2022[df2022['Player'].str.contains(f'{player1}|{player2}|{player_1}|{player_2}')]
  return s.T.iloc[1:]

