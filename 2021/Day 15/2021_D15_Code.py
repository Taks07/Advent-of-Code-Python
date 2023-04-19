import copy

with open("Input.txt", 'r') as file:
    cave = []

    for line in file:
        cave.append([int(i) for i in line[:-1]])

openlist = [] #Nodes to be examined
closedlist = [] #Examined nodes

openlist.append([(0,0),0]) #((coords,g,h,f))

def FindNeighbours(node,target):
    delta = [(0,1), (0,-1), (1,0), (-1,0)]
    neighbours = []

    for drow, dcol in delta:
        nextcoords = (drow + node[0][0], dcol + node[0][1])

        if -1 < nextcoords[0] < len(cave) and -1 < nextcoords[1] < len(cave[0]): #check if valid coords for neighbour
            g = node[1] + cave[nextcoords[0]][nextcoords[1]] #calculate distance from start
            NewNode = [nextcoords, g]
            neighbours.append(NewNode)

    #neighbours = sorted(neighbours, key = lambda x: x[1]) #Priority list according to g value
    return neighbours

def FindInList(node, open):
    if open:
        for n in openlist:
            if node[0] == n[0]:
                return openlist.index(n)

    else:
        for n in closedlist:
            if node[0] == n[0]:
                return closedlist.index(n)

    return None

#Shitty implementation of Djikstra search
def Search(target = (len(cave) - 1, len(cave[0]) - 1)):
    global openlist
    while openlist != []: #if openlist becomes empty, search failed
        openlist = sorted(openlist, key = lambda x : x[1]) #sort ascending from g value. use queue.PriorityQueue or heapq - faster
        currsquare = openlist.pop(0) #take highest priority node from open list as current node
        closedlist.append(currsquare) #add current node to closedlist - examined

        if (currsquare[0][0], currsquare[0][1]) == target: #if currentnode is target, end. get (total risk level/distance from start) of target square for answer
            return closedlist

        for neighbour in FindNeighbours(currsquare,target): #examine all neighbours of current square
            if FindInList(neighbour, False) == None: #only consider if neighbour not in closedlist. else, discard neighbour
                index = FindInList(neighbour,True)
                if index == None: #Not in openlist, so add. make sure openlist is still sorted according to g
                    openlist.append(neighbour) #Add neighbour to openlist. Will be in order of priority as sorted in FindNeighbours()

                else: #in openlist
                    if openlist[index][1] > neighbour[1]: #if version in openlist has higher g val that neighbour's, replace with neighbour
                        openlist[index][1] = neighbour[1] #replacing g val. (coords remain same)



    return closedlist

print("Part 1")
#print("Answer:", Search()[-1][1])


#Change cave
tempcave = []
for row in range(5*len(cave)):
    temprow = []

    for col in range(5*len(cave[0])):
        looprow = row//len(cave)
        loopcol = col//len(cave[0])

        val = cave[row%len(cave)][col%len(cave[0])] + looprow + loopcol

        if val > 9:
            val -= 9

        temprow.append(val)
    tempcave.append(temprow)

cave = copy.deepcopy(tempcave)

target = (len(cave) - 1, len(cave[0]) - 1)
print("\nPart 2")
print("Answer:", Search(target)[-1][1])
