__author__ = 'Jake'

class Player:
    def __init__(self, name):
        self.name = name
        self.h2h_1 = False
        self.h2h_2 = False
        self.h2h_5 = False
        self.h2h_10 = False
        self.h2h_20 = False
        self.h2h_50 = False
        self.h2h_100 = False
        self.h2h_200 = False
        self.h2h_500 = False
        self.games = 0
        self.NumberOfContests =0
        self.UserName = ""
        self.ContestId =0
        self.UserId = 0
        self.HepLevel = 0

    def addGames(self,number):
        self.games = self.games + number

    def setName(self,named):
        self.name = named

    def setUserName(self,x):
        self.UserName = x

    def setContestId(self,x):
        self.ContestId = x

    def setNumberofContests(self,x):
        self.NumberOfContests = x

    def setUserId(self,x):
        self.UserId = x

    def setHepLevel(self,x):
        self.HepLevel = x