__author__ = 'Jake'
from WebScrap import parseH2H
import time
from Data2Csv import list_to_CSV
from Data2Csv import removeDuplicats
from Data2Csv import getNewPlayers
#
# need to open draftkings in chrome and open the network tab in the dev tool. Once you click on the link that opens the popup the webpage should appear in the Network queue.
#The h2h Websites change every day so for thi sto work we must copy and past the website to parse after re getting it.
#
count = 0
last_list = []
while(True):
    count += 1
    player_list =[]
    #player_list = parseH2H('https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11383&draftGroupId=7918&defaultToDetails=true',1,player_list)
    #print("1$_H2H fetched")
    #time.sleep(5)
    #player_list = parseH2H('https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11389&draftGroupId=7918&defaultToDetails=true',2,player_list)
    #print("2$_H2H fetched")
    #time.sleep(5)
    player_list = parseH2H('https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11395&draftGroupId=7871&defaultToDetails=true',5,player_list)
    print("5$_H2H fetched")
    time.sleep(5)
    #player_list = parseH2H('https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11401&draftGroupId=7923&defaultToDetails=true',10,player_list)
    #print("10$_H2H fetched")
    #time.sleep(5)
    #player_list = parseH2H('https://www.draftkings.com/lobby/headtoheadmodal?contestTemplateId=11407&draftGroupId=7923&defaultToDetails=true',20,player_list)
    #print("20$_H2H fetched")
    #time.sleep(3)
    player_list  = removeDuplicats(player_list)
    list_to_CSV(player_list)
    if(count == 1):
        last_list = player_list
        #for item in player_list:
         #   print(item.name)
    if(count > 1):
        newPlayerList = getNewPlayers(last_list,player_list)
        print("------------------------------")
        for item in newPlayerList:
            print item
        last_list = player_list
    time.sleep(200)


#things to do...
# get difference between two lists - see who recently joined - on keypress run loop to update the h2h lists
# use diference_in_list  = set(list)-set(list)

# create a do not play list

# figure out what python package Tkinter is


#https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=11395&DraftGroupId=7871&Limit=200&Offset=106https://www.draftkings.com/lobby/getheadtoheadopponents?ContestTemplateId=11395&DraftGroupId=7871&Limit=200&Offset=106