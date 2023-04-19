import copy, queue

with open("Input.txt", 'r') as file:
    thecave = []

    for line in file:
        thecave.append([int(i) for i in line[:-1]])

def GetNeighbours(node, cave):
    delta = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbours = []

    for drow,dcol in delta:
        neighcoords = (drow + node[1][0], dcol + node[1][1])

        if -1 < neighcoords[0] < len(cave) and -1 < neighcoords[1] < len(cave[0]):
            neighbours.append((node[0] + cave[neighcoords[0]][neighcoords[1]], neighcoords))

    return neighbours


def SearchDjik(cave):
    openlist = queue.PriorityQueue() #queue.PriorityQueue is much faster for remaining sorted than normal list
    closedict = dict() #use dict to store and access (g val/total risk). coord:risk

    openlist.put((0, (0, 0)))  # (g, coords)

    target = (len(cave) - 1, len(cave[0]) - 1)
    while not openlist.empty():
        currnode = openlist.get()

        closedict[currnode[1]] = currnode[0]

        if currnode[1] == target:
            return closedict[target]

        for neighbour in GetNeighbours(currnode, cave):
            if neighbour[1] not in closedict:
                if neighbour[1] in [coord[1] for coord in openlist.queue]:
                    for node in openlist.queue:
                        if node[1] == neighbour[1]:
                            if node[0] > neighbour[0]:
                                openlist.queue.remove(node)
                                openlist.put(neighbour)
                        break

                else:
                    openlist.put(neighbour)

if __name__ == "__main__":
    print("Part 1")
    print("Answer:", SearchDjik(copy.deepcopy(thecave)))

    print("\nPart 2")
    tempcave = []
    for row in range(5 * len(thecave)):
        temprow = []

        for col in range(5 * len(thecave[0])):
            looprow = row // len(thecave)
            loopcol = col // len(thecave[0])

            val = thecave[row % len(thecave)][col % len(thecave[0])] + looprow + loopcol

            if val > 9:
                val -= 9

            temprow.append(val)
        tempcave.append(temprow)

    print("Answer:", SearchDjik(copy.deepcopy(tempcave)))




