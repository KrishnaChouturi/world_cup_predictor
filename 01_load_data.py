import pandas as pd

# Load
df = pd.read_csv("wcData/results.csv")

# Raw data
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 3 rows:")
print(df.head(3))
print("\nTournament types:")
print(df['tournament'].value_counts().head(20))