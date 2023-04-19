#DOESNT WORK. DO PROPER IMPLEMENTATION OF DJIKSTRA, EACH BOARD STATE IS NODE

import copy
import itertools
from queue import PriorityQueue
from collections import defaultdict
from math import inf

state = []
costs = {"A" : 1, "B" : 10, "C" : 100, "D" : 1000}


with open("Input.txt", 'r') as file:
    for line in file:
        state.append(list(line[:-1]))

def GetPossStates(state):
    delta = [d for d in itertools.product([-1,0,1], [-1,0,1]) if d != (0,0)]

    for i, row in enumerate(state):
        for j, colval in enumerate(row):
            if colval in ("A", "B", "C", "D"):
                for drow,dcol in delta:
                    neighcoords = (drow + i, dcol + j)

                    if state[neighcoords[0]][neighcoords[1]] == ".":
                        if neighcoords in ((3,1), (5,1), (7,1), (9,1)):
                            continue

                        newstate = copy.deepcopy(state)
                        newstate[neighcoords[0]][neighcoords[1]] = colval
                        newstate[i][j] = "."

                        cost = (abs(drow) + abs(dcol)) * costs[colval]

                        yield newstate, cost


def Stringify(state):
    return "".join(["".join(i) for i in state])

target = "##############...........####A#B#C#D###  #A#B#C#D#  #########"


def SearchDjik(state):
    openlist = PriorityQueue() #queue.PriorityQueue is much faster for remaining sorted than normal list
    closedict = set()

    openlist.put((state,0))
    cost = defaultdict(lambda:inf)

    cost[Stringify(state)] = 0

    while not openlist.empty():
        currstate,_ = openlist.get()

        closedict.add(Stringify(currstate))

        for newstate,newcost in GetPossStates(currstate):
            if newcost < cost[Stringify(newstate)]:
                cost[Stringify(newstate)] = newcost

            if Stringify(newstate) not in closedict:
                openlist.put((newstate, (cost[Stringify(newstate)])))

    print(cost[target])

ans = SearchDjik(state)



