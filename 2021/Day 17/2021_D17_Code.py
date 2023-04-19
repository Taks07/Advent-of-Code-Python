import re
with open("Input.txt", 'r') as file:
    targetbounds = []

    mo = re.search(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", file.readline())
    targetbounds.append((int(mo.group(1)),int(mo.group(2))))
    targetbounds.append((int(mo.group(3)),int(mo.group(4))))

xarea = [i for i in range(targetbounds[0][0],targetbounds[0][1] + 1)]
yarea = [i for i in range(targetbounds[1][0],targetbounds[1][1] + 1)]

def EmulateShot(xvel,yvel):
    coords = [0,0]
    maxy = 0


    while coords[0] < max(xarea) and coords[1] > min(yarea):
        coords[0] += xvel
        coords[1] += yvel

        if coords[1] > maxy:
            maxy = coords[1]

        if coords[0] in xarea and coords[1] in yarea:
            return maxy, True

        if xvel > 0:
            xvel -= 1

        yvel -= 1

    return 0, False

n = 1
while 0.5*(n)*(n+1) < min(xarea):
    n += 1


def Part1():
    maxy = 0
    for xvel in range(n,int(max(xarea)) + 1):
        for yvel in range(0,1000):
            currmax = EmulateShot(xvel,yvel)[0]
            if currmax > maxy:
                maxy = currmax

    print("Answer:", maxy)

def Part2():
    reached = 0
    for xvel in range(n,int(max(xarea)) + 1):
        for yvel in range(min(yarea),1000):
            if EmulateShot(xvel, yvel)[1]:
                reached += 1

    print("Answer:",reached)

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
