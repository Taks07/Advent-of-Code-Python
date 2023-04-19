with open("Input.txt", 'r') as file:
    heightmap = []

    for line in file:
        heightmap.append(line[:-1])

def GetSurrounding(row,col):
    surrounding = []
    differences = [(1,0), (-1,0), (0,1), (0,-1)]

    for drow, dcol in differences:
        if -1 < drow + row < len(heightmap) and -1 < dcol + col < len(heightmap[0]):
            surrounding.append(heightmap[row + drow][col + dcol])

    return surrounding
lowpoints = []

def Part1():
    threatlevel = 0
    for row in range(len(heightmap)):
        for col in range(len(heightmap[0])):
            currheight = heightmap[row][col]

            for adj in GetSurrounding(row,col):
                if int(adj) <= int(currheight):
                    currheight = -1
                    break

            if currheight != -1:
                threatlevel += int(currheight) + 1
                lowpoints.append((row,col))

    print("Answer:", threatlevel)

def CheckBasin(row,col,basintiles = []):
    if (row,col) not in basintiles:
        basintiles.append((row,col))

        differences = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for drow, dcol in differences:
            if -1 < drow + row < len(heightmap) and -1 < dcol + col < len(heightmap[0]) and heightmap[row + drow][col + dcol] != "9":
                basintiles = CheckBasin(row + drow,col + dcol,basintiles)

    return basintiles

def Part2():
    basins = []
    for row,col in lowpoints:
            if heightmap[row][col] == "9":
                continue

            currbasin = set(CheckBasin(row,col))

            if currbasin not in basins:
                for basin in basins:
                    if basin.issubset(currbasin):
                        currbasin -= basin

                basins.append(currbasin)

    basins = sorted(basins, key = len, reverse=True)

    ans = 1

    for i in range(3):
        ans *= len(basins[i])

    print("Answer:", ans)

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
