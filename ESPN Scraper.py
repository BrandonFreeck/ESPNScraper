from pandas import *
from numpy import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

Options = Options()
Options.headless = True

driver = webdriver.Firefox(options=Options)
path = '/Users/freeck/Dropbox/Programming/Repos/ESPN Scraper/Data/'
averages = []
todayPeriodId = 2
periodId = 1
teamCount = 0

stat = ''
# stat = '&scoringPeriodId=9&statSplit=singleScoringPeriod'

# TODO: Add flag for current/total etc (instead of the cancerous commenting/uncommenting currently happening)
# TODO: Add year variable & test all of below on 2022 Season
# TODO: Add dates for visualization purposes
# TODO: Add PeriodId to Date conversion for visualization purposes
# TODO: Unify data into single excel file for visualization/data storage purposes

teams = {
    'Bleacherberg Cup Snakes': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=1' + stat,
    'Honolulu Blue Macs': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=9' + stat,
    'NoCAP Bussin FR FR': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=11' + stat,
    'Booers SmallDongBrauns': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=13' + stat,
    'Raintown Puddleduckies': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=6' + stat,
    'Grand Lake Ospreys': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=10' + stat,
    'God Dangit Bobbehs': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=12' + stat,
    "Kanye's Sleepy Tweets": 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=14' + stat,
    'Armor Trimmers' + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=15' + stat,
    'Weeaboo Bombers' + '\t': 'https://fantasy.espn.com/baseball/team?leagueId=85215692&seasonId=2023&teamId=16' + stat}

# This is our loop, iterates teams and outputs urls
for url in teams:  # These variable names are horrible

    print(url)  # Prints team name
    # print(teams[url])  # Prints team url

    while periodId < todayPeriodId:
        driver.get(  # Commented out to get Projected Totals post draft
            # + '&statSplit=singleScoringPeriod&scoringPeriodId=' + str(periodId)
            teams[url]
        )
        time.sleep(4)
        # print(periodId)

        table = driver.find_elements(by=By.TAG_NAME, value='table')

        # Preparing dfs for concatenation
        # Probably a better way to do this, loop maybe?
        df0 = read_html(table[0].get_attribute('outerHTML'))[
            0].replace('--', 0)
        df1 = read_html(table[1].get_attribute('outerHTML'))[
            0].replace('--', 0)
        df2 = read_html(table[2].get_attribute('outerHTML'))[
            0].replace('--', 0)
        df3 = read_html(table[3].get_attribute('outerHTML'))[
            0].replace('--', 0)
        df4 = read_html(table[4].get_attribute('outerHTML'))[
            0].replace('--', 0)
        df5 = read_html(table[5].get_attribute('outerHTML'))[
            0].replace('--', 0)

        # Cleaning Up Types - Removing errant "Object" Types
        df1 = df1.apply(to_numeric)
        df2 = df2.apply(to_numeric)
        df4 = df4.apply(to_numeric)
        df5 = df5.apply(to_numeric)

        # Batting Results
        result1 = concat([df0, df1, df2], axis=1).droplevel(0, axis=1)
        # Pitching Results (Separate so we can quickly remove P from batters below)
        result2 = concat([df3, df4, df5], axis=1).droplevel(0, axis=1)

        # Removing Rows that would cause errant totals/etc
        result1 = result1[result1.SLOT != 'P']  # Removing P from Batters
        # result1 = result1[result1.SLOT != 'IL']  # Removing IL from Batters
        # result2 = result2[result2.SLOT != 'IL']  # Removing IL from Pitchers

        # Removing Bench & Totals Col for Daily Stats

        # Removing Bench from Batters
        # result1 = result1[result1.SLOT != 'Bench']

        # Removing Totals from Batters
        result1 = result1[result1.opp != 'TOTALS']

        # Removing Bench from Pitchers
        # result2 = result2[result2.SLOT != 'Bench']

        # Removing Totals from Pitchers
        result2 = result2[result2.opp != 'TOTALS']

        final_result = concat([result1, result2]).fillna(0)

        # print('Final Result')
        # print(final_result)
        # print(final_result.shape)

        if periodId == 1:
            average = (
                url, final_result['tot'].sum(), result1['tot'].sum(), result2['tot'].sum())
            averages.append(average)
        else:
            averages[teamCount][1] += final_result['tot'].sum()
            averages[teamCount][2] += result1['tot'].sum()
            averages[teamCount][3] += result2['tot'].sum()

        # if periodId == 1:
        #     average = [
        #         url, final_result['FPTS'].sum(), result1['FPTS'].sum(), result2['FPTS'].sum()]
        #     averages.append(average)
        # else:
        #     averages[teamCount][1] += final_result['FPTS'].sum()
        #     averages[teamCount][2] += result1['FPTS'].sum()
        #     averages[teamCount][3] += result2['FPTS'].sum()

        periodId += 1
        print(averages)

        if periodId == todayPeriodId:
            teamCount += 1
            print('Team Count Is: ' + str(teamCount))
            break

    print(averages)

    periodId = 1

    # final_result.to_csv(path + url + '.csv',  index=False)

driver.close()

averages.sort(key=lambda a: a[1], reverse=True)

print('\n')
print('----------------Ordered By Total---------------')
print('Name                   Total   Batting Pitching')
for average in averages:
    print(average[0] + '\t' + str(average[1]) +
          '\t' + str(average[2]) + '\t' + str(average[3]))

averages.sort(key=lambda a: a[2], reverse=True)

print('\n')
print('---------------Ordered By Batting--------------')
print('Name                   Total   Batting Pitching')
for average in averages:
    print(average[0] + '\t' + str(average[1]) +
          '\t' + str(average[2]) + '\t' + str(average[3]))

averages.sort(key=lambda a: a[3], reverse=True)

print('\n')
print('--------------Ordered By Pitching--------------')
print('Name                   Total   Batting Pitching')
for average in averages:
    print(average[0] + '\t' + str(average[1]) +
          '\t' + str(average[2]) + '\t' + str(average[3]))
