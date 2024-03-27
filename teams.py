# Your league's Id
leagueId = ''

# Year of the season you're interested in
seasonId = ''

# Integer for the current day's scoring period
scoringPeriodId = ''

# 'currSeason' or 'singleScoringPeriod' or 'projections'
# singleScoringPeriod is for the day's matchup
statSplit = 'projections'

# Best to hardcode your teamIds, no reason not to, they're unique and iterating isn't necessary
teams = {
    'Bleacherberg Cup Snakes': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=1' + stat,
    'Honolulu Blue Macs': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=9' + stat,
    'NoCAP Bussin FR FR': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=11' + stat,
    'Edgeville Moundhoppers': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=13' + stat,
    'Hyperion Acorns' + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=10' + stat,
    'Humboldt Homies' + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=12' + stat,
    "Cheek Busters" + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=14' + stat,
    'Armor Trimmers' + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=15' + stat,
    'Wallstreet Wildcards': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=16' + stat,
    'South Bay Beach Babes': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=6' + stat,
    'Penacony Dream Catchers': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=17' + stat,
    'Matt\'s Monstrous Team': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2024&teamId=18' + stat}
