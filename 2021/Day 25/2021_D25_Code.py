import copy

with open("Input.txt", 'r') as file:
    floor = []
    for line in file:
        floor.append(list(line[:-1]))

def CheckClear(row,col):
    cucumber = floor[row][col]

    if cucumber == ">":
        newcol = col + 1

        if newcol == len(floor[0]):
            newcol = 0


        if floor[row][newcol] == ".":
            return True, newcol

    else:
        newrow = row + 1

        if newrow == len(floor):
            newrow = 0

        if floor[newrow][col] == ".":
            return True, newrow

    return False,None

def Run():
    global floor
    copyfloor = copy.deepcopy(floor)

    for row in range(len(floor)):
        for col in range(len(floor[0])):
            if floor[row][col] == ">":
                if CheckClear(row,col)[0] == True:
                    copyfloor[row][CheckClear(row,col)[1]] = ">"
                    copyfloor[row][col] = "."

    floor = copy.deepcopy(copyfloor)

    for row in range(len(floor)):
        for col in range(len(floor[0])):
            if floor[row][col] == "v":
                if CheckClear(row, col)[0] == True:
                    copyfloor[CheckClear(row, col)[1]][col] = "v"
                    copyfloor[row][col] = "."

    floor = copy.deepcopy(copyfloor)

def Part1():
    count = 0

    while 1:
        count += 1
        prevfloor = copy.deepcopy(floor)

        Run()

        if prevfloor == floor:
            break

    print(count)

Part1()