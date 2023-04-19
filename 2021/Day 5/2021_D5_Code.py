import re
diagram = {}
points = []

with open("Input.txt", 'r') as file:
    coordslist = [[[int(k) for k in j.split(',')] for j in i.split(' -> ')] for i in file]

def Is_Diagonal(coord):
    if coord[0][0] != coord[1][0] and coord[0][1] != coord[1][1]:
        return True

    return False

def DrawOrth(coords):
    if coords[0][0] == coords[1][0]:
        # Vertical
        for i in range(coords[0][1], coords[1][1] + 1):
            points.append((coords[0][0],i))
        for i in range(coords[1][1], coords[0][1] + 1):
            points.append((coords[0][0],i))

    else:
        # Horizontal
        for i in range(coords[0][0], coords[1][0] + 1):
            points.append((i,coords[0][1]))
        for i in range(coords[1][0], coords[0][0] + 1):
            points.append((i,coords[0][1]))

def DrawDiag(coord):
    dy = -1
    if coord[1][0] > coord[0][0] and coord[1][1] > coord[0][1]:
        dy = 1

    elif coord[0][0] > coord[1][0] and coord[0][1] > coord[1][1]:
        dy = 1


    for i in range(coord[0][0], coord[1][0] + 1):
        points.append((i,coord[0][1] + (i - coord[0][0])*dy))

    for i in range(coord[1][0], coord[0][0] + 1):
        points.append((i,coord[1][1] + (i - coord[1][0])*dy))



def Part1():
    for coord in coordslist:
        if not Is_Diagonal(coord):
            DrawOrth(coord)

    for point in points:
        if point not in diagram:
            diagram[point] = 1

        else:
            diagram[point] += 1

    count = 0
    for val in diagram.values():
        if val > 1:
            count += 1

    print("Answer:", count)

def Part2():
    global diagram, points
    diagram = {}
    points = []

    for coord in coordslist:
        if not Is_Diagonal(coord):
            DrawOrth(coord)

        else:
            DrawDiag(coord)

    for point in points:
        if point not in diagram:
            diagram[point] = 1

        else:
            diagram[point] += 1

    count = 0
    for val in diagram.values():
        if val > 1:
            count += 1

    print("Answer:", count)


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
