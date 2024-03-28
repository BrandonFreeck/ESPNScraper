from pandas import *
from numpy import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from teams import *
# from teams_test import *

# Off with his (gecko) head
Options = Options()
Options.add_argument("--headless")
driver = webdriver.Firefox(options=Options)

path = '/Users/freeck/Dropbox/Programming/Repos/ESPNScraper/Data/'
averages = []
todayscoringPeriodId = 8
teamCount = 0

# stat = ''  # To be removed in lieu of "statSplit"
# stat = '&scoringscoringPeriodId=9&statSplit=singleScoringPeriod'

# See google doc for up to date TODO
# # TODO: Fix headless geckodriver
# # TODO: Add flag for current/total etc (instead of the cancerous commenting/uncommenting currently happening)
# # TODO: Add scoringPeriodId to Date conversion for visualization purposes
# # TODO: Send files into folder structure (turn this into a database later lmao)
# # (Year Folder) > (Team Folder) > .csv for each scoringPeriodId (converted to from scoringPeriodId to date)
# # TODO: Make example teams template file
# # TODO: Automatically infer todayscoringPeriodId via current date

# This is our loop, iterates teams and outputs urls
for url in teams:  # These variable names are horrible

    print(url)  # Prints team name
    # print(teams[url])  # Prints team url for testing

    while scoringPeriodId < todayscoringPeriodId:
        driver.get(  # Commented out to get Projected Totals post draft
            # + '&statSplit=singleScoringPeriod&scoringscoringPeriodId=' + str(scoringPeriodId)
            teams[url]
        )
        time.sleep(4)  # Can we make this better?
        # print(scoringPeriodId) # Print for testing

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
        # Pitching Results (Separate so we can quickly remove P from batters below) (Fucking Ohtani)
        result2 = concat([df3, df4, df5], axis=1).droplevel(0, axis=1)

        # Removing Rows that would cause errant totals/etc
        result1 = result1[result1.SLOT != 'P']  # Removing P from Batters
        result1 = result1[result1.SLOT != 'IL']  # Removing IL from Batters
        result2 = result2[result2.SLOT != 'IL']  # Removing IL from Pitchers

        # Removing Bench & Totals Col for Daily Stats

        # Removing Bench from Batters
        # result1 = result1[result1.SLOT != 'Bench']

        # Removing Totals from Batters
        # result1 = result1[result1.opp != 'TOTALS']

        # Removing Bench from Pitchers
        # result2 = result2[result2.SLOT != 'Bench']

        # Removing Totals from Pitchers
        # result2 = result2[result2.opp != 'TOTALS']

        final_result = concat([result1, result2]).fillna(0)

        # print('Final Result')
        # print(final_result)
        # print(final_result.shape)

        if scoringPeriodId == 1:
            average = (
                url, final_result['tot'].sum(), result1['tot'].sum(), result2['tot'].sum())
            averages.append(average)
        else:
            averages[teamCount][1] += final_result['tot'].sum()
            averages[teamCount][2] += result1['tot'].sum()
            averages[teamCount][3] += result2['tot'].sum()

        # if scoringPeriodId == 1:
        #     average = [
        #         url, final_result['FPTS'].sum(), result1['FPTS'].sum(), result2['FPTS'].sum()]
        #     averages.append(average)
        # else:
        #     averages[teamCount][1] += final_result['FPTS'].sum()
        #     averages[teamCount][2] += result1['FPTS'].sum()
        #     averages[teamCount][3] += result2['FPTS'].sum()

        scoringPeriodId += 1
        print(averages)

        if scoringPeriodId == todayscoringPeriodId:
            teamCount += 1
            print('Team Count Is: ' + str(teamCount))
            break

    print(averages)

    scoringPeriodId = 1

    # final_result.to_csv(path + url + '.csv',  index=False)

driver.close()

averages.sort(key=lambda a: a[1], reverse=True)

# A timeless data display approach

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
