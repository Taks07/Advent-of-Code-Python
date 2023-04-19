with open("Input.txt", 'r') as file:
    pairs = []

    for line in file:
        pair = line[:-1].split(',')

        pair[0] = pair[0].split('-')
        pair[1] = pair[1].split('-')

        pairs.append(pair)

def CheckRedundant(pair1, pair2):
    if (int(pair1[0]) <= int(pair2[0])) and (int(pair1[1]) >= int(pair2[1])):
        return True

    elif (int(pair2[0]) <= int(pair1[0])) and (int(pair2[1]) >= int(pair1[1])):
        return True

    else:
        return False

def Part1():
    count = 0

    for pair in pairs:
        if CheckRedundant(pair[0], pair[1]):
            count += 1

    print("Ans:", count)

def CheckOverlap(pair1, pair2):
    if (int(pair1[1]) < int(pair2[0])) or (int(pair1[0]) > int(pair2[1])):
        return False

    elif (int(pair2[1]) < int(pair1[0])) or (int(pair2[0]) > int(pair1[1])):
        return False

    else:
        return True

def Part2():
    count = 0

    for pair in pairs:
        if CheckOverlap(pair[0], pair[1]):
            count += 1

    print("Ans:", count)

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()