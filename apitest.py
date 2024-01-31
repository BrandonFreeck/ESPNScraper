from espn_api.baseball import League

league = League(league_id=85215692, year=2022)

teams = league.teams

print(teams[0].score)

# for team in teams:
#     print(team.team_name + " W:" + str(team.wins) + " L:" + str(team.losses))
#     print(team.scores)
