file = open("Input.txt", "r")
inputarr = []

for line in file:
    inputarr.append(line[:-1])

file.close()
    
#Part 1
def Part1():
    highestID = 0
    
    for seat in inputarr:
        row, column = seat[0:7], seat[-3:]
        
        startrow = 0
        endrow = 127

        for char in row:
            middlerow = (startrow + endrow)/2
            
            if char == "F":
                endrow = int(middlerow)

            else:
                startrow = round(middlerow)

        if row[-1] == "F":
            middlerow = int(middlerow - 0.5)

        else:
            middlerow = int(middlerow + 0.5)

        startcol = 0
        endcol = 7

        for char in column:
            middlecol = (startcol + endcol)/2

            if char == "L":
                endcol = int(middlecol)

            else:
                startcol = round(middlecol)

        if column[-1] == "L":
            middlecol = int(middlecol - 0.5)

        else:
            middlecol = int(middlecol + 0.5)

        seatID = (middlerow * 8) + middlecol
        
        if seatID > highestID:
            highestID = seatID

    print("Highest ID:",highestID)

def Part2():
    idlist = []
    for seat in inputarr:
        row, column = seat[0:7], seat[-3:]
        
        startrow = 0
        endrow = 127

        for char in row:
            middlerow = (startrow + endrow)/2
            
            if char == "F":
                endrow = int(middlerow)

            else:
                startrow = round(middlerow)

        if row[-1] == "F":
            middlerow = int(middlerow - 0.5)

        else:
            middlerow = int(middlerow + 0.5)

        startcol = 0
        endcol = 7

        for char in column:
            middlecol = (startcol + endcol)/2

            if char == "L":
                endcol = int(middlecol)

            else:
                startcol = round(middlecol)

        if column[-1] == "L":
            middlecol = int(middlecol - 0.5)

        else:
            middlecol = int(middlecol + 0.5)

        seatID = (middlerow * 8) + middlecol
        idlist.append(seatID)

    for val1 in idlist:
        for val2 in idlist:
            if (val1 - val2) == 2 and (val1+val2)/2 not in idlist:
                print("Seat ID:", val1-1)
        
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
    
