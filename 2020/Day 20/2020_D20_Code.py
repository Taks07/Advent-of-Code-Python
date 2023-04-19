file = open("Input.txt", "r")
tiledict = {}

line = file.readline()


while len(line) != 0:
    idnum = line[5:-2]
    tilearr = []

    line = file.readline()[:-1]
    while len(line) != 0:
        tilearr.append(line)
        line = file.readline()[:-1]

    tiledict[idnum] = tilearr
    line = file.readline()

#Part 1
def GetLeftRight(idnum):
    tile = tiledict[idnum]
    sidestr = ["", ""]

    for row in tile:
        sidestr[0] += row[0]
        sidestr[1] += row[-1]

    sidestr.append(sidestr[0][::-1])
    sidestr.append(sidestr[1][::-1])

    return sidestr

def GetTopBottom(idnum):
    tile = tiledict[idnum]
    topbttmstr = [tile[0], tile[-1]]

    topbttmstr.append(topbttmstr[0][::-1])
    topbttmstr.append(topbttmstr[1][::-1])

    return topbttmstr

def CheckIfCantJoin(idnum):
    allsides = GetLeftRight(idnum) + GetTopBottom(idnum)

    for otherid in [x for x in tiledict if x != idnum]:
        otherallsides = GetLeftRight(otherid) + GetTopBottom(otherid)

        for string in allsides:
            if string in otherallsides:
                reverse = string[::-1]

                allsides.remove(string)
                allsides.remove(reverse)            

    return allsides

def Part1():
    corners = []
    for idnum in tiledict:
        unjoinablesides = CheckIfCantJoin(idnum)

        if len(unjoinablesides) == 4:
            corners.append(idnum)

    total = 1
    for idnum in corners:
        total *= int(idnum)

    print("Answer:",total)
    
if __name__ == "__main__":
    print("Part 1")
    Part1()

#Part 2
def RotateTile(idnum):
    tile = tiledict[idnum]

    temptile = []

    for i in range(len(tile)-1, -1, -1):
        temprow = ""
        for row in tile:
            temprow += row[i]

        temptile.append(temprow)

    tiledict[idnum] = temptile

def FlipTileHorizontal(idnum):
    tile = tiledict[idnum]

    temptile = []

    for row in tile:
        temptile.append(row[::-1])

    tiledict[idnum] = temptile

def FlipTileVertical(idnum):
    for _ in range(2):
        RotateTile(idnum)

    FlipTileHorizontal(idnum)

def GetCurrSides(idnum):
    tile = tiledict[idnum]
    sidestr = ["", ""]
    for row in tile:
        sidestr[0] += row[0]
        sidestr[1] += row[-1]

    sidestr.append(sidestr[0][::-1])
    sidestr.append(sidestr[1][::-1])

    return [sidestr[0], tile[0], sidestr[1], tile[-1]] #left, top, right, bottom

def CheckIfCantJoin(idnum):
    allsides = GetLeftRight(idnum) + GetTopBottom(idnum)

    for otherid in [x for x in tiledict if x != idnum]:
        otherallsides = GetLeftRight(otherid) + GetTopBottom(otherid)

        for string in allsides:
            if string in otherallsides:
                reverse = string[::-1]

                allsides.remove(string)
                allsides.remove(reverse)

    return allsides
    
