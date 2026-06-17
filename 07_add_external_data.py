import pandas as pd

# Fifa Rankings
# Source: https://www.fifa.com/fifa-world-ranking
fifa = {
    'Argentina': 1, 'Spain': 2, 'France': 3, 'England': 4,
    'Portugal': 5, 'Brazil': 6, 'Morocco': 7, 'Netherlands': 8,
    'Belgium': 9, 'Germany': 10, 'Croatia': 11, 'Italy': 12,
    'Colombia': 13, 'Mexico': 14, 'Senegal': 15, 'Uruguay': 16,
    'United States': 17, 'Japan': 18, 'Switzerland': 19, 'Iran': 20,
    'Denmark': 21, 'Turkey': 22, 'Ecuador': 23, 'Peru': 24,
    'South Korea': 25, 'Nigeria': 26, 'Australia': 27, 'Algeria': 28,
    'Chile': 29, 'Canada': 30, 'Serbia': 31, 'Ukraine': 32,
    'Ivory Coast': 33, 'Qatar': 34, 'Scotland': 35, 'Poland': 36,
    'Russia': 37, 'Greece': 38, 'Hungary': 39, 'South Africa': 40,
    'Tunisia': 41, 'Paraguay': 42, 'Venezuela': 43, 'Bolivia': 44,
    'Ghana': 45, 'Egypt': 46, 'Saudi Arabia': 47, 'Costa Rica': 48,
    'Norway': 49, 'Sweden': 50, 'Austria': 51, 'Czech Republic': 52,
    'Romania': 53, 'Slovakia': 54, 'Wales': 55, 'Northern Ireland': 56,
    'Republic of Ireland': 57, 'Panama': 58, 'Jamaica': 59, 'Honduras': 60,
    'Cameroon': 61, 'Mali': 62, 'Burkina Faso': 63, 'Guinea': 64,
}

# Club Elo ratings (approximate)
# Source: https://www.eloratings.net
elo = {
    'Spain': 2129, 'Argentina': 2115, 'France': 2063, 'England': 2024,
    'Portugal': 1989, 'Colombia': 1982, 'Brazil': 1978, 'Netherlands': 1944,
    'Germany': 1939, 'Uruguay': 1910, 'Croatia': 1890, 'Italy': 1885,
    'Belgium': 1870, 'Morocco': 1865, 'Denmark': 1845, 'Switzerland': 1840,
    'United States': 1835, 'Senegal': 1830, 'Japan': 1825, 'Ecuador': 1815,
    'Mexico': 1810, 'Iran': 1795, 'Turkey': 1790, 'South Korea': 1780,
    'Ukraine': 1765, 'Australia': 1760, 'Nigeria': 1755, 'Poland': 1745,
    'Canada': 1740, 'Ivory Coast': 1735, 'Algeria': 1720, 'Hungary': 1705,
    'Peru': 1700, 'Chile': 1695, 'Serbia': 1690, 'Scotland': 1685,
    'Austria': 1680, 'Norway': 1675, 'Sweden': 1670, 'Czech Republic': 1665,
    'Tunisia': 1660, 'Ghana': 1655, 'Egypt': 1650, 'Saudi Arabia': 1645,
    'Costa Rica': 1640, 'Paraguay': 1635, 'Venezuela': 1630, 'Romania': 1625,
    'Slovakia': 1620, 'Greece': 1615, 'Qatar': 1610, 'Panama': 1605,
    'Bolivia': 1600, 'Cameroon': 1595, 'Mali': 1590, 'Burkina Faso': 1585,
    'Guinea': 1580, 'Jamaica': 1575, 'Honduras': 1570, 'South Africa': 1565,
    'Wales': 1560, 'Northern Ireland': 1555, 'Republic of Ireland': 1550,
}

# Betting odds to win World Cup 2026 (implied probability)
# Source: oddschecker.com
odds_prob = {
    'Argentina': 0.20, 'France': 0.16, 'Spain': 0.14, 'England': 0.12,
    'Brazil': 0.10, 'Germany': 0.07, 'Portugal': 0.06, 'Netherlands': 0.04,
    'Colombia': 0.03, 'Uruguay': 0.02, 'Belgium': 0.015, 'Croatia': 0.012,
    'Italy': 0.010, 'Morocco': 0.009, 'United States': 0.008, 'Denmark': 0.005,
    'Mexico': 0.004, 'Japan': 0.004, 'Senegal': 0.003, 'Switzerland': 0.003,
    'Ecuador': 0.002, 'Turkey': 0.002, 'South Korea': 0.002, 'Canada': 0.002,
    'Iran': 0.001, 'Australia': 0.001, 'Ukraine': 0.001, 'Nigeria': 0.001,
    'Poland': 0.001, 'Ivory Coast': 0.001, 'Algeria': 0.0005, 'Hungary': 0.0005,
    'Peru': 0.0005, 'Chile': 0.0005, 'Serbia': 0.0005, 'Scotland': 0.0003,
    'Austria': 0.0003, 'Norway': 0.0003, 'Sweden': 0.0003, 'Czech Republic': 0.0002,
    'Tunisia': 0.0002, 'Ghana': 0.0002, 'Egypt': 0.0002, 'Saudi Arabia': 0.0002,
    'Costa Rica': 0.0001, 'Paraguay': 0.0001, 'Venezuela': 0.0001, 'Romania': 0.0001,
    'Qatar': 0.0001, 'Greece': 0.0001, 'Panama': 0.0001, 'Bolivia': 0.0001,
    'Cameroon': 0.0001, 'Mali': 0.0001, 'Burkina Faso': 0.0001, 'Guinea': 0.0001,
    'Jamaica': 0.0001, 'Honduras': 0.0001, 'South Africa': 0.0001,
    'Wales': 0.0001, 'Northern Ireland': 0.0001, 'Republic of Ireland': 0.0001,
}


fifa_df = pd.DataFrame(list(fifa.items()), columns=['team', 'fifa_rank'])
elo_df = pd.DataFrame(list(elo.items()), columns=['team', 'elo'])
odds_df = pd.DataFrame(list(odds_prob.items()), columns=['team', 'wc_prob'])

external = fifa_df.merge(elo_df, on='team').merge(odds_df, on='team')
external['fifa_score'] = 1 / external['fifa_rank']

print("External data shape:", external.shape)
print("\nExternal data:")
print(external.to_string(index=False))

external.to_csv("wcData/external_data.csv", index=False)
print("\nSaved to wcData/external_data.csv")