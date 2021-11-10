import pandas as pd

url_3 = 'https://www.basketball-reference.com/leagues/NBA_2022.html#per_game-team'
df_3 = pd.read_html(url_3, header = 0)

team_stats = df_3[4]

#def team_stat(team):
 #   team1 = team.strip().title()
 #   stats = team_stats[team_stats['Team'].str.contains(f'{team1}')]
 #   return stats

def compare_team_stat(team_1,team_2):
  team1 = team_1.strip().title()
  team2 = team_2.strip().title()
  stats = team_stats[team_stats['Team'].str.contains(f'{team1}|{team2}')]
  return (stats.T).iloc[1:]
