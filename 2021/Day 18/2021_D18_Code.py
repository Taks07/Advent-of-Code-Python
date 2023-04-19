from ast import literal_eval
from math import floor, ceil
from itertools import permutations

def TryExplode(pair):
    exploded = False
    newpair = ""
    pair = str(pair).replace(" ", "")

    i = 0
    nested = 0

    #print(pair)
    while i < len(pair):
        char = pair[i]

        if char == "[":
            nested += 1

        elif char == "]":
            nested -= 1

        try:
            if nested > 4 and char.isnumeric() and not exploded:
                exploded = True

                leftpart = int(pair[i])


                if pair[i + 1].isnumeric():
                    leftpart = int(str(leftpart) + pair[i + 1])
                    i += 1

                rightpart = int(pair[i+2])

                if pair[i + 3].isnumeric():
                    rightpart = int(str(rightpart) + pair[i + 3])
                    i += 1

                temp = ""
                added = False

                skip = False
                for char in newpair[::-1]:
                    if skip:
                        skip = False
                        continue

                    if char.isnumeric() and not added:
                        if newpair[::-1][newpair[::-1].index(char) + 1].isnumeric():
                            skip = True
                            char += newpair[::-1][newpair[::-1].index(char) + 1]
                            char = char[::-1]

                        added = True
                        temp += str(int(char) + leftpart)[::-1]

                    else:
                        temp += char

                newpair = temp[::-1][:-1]
                newpair += "0"

                i += 4

                while not pair[i].isnumeric() and i < len(pair) - 1:
                    newpair += pair[i]
                    i += 1

                if i < len(pair) - 1:
                    val = pair[i]

                    if pair[i+1].isnumeric():
                        val += pair[i+1]
                        i += 1

                    newpair += str(int(val) + rightpart)

                i += 1
                continue

        except:
            pass

        newpair += char
        i += 1

    nested = 0

    for val in newpair:
        if val == "]":
            nested -= 1

        elif val == "[":
            nested += 1

    for i in range(nested):
        newpair += "]"

    #print(newpair, end = "\n\n")
    return newpair, exploded

def TrySplit(pair):
    pair = str(pair).replace(" ", "")
    newpair = ""
    split = False

    #print(pair)
    i = 0

    while i < len(pair) - 1:
        p1 = pair[i]
        p2 = pair[i + 1]

        if p1.isnumeric() and p2.isnumeric() and not split:
            split = True

            val = int(p1 + p2)
            leftval = str(floor(val/2))
            rightval = str(ceil(val/2))

            newpair += "[" + leftval + "," + rightval + "]"

            i += 2

        newpair += pair[i]
        i += 1

    newpair += "]"

    #print(newpair, end = "\n\n")
    return newpair, split

def Part1():
    numsum = []

    with open("Input.txt", 'r') as file:
        for line in file:
            currline = line[:-1]

            reduced = False

            while 1:
                currline, exploded = TryExplode(currline)

                if exploded:
                    continue

                currline, split = TrySplit(currline)

                if split:
                    continue

                break

            numsum.append(currline)

    while len(numsum) > 1:
        temp = "[" + numsum.pop(0) + "," + numsum.pop(0) + "]"

        while 1:
            temp, exploded = TryExplode(temp)

            if exploded:
                continue

            temp, split = TrySplit(temp)

            if split:
                continue

            break

        numsum.insert(0,temp)

    print("Answer:", FindMagnitude(literal_eval(numsum[0])))

def FindMagnitude(pair):
    if isinstance(pair[0], list):
        p1val = FindMagnitude(pair[0])

    else:
        p1val = pair[0]

    if isinstance(pair[1], list):
        p2val = FindMagnitude(pair[1])

    else:
        p2val = pair[1]

    return p1val*3 + p2val*2

def Part2():
    numsum = []

    with open("Input.txt", 'r') as file:
        for line in file:
            currline = line[:-1]

            reduced = False

            while 1:
                currline, exploded = TryExplode(currline)

                if exploded:
                    continue

                currline, split =  TrySplit(currline)

                if split:
                    continue

                break

            numsum.append(currline)

    max = 0
    for val1, val2 in permutations(numsum,2):
        temp = "[" + val1 + "," + val2 + "]"

        while 1:
            temp, exploded = TryExplode(temp)

            if exploded:
                continue

            temp, split = TrySplit(temp)

            if split:
                continue

            break

        currsum = FindMagnitude(literal_eval(temp))

        if currsum > max:
            max = currsum

    print("Answer:", max)

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
