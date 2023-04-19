file = open("Input.txt", "r")
inputarr = []

for line in file:
    inputarr.append([line[0], int(line[1:-1])])

file.close()

#Part 1
def ChangeFacing(facing, direction):
    directionarr = ("N", "E", "S", "W")
    currfacingindex = directionarr.index(facing)
    
    if direction == "L":
        currfacingindex -= 1

    else:
        currfacingindex += 1

    if currfacingindex == -1:
        currfacingindex = 3

    elif currfacingindex == 4:
        currfacingindex = 0

    return directionarr[currfacingindex]
        
        
    
def Part1():
    facing = "E"
    distance = [0,0] #[horizonal, vertical]
    directions = {"N": [0,1], "E": [1,0], "W": [-1,0], "S": [0,-1]}
    
    for instruction in inputarr:
        if instruction[0] == "F":
            distance[0] += directions[facing][0] * instruction[1]
            distance[1] += directions[facing][1] * instruction[1]

        elif instruction[0] in ("N", "E", "W", "S"):
            distance[0] += directions[instruction[0]][0] * instruction[1]
            distance[1] += directions[instruction[0]][1] * instruction[1]

        else:
            for i in range(instruction[1]//90):
                facing = ChangeFacing(facing, instruction[0])

    print("Distance:", abs(distance[0]) + abs(distance[1]))

#Part 2
def RotateWaypoint(waypoint, direction):
    if direction == "L":
        waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]

    else:
        waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]

    return waypoint
    

def Part2():
    waypoint = [10, 1]
    distance = [0,0]
    directions = {"N": [0,1], "E": [1,0], "W": [-1,0], "S": [0,-1]}

    for instruction in inputarr:
        if instruction[0] in ("N", "E", "W", "S"):
            waypoint[0] += directions[instruction[0]][0] * instruction[1]
            waypoint[1] += directions[instruction[0]][1] * instruction[1]

        if instruction[0] == "F":
            distance[0] += waypoint[0] * instruction[1]
            distance[1] += waypoint[1] * instruction[1]

        else:
            for i in range(instruction[1]//90):
                waypoint = RotateWaypoint(waypoint, instruction[0])

    print("Distance:", abs(distance[0]) + abs(distance[1]))
        
    
    
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
        
    
    
