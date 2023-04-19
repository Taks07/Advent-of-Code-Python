import copy
file = open("Input.txt", "r")

ActiveCoords = []

y = 0
for line in file:
    for x in range(len(line)-1):
        if line[x] == "#":
            ActiveCoords.append([x,y,0])
    y += 1

xrange = [-1, len(line)]
yrange = [-1, y]
zrange = [-1,1]
file.close()

#Part 1
def CheckNeighbour(coords, TempActive):
    if coords in TempActive:
        active = True

    else:
        active = False

    numactive = 0
    
    for x in range(coords[0]-1, coords[0]+2):
        for y in range(coords[1]-1, coords[1]+2):
            for z in range(coords[2]-1, coords[2]+2):
                if [x,y,z] != coords:
                    if [x,y,z] in TempActive:
                        numactive += 1
                        
    if active and (numactive not in (2,3)):
        active = False

    elif not active and numactive == 3:
        active = True

    return active

def UpdateCubes():
    global ActiveCoords
    TempActive = copy.deepcopy(ActiveCoords)
    for x in range(xrange[0], xrange[1]+1):
        for y in range(yrange[0], yrange[1]+1):
            for z in range(zrange[0], zrange[1]+1):
                active = CheckNeighbour([x,y,z], TempActive)

                if active and [x,y,z] not in ActiveCoords:
                    ActiveCoords.append([x,y,z])

                elif not active and [x,y,z] in ActiveCoords:
                    ActiveCoords.remove([x,y,z])

    xrange[0], xrange[1] = xrange[0]-1, xrange[1]+1
    yrange[0], yrange[1] = yrange[0]-1, yrange[1]+1
    zrange[0], zrange[1] = zrange[0]-1, zrange[1]+1

def Part1():
    for i in range(6):
        UpdateCubes()

    print("Number Active:", len(ActiveCoords))
    
if __name__ == "__main__":
    print("Part 1")
    Part1()
    
#Part2
file = open("Input.txt", "r")

ActiveCoords2 = []

y = 0
for line in file:
    for x in range(len(line)-1):
        if line[x] == "#":
            ActiveCoords2.append([x,y,0,0])
    y += 1

xrange = [-1, len(line)]
yrange = [-1, y]
zrange = [-1,1]
wrange = [-1,1]

def CheckNeighbour2(coords, TempActive):
    if coords in TempActive:
        active = True

    else:
        active = False

    numactive = 0
    
    for x in range(coords[0]-1, coords[0]+2):
        for y in range(coords[1]-1, coords[1]+2):
            for z in range(coords[2]-1, coords[2]+2):
                for w in range(coords[3]-1, coords[3]+2):
                    if [x,y,z,w] != coords:
                        if [x,y,z,w] in TempActive:
                            numactive += 1
                        
    if active and (numactive not in (2,3)):
        active = False

    elif not active and numactive == 3:
        active = True

    return active

def UpdateCubes2():
    global ActiveCoords2
    TempActive = copy.deepcopy(ActiveCoords2)
    for x in range(xrange[0], xrange[1]+1):
        for y in range(yrange[0], yrange[1]+1):
            for z in range(zrange[0], zrange[1]+1):
                for w in range(wrange[0], wrange[1]+1):
                    active = CheckNeighbour2([x,y,z,w], TempActive)

                    if active and [x,y,z,w] not in ActiveCoords2:
                        ActiveCoords2.append([x,y,z,w])

                    elif not active and [x,y,z,w] in ActiveCoords2:
                        ActiveCoords2.remove([x,y,z,w])

    xrange[0], xrange[1] = xrange[0]-1, xrange[1]+1
    yrange[0], yrange[1] = yrange[0]-1, yrange[1]+1
    zrange[0], zrange[1] = zrange[0]-1, zrange[1]+1
    wrange[0], wrange[1] = wrange[0]-1, wrange[1]+1

def Part2():
    for i in range(6):
        UpdateCubes2()

    print("Number Active:", len(ActiveCoords2))

if __name__ == "__main__":
    print("\nPart 2")
    Part2()


    
        
    
