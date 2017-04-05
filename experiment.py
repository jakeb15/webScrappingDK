__author__ = 'Jake'
from WebScrap import experimentLink
from Data2Csv import getNewPlayers
import time
import winsound
import time
#json file = https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=25811&DraftGroupId=10875&Limit=500&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=25811&DraftGroupId=10875&Limit=500&Offset=106"

ExpLvl = 4
# items in json file -
group_1 = "11383"
group_1a = "11513"
group_one = "https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_1+ "&DraftGroupId=" + group_1a + "&Limit=500&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_1 + "&DraftGroupId=" + group_1a + "&Limit=500&Offset=106"
group_2 = "11389"
group_2a = "11513"
group_two = "https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_2+ "&DraftGroupId=" + group_2a + "&Limit=500&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_2 + "&DraftGroupId=" + group_2a + "&Limit=500&Offset=106"
group_3 = "272770"
group_3a = "11513"
group_three =  "https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_3+ "&DraftGroupId=" + group_3a + "&Limit=500&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=" + group_3 + "&DraftGroupId=" + group_3a + "&Limit=500&Offset=106"
count = 0
last_list = []
player_list = []
last_list2 =[]
last_list3 = []

timeout = time.time() + 60*60   # 5 minutes from now
Stop = False

while(Stop == False):
    f = open('DKFishFinder.txt', 'a')
    player_list = experimentLink(group_one)
    if(count == 0):
        print("1$_H2H fetched")
        for item in player_list:
            if(item.HepLevel < ExpLvl):
                print(item.UserName + " " + "ExLevel: " + str(item.HepLevel) + " Games: " + str(item.games))
        time.sleep(2)
        print("-----------------------------------")
    p_list5 = experimentLink(group_two)
    if(count == 0):
        print("2$_H2H fetched")
        for item in p_list5:
            if(item.HepLevel < ExpLvl):
                print(item.UserName + " " + "ExLevel: " + str(item.HepLevel) + " Games: " + str(item.games))
        print("-----------------------------------")
    p_list20 = experimentLink(group_three)
    if(count == 0):
        print("3$_H2H fetched")
        for item in p_list20:
            if(item.HepLevel < ExpLvl):
                print(item.UserName + " " + "ExLevel: " + str(item.HepLevel) + " Games: " + str(item.games))
        print("-----------------------------------")
    count += 1
    if(count == 1):
        print("generating new list...")
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
                f.write(item + '3' +'\n')
        last_list3 = p_list20
        print("------------------------------")
        print("1$")
        if(len(newPlayerList)>0):
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            for item in newPlayerList:
                print(item)
                f.write(item + '1' + '\n')
        last_list = player_list
        print("------------------------------")
        print("2$")
        if(len(new_p_list5)>0):
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            for item in new_p_list5:
                print(item)
                f.write(item + '2' + '\n')
        last_list2 = p_list5
    else:
        print("no one new found")
    f.close()
    if(time.time()>timeout):
        Stop = True
        print("Timmer has Hit...Program Stopped")
    time.sleep(15)
