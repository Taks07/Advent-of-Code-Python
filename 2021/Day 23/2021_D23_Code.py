import copy

with open("Input.txt", 'r') as file:
    roomsval = []
    roomspos = []

    file.readline()
    hall = file.readline()

    line1 = file.readline().strip("\n").strip(" ").strip("#")
    line2 = file.readline().strip("\n").strip(" ").strip("#")

    for i in range(len(line1)):
        if line1[i] != "#":
            roomspos.append(i + 3)
            roomsval.append([line1[i], line2[i]])

hallsval = ["." for i in range(len(hall.strip("\n").strip("#"))) if i not in roomspos]
hallspos = [i for i in range(len(hall)) if hall[i] not in ("#", "\n") and i not in roomspos]

roomsize = 2

costs = {"A" : 1, "B" : 10, "C" : 100, "D" : 1000}
targetroom = {"A" : 3, "B" : 5, "C" : 7, "D" : 9}

#Use whenever accessing from -vals list using -pos
def GetIndex(pos):
    if pos in roomspos:
        return roomspos.index(pos)

    else:
        return hallspos.index(pos)

def Stringify(roomsval, hallsval):
    return str(roomsval) + str(hallsval)

def MoveToHall(roompos, hallpos, roomsval, hallsval): #Assume valid move - check if empty room, if completed, if blocked outside
    roomsval = copy.deepcopy(roomsval)
    hallsval = copy.deepcopy(hallsval)

    cost = 0

    currroom = roomsval[GetIndex(roompos)]

    cost += (1 + roomsize - len(currroom)) * costs[currroom[0]]

    if hallpos > roompos:
        diff = 1

    else:
        diff = -1

    for i in range(roompos + 1, hallpos + 1, diff):
        cost += costs[currroom[0]]

    hallsval[GetIndex(hallpos)] = currroom.pop(0)

    return roomsval, hallsval, cost

def MoveToRoom(roompos, hallpos, roomsval, hallsval): #Assume valid move - check if empty room, if completed, if blocked outside
    roomsval = copy.deepcopy(roomsval)
    hallsval = copy.deepcopy(hallsval)

    cost = 0

    currroom = roomsval[GetIndex(roompos)]

    cost += (roomsize - len(currroom)) * costs[hallsval[GetIndex(hallpos)]]

    if hallpos > roompos:
        diff = -1

    else:
        diff = 1

    for i in range(hallpos + 1, roompos + 1, diff):
        cost += costs[hallsval[GetIndex(hallpos)]]

    currroom.insert(0, hallsval[GetIndex(hallpos)])
    hallsval[GetIndex(hallpos)] = "."

    return roomsval, hallsval, cost

def PossibleMoves(roomsval, hallsval):
    roomsval = copy.deepcopy(roomsval)
    hallsval = copy.deepcopy(hallsval)

    for hall in hallspos:
        currhall = hallsval[GetIndex(hall)]

        if currhall != ".":  # hallpos not empty
            currroom = roomsval[GetIndex(targetroom[currhall])]

            dontmove = False

            for i in currroom:
                if i != currhall:
                    dontmove = True
                    break

            if dontmove:
                continue

            #implement check to see if route is clear

            yield MoveToRoom(hall, targetroom[currhall], roomsval, hallsval)

roomsval, hallsval, _ = MoveToHall(3,4, roomsval, hallsval)
for i in PossibleMoves(roomsval,hallsval):
    print(i)
