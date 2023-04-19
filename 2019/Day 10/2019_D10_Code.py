import math
file = open("Input.txt", 'r')

field = []
for line in file:
    field.append(list(line[:-1]))

file.close()


jumppairs = []
for j in range(len(field) * -1, len(field)):
    for i in range(len(field[0]) * -1, len(field[0])):
        if math.gcd(i, j) == 1:
            jumppairs.append((i,j))

def CheckTile(x,y):
    count = 0
    for pair in jumppairs:
        xcurr, ycurr = x,y
        while 1:
            ycurr += pair[1]
            xcurr += pair[0]

            if -1 < xcurr < len(field[0]) and -1 < ycurr < len(field):
                if field[ycurr][xcurr] == "#":
                    count += 1
                    break

            else:
                break


    return count

def Part1():
    mostseen = 0

    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == "#":
                currseen = CheckTile(x,y)

                if currseen > mostseen:
                    mostseen = currseen
                    coords = (x,y)

    print("Asteroids Detected:", mostseen)
    return coords

def FindDegrees(stationcoords, x, y):
    deltax = stationcoords[0] - x
    deltay =  stationcoords[1] - y


    angle = math.degrees(math.atan2(deltax, deltay))

    if (-90 < angle < 0) or (-180 < angle <= -90): #QUAD 1 or QUAD 4
        angle *= -1

    elif (0 < angle <= 90) or (90 < angle < 180): #QUAD 2 or QUAD 3
        angle = 360 - angle

    distance = ((deltax ** 2) + (deltay ** 2)) ** 0.5

    return angle, distance

def Part2(stationcoords):
    asteroids = []

    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == "#":
                angle, degrees = FindDegrees(stationcoords, x,y)

                asteroids.append((angle, degrees, (x,y)))

    asteroids = sorted(asteroids, key = lambda x: (x[0], x[1])) #sort according to angle then by distance
    coords = []

    i = 0
    while i < len(asteroids) - 1:
        LoS = [] #Asteroids in same line of sight
        currdeg = asteroids[i][0]

        LoS.append(asteroids[i][2])

        i += 1

        while currdeg == asteroids[i][0]:
            LoS.append(asteroids[i][2])
            i += 1

        coords.append(LoS)

    count = 0
    while 1:
        for ang in coords:

            try:
                currcoord = ang.pop(0)
                count += 1

            except:
                pass

            if count == 200:
                print("Answer:", currcoord[0] * 100 + currcoord[1])

if __name__ == "__main__":
    print("Part 1")
    stationcoords = Part1()

    print("\nPart 2")
    field[stationcoords[1]][stationcoords[0]] = "X"
    Part2(stationcoords)

