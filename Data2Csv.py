__author__ = 'Jake'
import csv

def list_to_CSV(list):
    myfile = open('C:\progData\DKh2h.csv', 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    firstRow = ["Name","Games","In_1$","In_2$","In_5$","In_10$","In_20$","In_50$","In_100$","In_200$","In_500$"]
    wr.writerow(firstRow)
    for item in list:
        newList = [item.name,item.games,item.h2h_1,item.h2h_2,item.h2h_5,item.h2h_10,item.h2h_20,item.h2h_50,item.h2h_100,item.h2h_200,item.h2h_500]
        wr.writerow(newList)


#this throws a list in a set, a set can not have dups then puts the set back into a list
def removeDuplicats(a_list):
    return list(set(a_list))

# returns the difference in the lists
def getNewPlayers(a_list, b_list):
    newPlayers = []
    existFlag = False
    for val in b_list:
        for item in a_list:
            if(val.UserName == item.UserName):
                existFlag = True
        if(existFlag == False):
            #doing the experience check here and sending just a name back
            if(val.HepLevel < 3):
                newPlayers.append(val.UserName)
            #newPlayers.append(val.NumberOfContests)
           #newPlayers.append(val.HepLevel)
        existFlag = False
    return newPlayers