import itertools
premier_league_teams: list[str] = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Liverpool",
    "Luton Town",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Sheffield United",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers",
    "Burnley"
]
matches = itertools.permutations(premier_league_teams, 2)
# print(f"Total Matches: {len(list(matches))}") ???
print("Premier League Matches".center(50, "-"))
for match in matches:
    print(f"{match[0]} - {match[1]}")