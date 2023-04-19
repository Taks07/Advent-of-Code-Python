with open("Input.txt", 'r') as file:
    crabs = file.readline().split(',')
    crabs = [int(crab) for crab in crabs]

def FuelCost1(currpos, dest):
    return abs(currpos - dest)

def Part1():
    minfuelcost = 10000000000000000000000
    for i in range(min(crabs), max(crabs) + 1):
        currfuelcost = 0

        for crab in crabs:
            currfuelcost += FuelCost1(crab, i)

        if currfuelcost < minfuelcost:
            minfuelcost = currfuelcost

    print("Answer:", minfuelcost)

def FuelCost2(currpos, dest):
    steps = abs(currpos - dest)
    return int(0.5*(steps)*(steps + 1))

def Part2():
    minfuelcost = 10000000000000000000000
    for i in range(min(crabs), max(crabs) + 1):
        currfuelcost = 0

        for crab in crabs:
            currfuelcost += FuelCost2(crab, i)

        if currfuelcost < minfuelcost:
            minfuelcost = currfuelcost

    print("Answer:", minfuelcost)

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()