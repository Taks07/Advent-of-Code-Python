import functools
import itertools
import sys

dice = 1

class Player():
    def __init__(self, pos):
        self.position = pos - 1
        self.score = 0

    def Move(self, roll):
        self.position += roll

        self.position = self.position%10

        self.score += self.position + 1

class Dice():
    def __init__(self):
        self.num = 1
        self.rolls = 0

    def Roll(self):
        self.rolls += 3

        for i in range(3):
            yield self.num
            self.num += 1

            if self.num > 100:
                self.num = 1

def Part1():
    d = Dice()

    players = [Player(10), Player(1)]
    currplayer = 0

    temp = {0:1,1:0}

    while players[0].score < 1000 and players[1].score < 1000:
        players[currplayer].Move(sum([i for i in d.Roll()])) #move currentplayer
        currplayer = temp[currplayer] #change turn

    print("Answer:", players[currplayer].score * d.rolls)


possrolls = [i for i in itertools.product([1,2,3], [1,2,3], [1,2,3])] #create all 27 possibilities

@functools.cache
def NewRound(players, currplayernum, rollnum): #players is list/tuple of players. each player has format [position, score].
    wins = [0, 0]

    players = [list(p) for p in players] #convert to list so can change values

    currplayer = players[currplayernum]

    currplayer[0] = (currplayer[0] + rollnum) % 10 #make sure position wraps around

    currplayer[1] += currplayer[0] + 1 #position is 0 indexed, so add 1

    if currplayer[1] < 21: #not yet finished
        changeplayer = {0: 1, 1: 0}

        for roll in possrolls:
            for i, w in enumerate(NewRound(tuple([tuple(p) for p in players]), changeplayer[currplayernum], sum(roll))):
                wins[i] += w
    else:
        wins[currplayernum] += 1
        return wins

    return wins

def Part2():
    wins = [0,0]

    for roll in possrolls:
        for i, w in enumerate(NewRound(((9,0),(0,0)), 0, sum(roll))): #pass players as tuple so can be hashed when caching. make sure positioned is decremented as 0-indexed
            wins[i] += w

    print("Answer:", max(wins))

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
