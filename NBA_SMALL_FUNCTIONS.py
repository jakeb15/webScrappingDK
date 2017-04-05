__author__ = 'Jake'

# takes teh abrevation and turns it into the city name example Orl to Orlando
def nba_Def_to_Team(abrev):
    if(abrev == 'LAC'):
        return 'L.A. Clippers'
    elif(abrev == 'OKC'):
        return 'Oklahoma City'
    elif(abrev == 'Cle'):
        return 'Cleveland'
    elif(abrev == 'Was'):
        return 'Washington'
    elif(abrev == 'Sac'):
        return 'Sacramento'
    elif(abrev == 'Por'):
        return 'Portland'
    elif(abrev == 'Den'):
        return 'Denver'
    elif(abrev == 'SA'):
        return 'San Antonio'
    elif(abrev == 'Tor'):
        return 'Toronto'
    elif(abrev == 'Cha'):
        return 'Charlotte'
    elif(abrev == 'Ind'):
        return 'Indiana'
    elif(abrev == 'Phi'):
        return 'Philadelphia'
    elif(abrev == 'NY'):
        return 'New York'
    elif(abrev == 'Bos'):
        return 'Boston'
    elif(abrev == 'Uta'):
        return 'Utah'
    elif(abrev == 'Orl'):
        return 'Orlando'
    elif(abrev == 'NO'):
        return 'New Orleans'
    elif(abrev == 'Hou'):
        return 'Houston'
    elif(abrev == 'Mia'):
        return 'Miami'
    elif(abrev == 'Det'):
        return 'Detroit'
    elif(abrev == 'Dal'):
        return 'Dallas'
    elif(abrev == 'Mem'):
        return 'Memphis'
    elif(abrev == 'Bkn'):
        return 'Brooklyn'
    elif(abrev == 'Chi'):
        return 'Chicago'
    elif(abrev == 'Por'):
        return 'Portland'
    elif(abrev == 'Atl'):
        return 'Atlanta'
    elif(abrev == 'Min'):
        return 'Minnesota'
    elif(abrev == 'Min'):
        return 'Minnesota'
    elif(abrev == 'LAL'):
        return 'L.A. Lakers'
    elif(abrev == 'Sac'):
        return 'Sacramento'
    elif(abrev == 'GS'):
        return 'Golden State'
    elif(abrev == 'Mil'):
        return 'Milwaukee'
    elif(abrev == 'Pho'):
        return 'Phoenix'




def CityName_to_ABREV(CityName):
    if(CityName == 'L.A. Clippers'):
        return 'LAC'
    elif(CityName == 'Oklahoma City'):
        return 'OKC'
    elif(CityName == 'Cleveland'):
        return 'CLE'
    elif(CityName == 'Washington'):
        return 'WAS'
    elif(CityName == 'Sacramento'):
        return 'SAC'
    elif(CityName == 'Portland'):
        return 'POR'
    elif(CityName == 'Denver'):
        return 'DEN'
    elif(CityName == 'San Antonio'):
        return 'SAS'
    elif(CityName == 'Toronto'):
        return 'TOR'
    elif(CityName == 'Charlotte'):
        return 'CHA'
    elif(CityName == 'Indiana'):
        return 'IND'
    elif(CityName == 'Philadelphia'):
        return 'PHI'
    elif(CityName == 'New York'):
        return 'NYK'
    elif(CityName == 'Boston'):
        return 'BOS'
    elif(CityName == 'Utah'):
        return 'UTA'
    elif(CityName == 'Orlando'):
        return 'ORL'
    elif(CityName == 'New Orleans'):
        return 'NOR'
    elif(CityName == 'Houston'):
        return 'HOU'
    elif(CityName == 'Miami'):
        return 'MIA'
    elif(CityName == 'Detroit'):
        return 'DET'
    elif(CityName == 'Dallas'):
        return 'DAL'
    elif(CityName == 'Memphis'):
        return 'MEM'
    elif(CityName == 'Brooklyn'):
        return 'BKN'
    elif(CityName == 'Chicago'):
        return 'CHI'
    elif(CityName == 'Portland'):
        return 'POR'
    elif(CityName == 'Atlanta'):
        return 'ATL'
    elif(CityName == 'Minnesota'):
        return 'MIN'
    elif(CityName == 'L.A. Lakers'):
        return 'LAL'
    elif(CityName == 'Brooklyn'):
        return 'BKN'
    elif(CityName == 'Golden State'):
        return 'GSW'
    elif(CityName == 'Milwaukee'):
        return 'MIL'
    elif(CityName == 'Phoenix'):
        return 'PHO'

def FullName2City(CityName):
    if(CityName == 'Los Angeles Clippers'):
        return 'L.A Clippers'
    elif(CityName == 'Oklahoma City Thunder'):
        return 'Oklahoma City'
    elif(CityName == 'Cleveland Cavaliers'):
        return 'Cleveland'
    elif(CityName == 'Washington Wizards'):
        return 'Washington'
    elif(CityName == 'Sacramento Kings'):
        return 'Sacramento'
    elif(CityName == 'Portland Trail Blazers'):
        return 'Portland'
    elif(CityName == 'Denver Nuggets'):
        return 'Denver'
    elif(CityName == 'San Antonio Spurs'):
        return 'San Antonio'
    elif(CityName == 'Toronto Raptors'):
        return 'Toronto'
    elif(CityName == 'Charlotte Hornets'):
        return 'Charlotte'
    elif(CityName == 'Indiana Pacers'):
        return 'Indiana'
    elif(CityName == 'Philadelphia 76ers'):
        return 'Philadelphia'
    elif(CityName == 'New York Knicks'):
        return 'New York'
    elif(CityName == 'Boston Celtics'):
        return 'Boston'
    elif(CityName == 'Utah Jazz'):
        return 'Utah'
    elif(CityName == 'Orlando Magic'):
        return 'Orlando'
    elif(CityName == 'New Orleans Pelicans'):
        return 'New Orleans'
    elif(CityName == 'Houston Rockets'):
        return 'Houston'
    elif(CityName == 'Miami Heat'):
        return 'Miami'
    elif(CityName == 'Detroit Pistons'):
        return 'Detroit'
    elif(CityName == 'Dallas Mavericks'):
        return 'Dallas'
    elif(CityName == 'Memphis Grizzlies'):
        return 'Memphis'
    elif(CityName == 'Brooklyn Nets'):
        return 'Brooklyn'
    elif(CityName == 'Chicago Bulls'):
        return 'Chicago'
    elif(CityName == 'Atlanta Hawks'):
        return 'Atlanta'
    elif(CityName == 'Minnesota Timberwolves'):
        return 'Minnesota'
    elif(CityName == 'Los Angeles Lakers'):
        return 'L.A. Lakers'
    elif(CityName == 'Golden State Warriors'):
        return 'Golden State'
    elif(CityName == 'Milwaukee Bucks'):
        return 'Milwaukee'
    elif(CityName == 'Phoenix Suns'):
        return 'Phoenix'