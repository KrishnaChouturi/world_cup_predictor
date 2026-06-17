import pandas as pd

df = pd.read_csv("wcData/results.csv")
df['date'] = pd.to_datetime(df['date'])

# Tournaments that reflect real competitive strength
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

print("Filtered shape:", filtered.shape)
print("\nDate range:", filtered['date'].min(), "to", filtered['date'].max())
print("\nMatches per tournament:")
print(filtered['tournament'].value_counts())
print("\nUnique teams:", filtered['home_team'].nunique())