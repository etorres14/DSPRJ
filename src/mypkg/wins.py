import pandas as pd


url_4 = 'https://www.basketball-reference.com/leagues/NBA_2022.html#per_game-team'
df_4 = pd.read_html(url_4, header = 0)

off_team_stats = df_4[4]
def_team_stats = df_4[5]

def projected_wins(team):
  team = team.strip().title()
  two_pp = off_team_stats[off_team_stats['Team'].str.contains(team)]['2P%'].values[0]
  three_pp = off_team_stats[off_team_stats['Team'].str.contains(team)]['3P%'].values[0]
  reb = off_team_stats[off_team_stats['Team'].str.contains(team)]['TRB'].values[0]
  tov = off_team_stats[off_team_stats['Team'].str.contains(team)]['TOV'].values[0]
  otwo_pp = def_team_stats[def_team_stats['Team'].str.contains(team)]['2P%'].values[0]
  othree_pp = def_team_stats[def_team_stats['Team'].str.contains(team)]['3P%'].values[0]
  oreb = def_team_stats[def_team_stats['Team'].str.contains(team)]['TRB'].values[0]
  otov = def_team_stats[def_team_stats['Team'].str.contains(team)]['TOV'].values[0]
  oblk = def_team_stats[def_team_stats['Team'].str.contains(team)]['BLK'].values[0]

  return (47.1054 + 198.0596 * three_pp + 259.33 * two_pp - 3.6428 * tov + 1.4378 * reb - 293.6768 * othree_pp - 121.0769 * otwo_pp + 2.4905 * otov - 2.374 * oreb + 2.8668 * oblk).round()