def CreateImage():
    fullimage = []
    
    corners = []
    others = []

    for idnum in tiledict:
        unjoinablesides = CheckIfCantJoin(idnum)

        if len(unjoinablesides) == 4:
            corners.append(idnum)

        else:
            others.append(idnum)
                 
    sidelength = int(len(tiledict) ** 0.5)

    topleft = corners.pop(0)

    currsides = GetCurrSides(topleft)

    temprow = []
    while (GetCurrSides(topleft)[0] not in CheckIfCantJoin(topleft)):
        RotateTile(topleft)

    if (GetCurrSides(topleft)[1] not in CheckIfCantJoin(topleft)):
        FlipTileVertical(topleft)

    temprow.append(topleft)

    others = others + corners

    while len(temprow) != sidelength:
        prevtile = GetCurrSides(temprow[-1])[2]
        
        for idnum in others:
            for _ in range(4):
                if prevtile != GetCurrSides(idnum)[0]:
                    RotateTile(idnum)

                else:
                    break

            if prevtile != GetCurrSides(idnum)[0]:
                FlipTileHorizontal(idnum)

                for _ in range(4):
                    if prevtile != GetCurrSides(idnum)[0]:
                        RotateTile(idnum)

                    else:
                        break

            if prevtile == GetCurrSides(idnum)[0]:
                temprow.append(idnum)
                others.remove(idnum)
                break
    fullimage.append(temprow)

    while len(fullimage) != sidelength:
        temprow = []
        topidnum = fullimage[-1][0]

        prevtile = GetCurrSides(topidnum)[3]
        for idnum in others:
            for _ in range(4):
                if prevtile != GetCurrSides(idnum)[1]:
                    RotateTile(idnum)

                else:
                    break

            if prevtile != GetCurrSides(idnum)[1]:
                FlipTileHorizontal(idnum)

                for _ in range(4):
                    if prevtile != GetCurrSides(idnum)[1]:
                        RotateTile(idnum)

                    else:
                        break

            if prevtile == GetCurrSides(idnum)[1]:
                temprow.append(idnum)
                others.remove(idnum)
                break

        while len(temprow) != sidelength:
            prevtile = GetCurrSides(temprow[-1])[2]
            
            for idnum in others:
                for _ in range(4):
                    if prevtile != GetCurrSides(idnum)[0]:
                        RotateTile(idnum)

                    else:
                        break

                if prevtile != GetCurrSides(idnum)[0]:
                    FlipTileHorizontal(idnum)

                    for _ in range(4):
                        if prevtile != GetCurrSides(idnum)[0]:
                            RotateTile(idnum)

                        else:
                            break

                if prevtile == GetCurrSides(idnum)[0]:
                    temprow.append(idnum)
                    others.remove(idnum)
                    break
        fullimage.append(temprow)

    return fullimage

def JoinImage(fullimage = CreateImage()):
    imagetile = []

    for tilerow in fullimage:  
        for i in range(1,9):
            temprow = ""
            for idnum in tilerow:
                temprow += tiledict[idnum][i][1:9]

            imagetile.append(temprow)
    return imagetile

def CheckSpace(y, x, image):
    return image[y][x] == image[y+1][x+1] == image[y+1][x+4] == image[y][x+5] == image[y][x+6] == image[y+1][x+7] == image[y+1][x+10] == image[y][x+11] == image[y][x+12] == image[y+1][x+13] == image[y+1][x+16] == image[y][x+17] == image[y][x+18] == image[y-1][x+18] == image[y][x+19] == "#"
            
    
def CheckForMonsters(imagekey):
    monsters = 0

    for _ in range(4):
        image = tiledict[imagekey]
        for y in range(1, len(image)-1):
            for x in range(0, len(image[0])-19):
                if CheckSpace(y,x, image):
                    monsters += 1

        if monsters > 0:
            return monsters

        else:
            RotateTile(imagekey)

    if monsters == 0:
        FlipTileHorizontal(imagekey)

        for _ in range(4):
            image = tiledict[imagekey]
            for y in range(1, len(image)-1):
                for x in range(0, len(image[0])-19):
                    if CheckSpace(y,x,image):
                        monsters += 1

            if monsters > 0:
                return monsters

            else:
                RotateTile(imagekey)

def Part2():
    tiledict["image"] = JoinImage()

    monstercount = CheckForMonsters("image")
    hashcount = 0

    for row in tiledict["image"]:
        for char in row:
            if char == "#":
                hashcount += 1
    print("Answer:", hashcount - monstercount*15)

if __name__ == "__main__":
    print("\nPart 2")
    Part2()

        
                
                
            

            
                
            
            
        
    


        

    
        
        
