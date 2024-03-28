# Your league's Id
leagueId = '85215692'

# Year of the season you're interested in
seasonId = '2024'

# Integer for the current day's scoring period
scoringPeriodId = 1

# 'currSeason' or 'singleScoringPeriod' or 'projections'
# singleScoringPeriod is for the day's matchup
statSplit = '&statSplit=' + 'projections'

# Best to hardcode your teamIds, no reason not to, they're unique and iterating isn't necessary. You're hardcoding the names already anyways
# Example item format --
teams = {
    'Bleacherberg Cup Snakes': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=1' + statSplit,
    'Honolulu Blue Macs': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=9' + statSplit,
    'NoCAP Bussin FR FR': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=11' + statSplit,
    'Edgeville Moundhoppers': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=13' + statSplit,
    'Hyperion Acorns' + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=10' + statSplit,
    'Humboldt Homies' + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=12' + statSplit,
    "Cheek Busters" + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=14' + statSplit,
    'Armor Trimmers' + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=15' + statSplit,
    'Wallstreet Wildcards': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=16' + statSplit,
    'South Bay Beach Babes': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=6' + statSplit,
    'Penacony Dream Catchers': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=17' + statSplit,
    'Matt\'s Monstrous Team': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=18' + statSplit
}
