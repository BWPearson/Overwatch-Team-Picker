import itertools
import sys
class Player:
    def __init__(self, name, role, sr):
        self.name = name
        self.sr = sr
        self.role = role

    def Name(self):
        return self.name

    def SR(self):
        return self.sr

    def Role(self):
        return self.role

    def ChangeSR(self, sr):
        self.sr = sr
        return

    def GetInfo(self):
        return self.name, self.role, self.sr

    def ChangeRole(self, role):
        self.role = role

class Controller:
    def __init__(self):
        self.Team1 = []
        self.Team2 = []
        self.PlayerPool = []

    def AddPlayer(self, name, role, sr, team):
        player = Player(name, role, sr)
        if team == "1":
            self.Team1.append(player)
        else:
            self.Team2.append(player)

    def RemovePlayer(self, index, team):
        if team == 1:
            self.Team1.pop(index)
        else:
            self.Team2.append(index)

    def ShowTeams(self, team1 = None, team2 = None):
        if (not team1 and not team2):
            team1 = self.Team1
            team2 = self.Team2
        print "Team 1\n"
        avg = 0
        playerCount = 0
        for player in team1:
            name, role, sr = player.GetInfo()
            avg += int(sr)
            playerCount += 1
            print "{0} {1} {2}\n".format(name, role, sr)
        avg = avg/playerCount
        print "Average SR: " + str(avg)+"\n\n"
        print "Team 2\n"
        avg = 0
        playerCount = 0
        for player in team2:
            name, role, sr = player.GetInfo()
            avg += int(sr)
            playerCount += 1
            print "{0} {1} {2}\n".format(name, role, sr)
        avg = avg / playerCount
        print "Average SR: " + str(avg)+"\n\n"


    def SwapPlayers(self, player1Index, player2Index):
        player1 = self.Team1.pop(player1Index)
        player2 = self.Team2.pop(player2Index)
        self.Team1.append(player2)
        self.Team2.append(player1)

    def GetCombos(self, diff):
        orig_stdout = sys.stdout
        open('teams.txt', 'w').close()
        f = open('teams.txt', 'a+')
        sys.stdout = f
        self.playerPool = []
        for player in self.Team1:
            self.playerPool.append(player)
        for player in self.Team2:
            self.playerPool.append(player)
        teams = list(itertools.combinations(self.playerPool, 6))
        for combination in teams:
            team1 = list(combination)
            team2 = [player for player in self.playerPool if player not in team1]
            average1 = 0
            average2 = 0
            playerCount = 0
            for player in team1:
                name, role, sr = player.GetInfo()
                average1 += int(sr)
                playerCount += 1
            average1 = average1/playerCount
            playerCount = 0
            for player in team2:
                name, role, sr = player.GetInfo()
                average2 += int(sr)
                playerCount += 1
            average2 = average2 / playerCount
            if abs(average1 - average2) <= diff:
                self.ShowTeams(team1, team2)
        sys.stdout = orig_stdout
        f.close()
        print("Teams saved to teams.txt")

controller = Controller()
ans=True
while ans:
    print ("""
    1.Add a player
    2.Delete a player
    3.Show Teams
    4.Swap Players
    5.Return Possible Teams
    6.Import Teams
    7.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ")
    if ans=="1":
        player=raw_input("\nEnter the following separated by spaces: Name role sr team\n")
        name, role, sr, team = player.split()
        controller.AddPlayer(name, role, sr, team)
        print("\n Player Added")
    elif ans=="2":
        player = raw_input("\nEnter the following separated by spaces: Name role sr team\n")
        name, role, sr, team = player.split()
        controller.AddPlayer(name, role, sr, team)
        print("\n Player Removed")
    elif ans=="3":
        controller.ShowTeams()
    elif ans=="4":
        indexes = raw_input("Enter a player index from Team 1 and a player index from Team 2 to swap them: ")
        index1, index2 = indexes.split()
        controller.SwapPlayers(int(index1), int(index2))
        print("\n Swapped Players")
    elif ans == "5":
        difference = raw_input("Enter an SR difference to search for possible teams: ")
        controller.GetCombos(int(difference))
        print "Generated possible teams\n"
    elif ans=="6":
        fileName = raw_input("Enter a fileName to open: ")
        f = open(fileName,"r")
        for line in f:
            name, role, sr, team = line.split()
            controller.AddPlayer(name, role, sr, team)
            print "Importing player {0} {1} {2}\n".format(name, role, sr)
        f.close()
        print "\nImported Teams"
    elif ans == "7":
        ans = False
        print("\n Goodbye")
    elif ans !="":
        print("\n Not Valid Choice Try again")
