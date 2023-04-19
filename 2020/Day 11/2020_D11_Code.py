import copy
file = open("Input.txt", "r")
inputarr = []

for line in file:
    chararray = []
    for char in line:
        if char != "\n":
            chararray.append(char)
    inputarr.append(chararray)
file.close()

#Part 1
def ApplyRules1():
    combos = ((0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1))
    copyarr1 = copy.deepcopy(inputarr)
    copyarr2 = copy.deepcopy(inputarr)

    while True:
        for row in range(len(copyarr1)):
            for column in range(len(copyarr1[0])):
                occupied = 0
                if copyarr1[row][column] != ".":    
                    for rowdiff, coldiff in combos:
                        if row + rowdiff not in (-1, len(copyarr1)) and column + coldiff not in (-1, len(copyarr1[0])):
                            if copyarr1[row + rowdiff][column + coldiff] == "#":
                                occupied += 1
                                

                    if copyarr1[row][column] == "L" and occupied == 0:
                        copyarr2[row][column] = "#"

                    elif copyarr1[row][column] == "#" and occupied > 3:
                        copyarr2[row][column] = "L"
                            
        if copyarr1 == copyarr2:
            return copyarr2

        else:
            copyarr1 = copy.deepcopy(copyarr2)



def Part1():
    finalseating = ApplyRules1()
        
    count = 0

    for row in finalseating:
            for column in row:
                if column == "#":
                    count += 1

    print("Number of Occupied Seats:", count)

#Part 2
def ApplyRules2():
    combos = ((0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1))
    copyarr1 = copy.deepcopy(inputarr)
    copyarr2 = copy.deepcopy(inputarr)

    while True:
        for row in range(len(copyarr1)):
            for column in range(len(copyarr1[0])):
                occupied = 0
                if copyarr1[row][column] != ".":    
                    for rowdiff, coldiff in combos:
                        multiple = 1
                        while (row + rowdiff * (multiple)) > -1 and (row + rowdiff * (multiple)) < len(copyarr1) and (column + coldiff * (multiple)) > -1 and (column + coldiff * (multiple)) < len(copyarr1[0]):
                            if copyarr1[row + rowdiff * multiple][column + coldiff * multiple] != ".":
                                if copyarr1[row + rowdiff * multiple][column + coldiff * multiple] == "#":
                                    occupied += 1            
                                break
                            multiple +=1

                        
                                                                                                                                                                                                                                                                                                                                                                                                                                      
                    if copyarr1[row][column] == "L" and occupied == 0:
                        copyarr2[row][column] = "#"

                    elif copyarr1[row][column] == "#" and occupied >= 5:
                        copyarr2[row][column] = "L"

        if copyarr1 == copyarr2:
            return copyarr2

        else:
            copyarr1 = copy.deepcopy(copyarr2)
                                     
                     

        


        

def Part2():
    finalseating = ApplyRules2()
        
    count = 0

    for row in finalseating:
            for column in row:
                if column == "#":
                    count += 1

    print("Number of Occupied Seats:", count)
    
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()

