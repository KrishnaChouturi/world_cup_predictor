import pandas as pd

metrics = pd.read_csv("wcData/metrics.csv")
sos = pd.read_csv("wcData/sos.csv")

combined = metrics.merge(sos, on='team')

print("Combined shape:", combined.shape)
print("\nColumns:", combined.columns.tolist())
print("\nSample (top 15 by PPG):")
print(
    combined.sort_values('ppg', ascending=False)
    [['team', 'games', 'ppg', 'gd_per_game', 'recent_form', 'sos']]
    .head(15)
    .to_string(index=False)
)

combined.to_csv("wcData/combined_metrics.csv", index=False)
print("\nSaved to wcData/combined_metrics.csv")