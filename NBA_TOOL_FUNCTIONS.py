__author__ = 'Jake'
import csv
import NBA_SMALL_FUNCTIONS
import numpy

import rotoGuruCSV
import re

# Salary difference between Draftkings and Fanduel
def Salary_Diff(dayx):
    day = dayx

    myDKFile = r'C:\progData\DKvsFD\DK_' + str(day) + '.csv'
    myFDFile = r'C:\progData\DKvsFD\FD_' + str(day) + '.csv'


    DK = []
    FD = []
    Diff = []

    with open(myDKFile, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            DK.append(item)
    f.close()

    with open(myFDFile, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            FD.append(item)
    f.close()

    for item in FD:
        item["Name"] = item['First Name'] + " " + item['Last Name']

    for item in FD:
        for guy in DK:
            if(item["Name"]==guy["Name"]):
                temp = {"Name" : item["Name"]}
                temp["Salary_Diff"] = int(item["Salary"]) - int(guy["Salary"])
                temp["FD_ratio"] = 60000 / float(item["Salary"])
                temp["DK_ratio"] = 50000 / float(item["Salary"])
                Diff.append(temp)

    for item in Diff:
        #FD - DK ~ FD has usually higher Prices
        print(item["Name"] + " " +  str(item["Salary_Diff"]) + " " + str(item["FD_ratio"]) +  " " + str(item["DK_ratio"]))

    with open(r'C:\progData\DKvsFD\salary.csv','wb') as csvfile:
        fieldnames = ['Name','Salary_Diff','FD_ratio','DK_ratio']
        a = csv.DictWriter(csvfile,fieldnames=fieldnames)
        a.writeheader()
        for item in Diff:
            a.writerow(item)
    csvfile.close()

#fixes a file to be a csv file that is taken from the website [http://rotoguru1.com/cgi-bin/hyday.pl?game=dk&scsv=1]
def FixCSV(file):
    f = open(file, 'r')
    header = '"Date","GID","Pos","Name","Starter","DK Pts","DK Salary","Team","H/A","Oppt","Team Score","Oppt Score","Minutes","Stat line"'
    print(header)
    lineNumb = 0
    line_list = [] # list of lines to be written to file
    for line in f:
        temp_line = ""
        if lineNumb == 0:
            #skips header
            lineNumb+= 1
        else:
            lineNumb+= 1
            items = line.split(';')
            count = 0
            for x in items:
                if count == 3:
                    name = x.split(',')
                    print(name)
                    new_name = name[1] + ' ' + name[0]
                    temp_line += '"' + new_name + '"' + ','
                    count+=1
                elif count < 13:
                    temp_line = temp_line + '"' + x + '"' + ','
                    count +=1
                else:
                    temp_line += '"' + x + '"'
            print(temp_line)
            line_list.append(temp_line)
            temp_line = ""
    f.close()
    f = open(file, 'w')
    f.write(header + "\n")
    for x in line_list:
        f.write(x + "\n")

#Uses the NBA schedule to find Back 2 back games and 3 games in 4 days to measure what teams are fatigued
def back2back(threedaysago,b4yesterday,yesterday,today,tomorrow):
    file = r'C:\progData\DKvsFD\schedule.csv'
    games = []
    playingToday = []
    threedaysagolist = []
    playedb4yesterday = []
    playedYesterday = []
    playTomorrow = []
    B2B = []
    threeGamesinfourdays = []

    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            games.append(item)
    f.close()

    for item in games:
        if item["Date"] == threedaysago:
            threedaysagolist.append(item['Visitor/Neutral'])
            threedaysagolist.append(item['Home/Neutral'])
    for item in games:
        if item["Date"] == b4yesterday:
            playedb4yesterday.append(item['Visitor/Neutral'])
            playedb4yesterday.append(item['Home/Neutral'])

    for item in games:
        if item["Date"] == yesterday:
            playedYesterday.append(item['Visitor/Neutral'])
            playedYesterday.append(item['Home/Neutral'])

    for item in games:
        if item["Date"] == today:
            playingToday.append(item['Visitor/Neutral'])
            playingToday.append(item['Home/Neutral'])

    for item in games:
        if item["Date"] == tomorrow:
            playTomorrow.append(item['Visitor/Neutral'])
            playTomorrow.append(item['Home/Neutral'])

    for y in playedYesterday:
        for x in playingToday:
            if y == x:
                B2B.append(x)

    for y in playingToday:
        for x in playTomorrow:
            if y==x:
                B2B.append(x)

    for y in B2B:
        for x in playedb4yesterday:
            if y == x:
                threeGamesinfourdays.append(x)

    for y in B2B:
        for x in threedaysagolist:
            if y == x:
                threeGamesinfourdays.append(x)

    # print("yesterday")
    # for item in playedYesterday:
    #     print item
    # print("today")
    # for item in playingToday:
    #     print item
    # print("tomorrow")
    # for item in playTomorrow:
    #     print item
    #print("Back 2 Back")
    #for item in B2B:
    #    print(item)

    #print("3 Games in 4 Days")
    #for item in threeGamesinfourdays:
    #    print item

    return (B2B,threeGamesinfourdays)

#Takes numerous Draftkings Salarys csv's ranged from DK_1 to DK_32(some number) and puts them into one large csv with player salary and day
def SalaryChange(day):
    DK_CSVs = []
    completelist = []
    for x in range(0,day,1):
        myDKFile = r'C:\progData\DKvsFD\DK_' + str(day - x) + '.csv'
        with open(myDKFile, 'r') as f:
            DK = []
            reader = csv.DictReader(f)
            print(myDKFile)
            for item in reader:
                item["Date"] = day - x
                DK.append(item)
        f.close()
        DK_CSVs.append(DK)
    count = 8
    allplayers = []
    for item in DK_CSVs:
        count-=1
        for x in range(0,len(item)):
            #print('Day '+ str(count) + ': ' + item[x]["Name"] + ' ' +  item[x]["Salary"]+ " " + str(item[x]['Date']))
            allplayers.append(item[x])

    for item in allplayers:
        print (item["Name"])

    with open(r'C:\progData\DKvsFD\Day2DaySalaryChange.csv','w') as csvfile:
        fieldnames = ['Name','Salary','GameInfo','AvgPointsPerGame','teamAbbrev','Date','Position']
        a = csv.DictWriter(csvfile,fieldnames=fieldnames)
        a.writeheader()
        for item in allplayers:
            a.writerow(item)
    csvfile.close()

# Takes the file created from SalaryChange and averages the players and subtracts current price from average price
# Goal is create a file makes Value appear more easy to see
def SalaryChange2(day):
    myDKFile = r'C:\progData\DKvsFD\Day2DaySalaryChange.csv'
    with open(myDKFile, 'r') as f:
        DK = []
        Master = []
        reader = csv.DictReader(f)
        for item in reader:
            DK.append(item)
        f.close()
        copy_DK = DK

        for item in DK:
            if(item['Date']==day):
                count = 0
                item['Salary_AVG'] = 0
                item['Salary_Diff'] = 0
                for x in copy_DK:
                    if(item['Name'] == x['Name'] and item['Date']):
                        item['Salary_AVG'] += int(x['Salary'])
                        count+=1
                        copy_DK.remove(x)
                print (item['Name'] + ' ' + str(item['Salary_AVG']/count) + " " + str((item['Salary_AVG']/count)-int(item['Salary'])) + " " + str(count))
                item['Salary_AVG'] = item['Salary_AVG']/count
                item['Salary_Diff'] = item['Salary_AVG'] - int(item['Salary'])
                Master.append(item)

    with open(r'C:\progData\DKvsFD\SalaryChange_DK_Daily.csv','w') as csvfile:
        fieldnames = ['Name','Salary','Salary_AVG','Salary_Diff','GameInfo','AvgPointsPerGame','teamAbbrev','Date','Position']
        a = csv.DictWriter(csvfile,fieldnames=fieldnames)
        a.writeheader()
        for item in Master:
            a.writerow(item)
    csvfile.close()


def Who_Is_Playing(day):
    players = []
    temp = []
    Games = []
    return_games = []

    myDKFile = r'C:\progData\DKvsFD\DK_' + str(day) + '.csv'
    with open(myDKFile, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            players.append(item)
    f.close()
    for item in players:
        if(item['GameInfo'] not in Games):
            temp.append(item['GameInfo'])

    temp = list(set(temp)) # removes duplicates ... a set cannot have duplicates

    for item in temp:
        Match = {}
        teams = item.split()
        time = teams[1] # takes 2nd token of split and puts it in time
        temp = teams[0].split('@')
        home = temp[0]
        away = temp[1]
        Match['Home'] = NBA_SMALL_FUNCTIONS.nba_Def_to_Team(home)
        Match['Away'] = NBA_SMALL_FUNCTIONS.nba_Def_to_Team(away)
        Match['Time'] = time
        #print home + " " +  away + " " + time
        return_games.append(Match)
    return return_games
    #Home // Away // Time

#Function to show team stats and what teams are weak against what ie defensive rebounds/ offensive rebounds/ turnovers steals ect..
#http://basketball.realgm.com/nba/team_stats/2017/Advanced_Stats/Team_Totals/Regular_Season/team_pace/desc
def Basketball_Team_Analysis(whos_Playing,day,b2b):
    teams=[]
    vsOpponents = team_vs_opp() # team is in format Chicago Bulls
    B2B, ThreeInFour = b2b
    Starters,Bench = last_Starters(day)
    Vs = whos_Playing
    print("finding team stats....and advantages")
    file = r'C:\progData\DKvsFD\NBA_Advance_Stats.csv'
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            teams.append(item)
    f.close()


    #Range of data
    TurnOver_percent = []
    Steal_percent = []
    Block_percent = []
    OffensiveREB_percent =[]
    DeffensiveREB_precent = []
    TotREB_percent = []
    EFG_percent = []
    AST_percent = []
    FIC40 = [] # A formula to encompass all aspects of the box score into a single statistic
    Pace = []

    #Fill arrays
    for item in teams:
        TurnOver_percent.append(float(item['TOV%']))
        Steal_percent.append(float(item['STL%']))
        Block_percent.append(float(item['BLK%']))
        OffensiveREB_percent.append(float(item['ORB%']))
        DeffensiveREB_precent.append(float(item['DRB%']))
        TotREB_percent.append(float(item['TRB%']))
        EFG_percent.append(float(item['eFG%']))
        AST_percent.append(float(item['AST%']))
        FIC40.append(float(item['FIC40']))
        Pace.append(float(item['Pace']))
    #turn list into numpy arrays
    TurnOver_percent = numpy.array(TurnOver_percent)
    Steal_percent = numpy.array(Steal_percent)
    Block_percent = numpy.array(Block_percent)
    OffensiveREB_percent = numpy.array(OffensiveREB_percent)
    DeffensiveREB_precent = numpy.array(DeffensiveREB_precent)
    TotREB_percent = numpy.array(TotREB_percent)
    EFG_percent = numpy.array(EFG_percent)
    AST_percent = numpy.array(AST_percent)
    FIC40 = numpy.array(FIC40)
    Pace = numpy.array(Pace)

    #Item contains Home/Away/Time headers
    #http://basketball.realgm.com/nba/team_stats/2017/Advanced_Stats/Team_Totals/Regular_Season/team_pace/desc
    for item in Vs:
        EFG_H,EFG_A,Pace_H,Pace_A,TurnOver_H,TurnOver_A,Steal_H, Steal_A,  RebD_H, RebD_A, RebO_A, RebO_H,TRB_H,TRB_A,eDiff_H,eDiff_A = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        HOME = ''
        AWAY = ''

        print(item['Home'] +' @ ' + item['Away'])

        # x contains Team	TS%	eFG%	Total S%	ORB%	DRB%	TRB%	AST%	TOV%	STL%	BLK%	PPS	FIC40	ORtg	DRtg	eDiff	Poss	Pace
        for x in teams:
            if(x['Team']== item['Home']):
                HOME = x["Team"]
                Pace_H = float(x['Pace'])
                TurnOver_H = float(x['TOV%'])
                Steal_H = float(x['STL%'])
                RebD_H = float(x['DRB%'])
                RebO_H = float(x['ORB%'])
                TRB_H = float(x['TRB%'])
                eDiff_H = float(x['eDiff'])
                EFG_H = float(x['eFG%'])
            if(x['Team'] == item['Away']):
                AWAY = x["Team"]
                Pace_A = float(x['Pace'])
                TurnOver_A = float(x['TOV%'])
                Steal_A = float(x['STL%'])
                RebD_A = float(x['DRB%'])
                RebO_A = float(x['ORB%'])
                TRB_A =  float(x['TRB%'])
                eDiff_A = float(x['eDiff'])
                EFG_A = float(x['eFG%'])
        print("Game Pace: " + str((Pace_A + Pace_H) / 2) + '               ' + 'League: ' +'['+ str(numpy.min(Pace)) + '-' + str(numpy.max(Pace))+']')
        print("Blowout Factor: "+HOME + " eDiff: " + str(eDiff_H) + " vs " + AWAY + " eDiff " + str(eDiff_A))
        print("peripherals : ")
        for item in vsOpponents:
            if (NBA_SMALL_FUNCTIONS.FullName2City(item['TEAM']) == HOME):
                print('------------------' + HOME + '-------------------------')
                print('[Blocks] ' + HOME +  " Opponents Average " + item['BLK']  )
                print('[Steals] ' + HOME +  " Opponents Average " + item['STL']  )
                print('[FGM]/[FGA] ' + HOME +  " Opponents Average " + item['FGM'] + '/' + item['FGA']  )
            if (NBA_SMALL_FUNCTIONS.FullName2City(item['TEAM']) == AWAY):
                print('------------------' + AWAY + '-------------------------')
                print('[Blocks] ' + AWAY +  " Opponents Average " + item['BLK']  )
                print('[Steals] ' + AWAY +  " Opponents Average " + item['STL']  )
                print('[FGM]/[FGA] ' + AWAY +  " Opponents Average " + item['FGM'] + '/' + item['FGA']  )
        print('-------------------------------------------')
        print(HOME + " TotRebounds: " + str(TRB_H) + "% vs " + AWAY + " TotRebounds " + str(TRB_A)+'%' + '    ' + 'League_TotReb: ['+ str(numpy.min(TotREB_percent)) + '-' + str(numpy.max(TotREB_percent))+']' )
        print(HOME + " Turnovers: " + str(TurnOver_H) + " vs " + AWAY + " Turnovers% " + str(TurnOver_A) + '     ' + 'TurnOver%:['+ str(numpy.min(TurnOver_percent)) + '-' + str(numpy.max(TurnOver_percent))+'] ')
        print(AWAY +" Steal%: " + str(Steal_A) + " vs " + HOME +" Steal% " + str(Steal_H) + '      '  + '      ' + 'Steal%:['+ str(numpy.min(Steal_percent)) + '-' + str(numpy.max(Steal_percent))+'] ')
        print(HOME + " DREB: " + str(RebD_H) + " vs " + AWAY + " OREB: " + str(RebO_A) + '      ' + 'OREB:['+ str(numpy.min(OffensiveREB_percent)) + '-' + str(numpy.max(OffensiveREB_percent))+'] ')
        print(AWAY + " DREB: " + str(RebD_A) + " vs " + HOME + " OREB: " + str(RebO_H) + '      ' + 'DREB:['+ str(numpy.min(DeffensiveREB_precent)) + '-' + str(numpy.max(DeffensiveREB_precent))+'] ')
        print(HOME + ' eFG% ' + str(EFG_H) + " vs " + AWAY + ' eFG%' + str(EFG_A) + '     ' + 'League(EFG): [' + str(numpy.min(EFG_percent)) + '-' + str(numpy.max(EFG_percent))+'] ')
        print('-------------------------------------------------------------------------------------')
        print ("B2B: ",)
        for item in B2B:
            if (NBA_SMALL_FUNCTIONS.FullName2City(item) == HOME):
                print (HOME,)
            if (NBA_SMALL_FUNCTIONS.FullName2City(item) == AWAY):
                print (AWAY,)
        print (" 3in4: ",)
        for item in ThreeInFour:
            if (NBA_SMALL_FUNCTIONS.FullName2City(item) == HOME):
                print (HOME,)
            if (NBA_SMALL_FUNCTIONS.FullName2City(item) == AWAY):
                print (AWAY)

        print("")

        for item in Starters:
            if (item['Team'] == NBA_SMALL_FUNCTIONS.CityName_to_ABREV(HOME).lower()):
                print(item['DK Salary'] + ' ' + item['Name'] + ' min: ' + item['Minutes'] + ' DKPTS: ' + item['DK Pts'])
        for item in Bench:
            if(item['Team'] == NBA_SMALL_FUNCTIONS.CityName_to_ABREV(HOME).lower() and float(item['Minutes']) > 25):
                print('       ' +item['DK Salary'] + ' '  + item['Name'] + ' min: ' + item['Minutes'] + ' DKPTS: ' + item['DK Pts'])

        print("")
        print("")
        for item in Starters:
            if (item['Team'] == NBA_SMALL_FUNCTIONS.CityName_to_ABREV(AWAY).lower()):
                print(item['DK Salary'] + ' ' +item['Name'] + ' min: ' + item['Minutes'] + ' DKPTS: ' + item['DK Pts'])
        for item in Bench:
            if(item['Team'] == NBA_SMALL_FUNCTIONS.CityName_to_ABREV(AWAY).lower() and float(item['Minutes']) > 25):
                print('       ' + item['DK Salary'] + ' ' + item['Name'] + ' min: ' + item['Minutes'] + ' DKPTS: ' + item['DK Pts'])
        print("")
        print("")
        print("")
        print('-------------------------------------------------------------------------------------')


#takes a team and a stat and returns a Player whos doing well in that stat from that team that is in top 100 players who play mpg
#Player	Team	TS%	eFG%	Total S %	ORB%	DRB%	TRB%	AST%	TOV%	STL%	BLK%	USG%	PPR	PPS	ORtg	DRtg	eDiff	FIC	PER (TEAM is IN 3 LETTER ABREV ALL CAP Ex NYK SAS CHI TOR IND ORL
def Basketball_Player_Analysis(team,stat,day):
    players = []
    DK_players = []
    file = r'C:\progData\DKvsFD\NBA_PLAYER_STATS_PER.csv'
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            players.append(item)
    f.close()
    myDKFile = r'C:\progData\DKvsFD\DK_' + str(day ) + '.csv'
    with open(myDKFile, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            DK_players.append(item)
    f.close()

    for item in DK_players:
        print (item)

    for item in players:
        item['Salary'] = '0'
        for x in DK_players:
            if(item['Player']== x['Name']):
                item['Salary'] = x['Salary']


    for item in players:
        if(item['Salary']!= '0'):
            print(item['Player'] + ' ' + item['Salary'] + ' per/Salary: ' + str(float(item['Salary'])/float(item['PER'])))


#Searches last 5 days and gets last 5 starters and returns that and minutes and dkpts
# takes in last file
def last_Starters(day):
    x = 0
    team = []
    Starters = []
    Bench = []
    while(x<5):

        myDKFile = r'C:\progData\DKvsFD\DK_PTS_' + str(int(day)-x) + '.csv'
        players  = []

        with open(myDKFile, 'r') as f:
            reader = csv.DictReader(f)
            for item in reader:
                players.append(item)
        f.close()

        for item in players:
            if(item['Starter']== '1' and item['Team'] not in team):
                #print item['Name'] + " " + item['Team'] + ' ' + item['Minutes'] + ' ' + item['DK Pts'] + ' ' + item['DK Salary']
                Starters.append(item)
            elif(item['Starter'] != '1' and item['Team'] not in team):
                if(item['Minutes'] == 'DNP' or item['Minutes'] == 'NA'):
                    item['Minutes'] = '0'
                Bench.append(item)
        for item in players:
            if(item['Starter']== '1'):
                team.append(item['Team'])
        x+=1

    return (Starters,Bench)

#this function returns a csv file of how teams perform aganist this team. example Phoenix's opponents have an average of 6 blocks a game
# all data is drawn from a http://stats.nba.com/teams/opponent/#!?sort=OPP_PTS&dir=1
def team_vs_opp():
    Opponents = []
    file = r'C:\progData\DKvsFD\NBA_vs_Opp.csv'
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            Opponents.append(item)
    f.close()
    return  Opponents