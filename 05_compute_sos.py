import pandas as pd

matches = pd.read_csv("wcData/matches_master.csv")
matches['date'] = pd.to_datetime(matches['date'])

# Win Rate
win_rate = matches.groupby('team').apply(
    lambda g: (g['points'].sum()) / (g['points'].count() * 3)
).reset_index()
win_rate.columns = ['team', 'win_rate']

# Avr Opp Win Rate
matches = matches.merge(win_rate, left_on='opponent', right_on='team', suffixes=('', '_opp'))
matches = matches.rename(columns={'win_rate': 'opp_strength'})

sos = matches.groupby('team')['opp_strength'].mean().reset_index()
sos.columns = ['team', 'sos']

print("Top 15 by SOS (hardest schedules):")
print(sos.sort_values('sos', ascending=False).head(15))

print("\nBottom 10 by SOS (easiest schedules):")
print(sos.sort_values('sos').head(10))

sos.to_csv("wcData/sos.csv", index=False)
print("\nSaved to wcData/sos.csv")