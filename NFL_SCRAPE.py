__author__ = 'Jake'
from WebScrap import experimentLink
from Data2Csv import getNewPlayers
import time
import winsound

#json file = https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=25811&DraftGroupId=10875&Limit=500&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=25811&DraftGroupId=10875&Limit=500&Offset=106"


# items in json file -
group_1 = "25811"
group_1a = "10933"
group_one = "https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_1+ "&DraftGroupId=" + group_1a + "&Limit=500&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_1 + "&DraftGroupId=" + group_1a + "&Limit=500&Offset=106"
group_2 = "25812"
group_2a = "10933"
group_two = "https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_2+ "&DraftGroupId=" + group_2a + "&Limit=500&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_2 + "&DraftGroupId=" + group_2a + "&Limit=500&Offset=106"
group_3 = "272773"
group_3a = "10933"
group_three =  "https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_3+ "&DraftGroupId=" + group_3a + "&Limit=500&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_3 + "&DraftGroupId=" + group_3a + "&Limit=500&Offset=106"
count = 0
last_list = []
player_list = []
last_list2 =[]
last_list3 = []
while(True):
    player_list = experimentLink(group_one)
    if(count == 0):
        print("1$_H2H fetched")
        for item in player_list:
            if(item.HepLevel < 5):
                print (item.UserName + " " + "ExLevel: " + str(item.HepLevel) + " Games: " + str(item.games))
        time.sleep(2)
        print("-----------------------------------")
    p_list5 = experimentLink(group_two)
    if(count == 0):
        print("2$_H2H fetched")
        for item in p_list5:
            if(item.HepLevel < 5):
                print (item.UserName + " " + "ExLevel: " + str(item.HepLevel) + " Games: " + str(item.games))
        print("-----------------------------------")
    p_list20 = experimentLink(group_three)
    if(count == 0):
        print("3$_H2H fetched")
        for item in p_list20:
            if(item.HepLevel < 5):
                print (item.UserName + " " + "ExLevel: " + str(item.HepLevel) + " Games: " + str(item.games))
        print("-----------------------------------")
    count += 1
    if(count == 1):
        print ("generating new list...")
        last_list = player_list
        last_list2 = p_list5
        last_list3 = p_list20
        #for item in player_list:
         #   print(item.name)
    if(count > 1):
        newPlayerList = getNewPlayers(last_list,player_list)
        new_p_list5 = getNewPlayers(last_list2,p_list5)
        new_p_list20 = getNewPlayers(last_list3,p_list20)
        print("-------------------------------")
        print("3$")
        if(len(new_p_list20) > 0):
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            for item in newPlayerList:
                print(item)
        last_list3 = p_list20
        print("------------------------------")
        print("1$")
        if(len(newPlayerList)>0):
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            for item in newPlayerList:
                print(item)
        last_list = player_list
        print("------------------------------")
        print("2$")
        if(len(new_p_list5)>0):
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            for item in new_p_list5:
                print(item)
        last_list2 = p_list5
    else:
        print ("no one new found")
    time.sleep(25)