file = open("Input.txt", "r")
inputarr = []

line = file.readline()[:-1]

while len(line) != 0:
    directions = []
    skipi = []
    for i in range(len(line)):
        if i not in skipi:
            if line[i:i+2] in ("se", "sw", "nw", "ne"):
                directions.append(line[i:i+2])
                skipi.append(i+1)

            else:
                directions.append(line[i])

    inputarr.append(directions)
    line = file.readline()[:-1]

#Part 1
blacktiles = []

def Part1():
    for instructions in inputarr:
        coordinates = [0, 0, 0] #[x,y,z]
        for direction in instructions:
            if direction == "e":
                coordinates[0] += 1
                coordinates[1] -= 1

            elif direction == "w":
                coordinates[0] -= 1
                coordinates[1] += 1

            elif direction == "se":
                coordinates[2] += 1
                coordinates[1] -= 1

            elif direction == "nw":
                coordinates[2] -= 1
                coordinates[1] += 1

            elif direction == "sw":
                coordinates[0] -= 1
                coordinates[2] += 1

            else:
                coordinates[0] += 1
                coordinates[2] -= 1

        if coordinates in blacktiles:
            blacktiles.remove(coordinates)

        else:
            blacktiles.append(coordinates)

    print("Answer:", len(blacktiles))

#Part 2
allrange = [0,0]

def SetUpRange():
    global allrange
    for coords in blacktiles:
        if coords[0] < allrange[0]:
            allrange[0] = coords[0] - 1

        if coords[1] < allrange[0]:
            allrange[0] = coords[1] - 1

        if coords[2] < allrange[0]:
            allrange[0] = coords[2] - 1

        if coords[0] > allrange[1]:
            allrange[1] = coords[1] + 1

        if coords[1] > allrange[1]:
            allrange[1] = coords[2] + 1

        if coords[2] > allrange[1]:
            allrange[1] = coords[2] + 1

def CheckNeighbours(tilecoord, blacktilearr):
    neighbours = [[1,-1,0],[-1,1,0],[1,0,-1],[-1,0,1],[0,1,-1],[0,-1,1]]
    black = 0

    for delta in neighbours:
        if [tilecoord[0] + delta[0], tilecoord[1] + delta[1], tilecoord[2] + delta[2]] in blacktilearr:
            black += 1

    return black
                
    
    
def FlipTiles():
    global allrange
    blacktilecopy = [x for x in blacktiles]

    for x in range(allrange[0], allrange[1]+1):
        for y in range(allrange[0], allrange[1]+1):
            for z in range(allrange[0], allrange[1]+1):
                if (x + y + z) == 0:
                    black = CheckNeighbours([x,y,z], blacktilecopy)

                    if (black == 0 or black > 2) and [x,y,z] in blacktiles:
                        blacktiles.remove([x,y,z])

                    if black == 2 and [x,y,z] not in blacktiles:
                        blacktiles.append([x,y,z])
                        

    allrange[0], allrange[1] = allrange[0]-1, allrange[1]+1

                        

    
def Part2():
    SetUpRange()
    for _ in range(100):
        FlipTiles()

    print("Answer:", len(blacktiles))
        

    
if __name__ == "__main__":
    print("Part 1")
    Part1()


    print("\nPart 2")
    Part2()


        
