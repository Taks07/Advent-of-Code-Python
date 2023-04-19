import copy, timeit
import re

with open("Input.txt", 'r') as file:
    blocks = []

    for line in file:
        temp = []
        match = re.match(r"(on|off) x=(.+),y=(.+),z=(.+)", line[:-1])


        for i in range(2,5):
            temp.append([int(j) for j in match.group(i).split("..")])

        temp.append(match.group(1))

        blocks.append(temp)

grid = dict()

def Build():
    temp = {"on" : 1, "off" : 0}

    for b in blocks:
        if -51<b[1][0]<51:
            for x in range(b[0][0], b[0][1] + 1):
                for y in range(b[1][0], b[1][1] + 1):
                    for z in range(b[2][0], b[2][1] + 1):
                            grid[(x,y,z)] = temp[b[3]]

def Part1():
    Build()
    print("Answer:", sum(grid.values()))

class Block():
    def __init__(self, xrange, yrange, zrange, state):
        self.state = state
        self.ranges = [xrange,yrange,zrange]

    def Volume(self):
        val = 1

        for range in self.ranges:
            val *= (range[1] - range[0]) + 1

        return val

def Intersection(block1, block2):
    ranges = []

    for i in range(3):
        temprange1 = copy.deepcopy(block1.ranges[i])
        temprange2 = copy.deepcopy(block2.ranges[i])

        #one envelops the other
        if temprange2[0] <= temprange1[0] and temprange1[1] <= temprange2[1]:
            ranges.append([temprange1[0], temprange1[1]])

        elif temprange1[0] <= temprange2[0] and temprange2[1] <= temprange1[1]:
            ranges.append([temprange2[0], temprange2[1]])

        #upper part intersects
        elif temprange1[0] < temprange2[0] and temprange2[0] <= temprange1[1] <= temprange2[1]:
            ranges.append([temprange2[0], temprange1[1]])

        elif temprange2[0] < temprange1[0] and temprange1[0] <= temprange2[1] <= temprange1[1]:
            ranges.append([temprange1[0], temprange2[1]])

        #lower part intersects
        elif temprange2[0] <= temprange1[0] <= temprange2[1] and temprange1[1] > temprange2[1]:
            ranges.append([temprange1[0], temprange2[1]])

        elif temprange1[0] <= temprange2[0] <= temprange1[1] and temprange2[1] > temprange1[1]:
            ranges.append([temprange2[0], temprange1[1]])

        #no intersection
        else:
            return None


    return ranges

def Part2():
    onblocks = set()
    offblocks = set()


    for b in blocks:
        tempon = copy.deepcopy(onblocks)
        tempoff = copy.deepcopy(offblocks)

        currblock = Block(b[0],b[1],b[2],b[3]) #array of all blocks making up current one. If intersect with other on blocks, split

        for alreadyon in tempon:
            intersecting = Intersection(alreadyon,currblock)

            if intersecting:
                offblocks.add(Block(intersecting[0],intersecting[1],intersecting[2], "off"))

        for alreadyoff in tempoff:
            intersecting = Intersection(alreadyoff,currblock)

            if intersecting:
                onblocks.add(Block(intersecting[0],intersecting[1],intersecting[2], "on"))

        if b[3] == "on":
            onblocks.add(currblock)

    totalvol = 0

    for b in onblocks:
        totalvol += b.Volume()

    for b in offblocks:
        totalvol -= b.Volume()

    print("Answer:", totalvol)


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()