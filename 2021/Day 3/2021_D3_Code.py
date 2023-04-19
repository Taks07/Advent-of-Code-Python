import copy
binaryvalues = []

with open("Input.txt", 'r') as file:
    for line in file:
        binaryvalues.append(line[:-1])

def FindMostCommon(vals):
    mostcommon = [[0, 0] for i in range(len(vals[0]))]

    for value in vals:
        for i in range(len(value)):
            mostcommon[i][int(value[i])] += 1

    return mostcommon


def Part1():
    numbercount = FindMostCommon(binaryvalues)

    gammarate = ""
    epsilonrate = ""

    for pair in numbercount:
        if pair[0] > pair[1]:
            gammarate += "0"
            epsilonrate += "1"

        else:
            gammarate += "1"
            epsilonrate += "0"

    print("Answer:", int(gammarate,2) * int(epsilonrate,2))


def Part2():
    ratings = []

    bincopy = copy.deepcopy(binaryvalues)

    for i in range(len(bincopy[0])):
        numbercount = FindMostCommon(bincopy)
        mostcommon = ""

        for pairs in numbercount:
            if pairs[0] > pairs[1]:
                mostcommon += "0"

            elif pairs[1] > pairs[0]:
                mostcommon += "1"

            else:
                mostcommon += "2"

        for val in binaryvalues:
            if mostcommon[i] == "2" and val[i] == "0" and len(bincopy) != 1:
                try:
                    bincopy.remove(val)

                except:
                    pass

            elif val[i] != mostcommon[i] and len(bincopy) != 1:
                try:
                    bincopy.remove(val)

                except:
                    pass

            if len(bincopy) == 1:
                break


    ratings.append(bincopy[0])

    bincopy = copy.deepcopy(binaryvalues)

    for i in range(len(bincopy[0])):
        numbercount = FindMostCommon(bincopy)
        mostcommon = ""

        for pairs in numbercount:
            if pairs[0] > pairs[1]:
                mostcommon += "0"

            elif pairs[1] > pairs[0]:
                mostcommon += "1"

            else:
                mostcommon += "2"

        for val in binaryvalues:
            if mostcommon[i] == "2" and val[i] == "1" and len(bincopy) != 1:
                try:
                    bincopy.remove(val)

                except:
                    pass

            elif val[i] == mostcommon[i] and len(bincopy) != 1:
                try:
                    bincopy.remove(val)

                except:
                    pass

            if len(bincopy) == 1:
                break

    ratings.append(bincopy[0])

    print("Answer:", int(ratings[0], 2) * int(ratings[1], 2))



if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()



