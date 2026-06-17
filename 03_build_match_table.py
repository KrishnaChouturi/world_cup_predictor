import pandas as pd

df = pd.read_csv("wcData/results.csv")
df['date'] = pd.to_datetime(df['date'])

COMPETITIVE = [
    'FIFA World Cup',
    'FIFA World Cup qualification',
    'UEFA Euro',
    'UEFA Euro qualification',
    'UEFA Nations League',
    'Copa América',
    'African Cup of Nations',
    'African Cup of Nations qualification',
    'AFC Asian Cup',
    'AFC Asian Cup qualification',
    'Gold Cup',
    'CONCACAF Nations League',
    'CONCACAF Championship',
]

filtered = df[
    (df['date'] >= '2018-01-01') &
    (df['tournament'].isin(COMPETITIVE))
].copy()

# Home
home = filtered[['date', 'home_team', 'away_team', 'home_score', 'away_score', 'tournament', 'neutral']].copy()
home.columns = ['date', 'team', 'opponent', 'goals_for', 'goals_against', 'tournament', 'neutral']
home['home'] = True

# Away
away = filtered[['date', 'away_team', 'home_team', 'away_score', 'home_score', 'tournament', 'neutral']].copy()
away.columns = ['date', 'team', 'opponent', 'goals_for', 'goals_against', 'tournament', 'neutral']
away['home'] = False

matches = pd.concat([home, away], ignore_index=True)
matches = matches.sort_values('date').reset_index(drop=True)

# Results
def get_result(row):
    if row['goals_for'] > row['goals_against']:
        return 'W'
    elif row['goals_for'] < row['goals_against']:
        return 'L'
    else:
        return 'D'

matches['result'] = matches.apply(get_result, axis=1)

def get_points(result):
    return 3 if result == 'W' else (1 if result == 'D' else 0)

matches['points'] = matches['result'].apply(get_points)
matches['goal_diff'] = matches['goals_for'] - matches['goals_against']

print("Master table shape:", matches.shape)
print("\nColumns:", matches.columns.tolist())
print("\nSample rows:")
print(matches[matches['team'] == 'France'].head(10))

matches.to_csv("wcData/matches_master.csv", index=False)
print("\nSaved to wcData/matches_master.csv")