#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11383&draftGroupId=7866&defaultToDetails=true #1$
#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11389&draftGroupId=7866&defaultToDetails=true #2$
#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11395&draftGroupId=7866&defaultToDetails=true #5$
#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11401&draftGroupId=7866&defaultToDetails=true #10$
#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11407&draftGroupId=7866&defaultToDetails=true #20$
#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11413&draftGroupId=7866&defaultToDetails=true #50$
#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11419&draftGroupId=7866&defaultToDetails=true #100$
#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11425&draftGroupId=7866&defaultToDetails=true #200$
#https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11431&draftGroupId=7866&defaultToDetails=true #500$

from bs4 import BeautifulSoup
from bs4 import SoupStrainer #import to parse only part of a document, in this case the <div class_="opponents-list shadows-light level2"> tag
import urllib2
import os
from Player import Player
import json


def parseH2H(url,dollar,plist):
    text = urllib2.urlopen(url).read()
    parse_This = SoupStrainer(class_="opponents-list shadows-light level2")
    soup = BeautifulSoup(text,"html.parser",parse_only=parse_This)
    str = soup.get_text()
    text = os.linesep.join([s for s in str.splitlines() if s])

    stopwords = ["play"]
    text_split = text.split()

    result = [word for word in text_split if word.lower() not in stopwords]
    result = ' '.join(result)

    players = result.split()
    player_list = plist

    for player in players:
        if(player[0] != 'x' ):
            ## somewhere in here we can do a check the list to see if player = playerlist.name
            temp = inList(player,player_list)
            if(temp  > 0):
                person = player_list[temp]
            else:
                person = Player("")
                person.setName(player)
            if(dollar == 1):
                person.h2h_1 = True
            elif(dollar == 2):
                person.h2h_2 = True
            elif(dollar == 5):
                person.h2h_5 = True
            elif(dollar == 10):
                person.h2h_10 = True
            elif(dollar == 20):
                person.h2h_20 = True
            elif(dollar == 50):
                person.h2h_50 = True
            elif(dollar == 100):
                person.h2h_100 = True
            elif(dollar == 200):
                person.h2h_200 = True
            elif(dollar == 500):
                person.h2h_500 = True
            else:
                print("error on h2h dollar amount")
        elif(player[0] == 'x' and player[1].isdigit()):
            str = player[1:]
            person.addGames(int(str))
            player_list.append(person)
        else:
            print("error")

    #for item in player_list:
        #print(item.name, item.games, item.h2h_1, item.h2h_2, item.h2h_5 , item.h2h_10, item.h2h_20)

    return player_list

def inList(str,list):
    inFlag = False
    count = 0
    for item in list:
        if(inFlag == False):
            count +=1
        if(str == item.name):
            inFlag = True

    if(inFlag == True):
        return count
    else:
        return -3

#new function not sure how the html works but it returns a json string with all the players, parse the json file getting more than the allowed limit of 100 players
#that my last function was getting, can set the limit right no its 200 players. the URL will need to be updated every day
def experimentLink(url):
    text = urllib2.urlopen(url).read()
    #json.loads <- s is for string which is waht I have. if I was loading from a straight json file it would be .load
    j = json.loads(text)
    player_List = []
    for x in j["Opponents"]:
        player = Player(x["UserName"])
        player.setUserName(x["UserName"])
        player.setContestId(x["ContestId"])
        player.setNumberofContests(x["NumberOfContests"])
        player.setUserId(x["UserId"])
        player.setHepLevel(x["HepLevel"])
        player_List.append(player)

    return player_List