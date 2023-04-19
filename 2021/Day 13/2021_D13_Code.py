import copy
import pprint

with open("Input.txt", 'r') as file:
    dots = []
    folds = []

    line = file.readline()
    while line != "\n":
        dots.append(line[:-1].split(","))
        line= file.readline()

    dots = [[int(i) for i in coords] for coords in dots]
    for line in file:
        instruction = line[:-1].split(" ")[2].split("=")

        folds.append(instruction)

    folds = [[coords[0], int(coords[1])] for coords in folds]

max = [-1000000000000000000,-1000000000000000000]

for x,y in dots:
    if x > max[0]:
        max[0] = x

    if y > max[1]:
        max[1] = y

transpaper = [["." for col in range(max[0] + 1)] for row in range(max[1] + 1)]

for col, row in dots:
    transpaper[row][col] = "#"

def FoldVertically(paper, yval):
    copypaper = copy.deepcopy(paper)

    half1 = []
    half2 = []

    for i,row in enumerate(copypaper): #half2 should be shorter than half1
        if i < yval:
            half1.append(row)

        elif i > yval:
            half2.append(row)

    if len(half2) > len(half1):
        temp = copy.deepcopy(half1)
        half1 = copy.deepcopy(half2)[::-1]
        half2 = copy.deepcopy(temp)[::-1]

    for i in range(len(half2)):
        half1line = half1[(i * -1) - 1]
        half2line = half2[i]

        for val in range(len(half1line)):
            if half1line[val] != half2line[val]:
                half1line[val] = "#"

    return copy.deepcopy(half1)

def FoldHorizontally(paper, xval):
    copypaper = copy.deepcopy(paper)

    half1 = []
    half2 = []

    for row in copypaper:
        temp1 = []
        temp2 = []
        for i in range(len(copypaper[0])):
            if i < xval:
                temp1.append(row[i])

            elif i > xval:
                temp2.append(row[i])

        half1.append(temp1)
        half2.append(temp2)

    if len(half2[0]) > len(half1[0]):
        temp = [[i for i in row[::-1]] for row in half1]
        half1 = [[i for i in row[::-1]] for row in half2]
        half2 = copy.deepcopy(temp)

    for rownum in range(len(half1)):
        half1line = half1[rownum]
        half2line = half2[rownum]

        for valnum in range(len(half2line)):
            if half1line[(valnum * -1) - 1] != half2line[valnum]:
                half1line[(valnum * -1) - 1] = "#"

    return copy.deepcopy(half1)

def Part1():
    global transpaper

    firstfold = folds.pop(0)
    if firstfold[0] == "x":
        transpaper = FoldHorizontally(transpaper,firstfold[1])

    else:
        transpaper = FoldVertically(transpaper, firstfold[1])

    print("Answer:", sum([sum([1 for val in row if val == "#"]) for row in transpaper]))

def Part2():
    global transpaper

    for axis, val in folds:
        if axis == "x":
            transpaper = FoldHorizontally(transpaper,val)

        else:
            transpaper = FoldVertically(transpaper,val)

    for line in transpaper:
        print("".join([" " if i == "." else "#" for i in line]))

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()