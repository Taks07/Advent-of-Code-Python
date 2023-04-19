import copy
import itertools

class Scanner():
    def __init__(self, beacons):
        self.beaconcoords = beacons
        self.offset = [0,0,0]

        self.FindDistances()

    def FindDistances(self):
        self.distances = {beacon:set() for beacon in self.beaconcoords}

        for currbeacon, comparebeacon in itertools.permutations(self.beaconcoords, 2):
            self.distances[currbeacon].add(sum([(comparebeacon[i] - currbeacon[i])**2 for i in range(len(currbeacon))]))

    def AddBeacons(self, seperatebeacons):
        for beacon in seperatebeacons:
            self.beaconcoords.append(tuple(beacon))

        self.FindDistances()

scanners = []
with open("Input.txt", 'r') as file:
    line = file.readline()

    while line != "":
        beacons = []

        line = file.readline()

        while line not in ("\n", ""):
            beacon = line[:-1].split(",")
            beacons.append(tuple([int(i) for i in beacon]))

            line = file.readline()

        scanners.append(Scanner(beacons))
        line = file.readline()

def DetermineOffset(samebeacons, seperatebeacons): #will return oriented seperatebeacons and offset. no need to return samebeacons as can just remove
    basesamebeacons = [b[0] for b in samebeacons] # same beacons from POV of base
    currsamebeacons = [b[1] for b in samebeacons] # same beacons from POV of curr. will be changed until correct orrientation. seperatebeacons will follow same change

    for newcurrsame, newseperate in Orientations(currsamebeacons, seperatebeacons):
        offset = [newcurrsame[0][0] - basesamebeacons[0][0], newcurrsame[0][1] - basesamebeacons[0][1], newcurrsame[0][2] - basesamebeacons[0][2]]

        if all([[newcurrsame[i][0] - basesamebeacons[i][0], newcurrsame[i][1] - basesamebeacons[i][1], newcurrsame[i][2] - basesamebeacons[i][2]] == offset for i in range(len(basesamebeacons))]):
            return newseperate, offset

def Orientations(currsamebeacons, seperatebeacons): #Hardcoded orientations. It's late
    beacons = currsamebeacons + seperatebeacons
    copybeacons = copy.deepcopy(beacons)
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[0], -b[1], -b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[0], b[1], -b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[0], -b[1], b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[0], b[2], -b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[0], b[2], b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[0], -b[2], b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[0], -b[2], -b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[1], b[0], -b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[1], b[0], b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[1], -b[0], b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[1], -b[0], -b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[1], b[2], b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[1], b[2], -b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[1], -b[2], -b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[1], -b[2], -b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[2], b[0], b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[2], b[0], -b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[2], -b[0], -b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[2], -b[0], b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[2], b[1], -b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[2], b[1], b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([b[2], -b[1], b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    beacons = [copy.deepcopy([-b[2], -b[1], -b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] #done

    #mirrored cause i messed up orientations. so, just doing all 48
    beacons = [copy.deepcopy([b[0], b[1], -b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[0], -b[1], b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[0], b[1], b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[0], -b[1], -b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[0], b[2], b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[0], b[2], -b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[0], -b[2], -b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[0], -b[2], b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[1], b[0], b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[1], b[0], -b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[1], -b[0], -b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[1], -b[0], b[2]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[1], b[2], -b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[1], b[2], b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[1], -b[2], b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[1], -b[2], b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[2], b[0], -b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[2], b[0], b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[2], -b[0], b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] # done

    beacons = [copy.deepcopy([-b[2], -b[0], -b[1]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[2], b[1], b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[2], b[1], -b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([b[2], -b[1], -b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):]  # done

    beacons = [copy.deepcopy([-b[2], -b[1], b[0]]) for b in copybeacons]
    yield beacons[:len(currsamebeacons)], beacons[len(currsamebeacons):] # done

scannerlocs = [[0,0,0]]
def Part1():
    basescanner = scanners.pop(0) #Compare and orient all scanners with scanner 0. Add to self.beaconcoords with each currscanner to build up final map.

    while scanners != []:
        toremove = []

        for currscanner in scanners:
            samebeacons = []

            if basescanner != currscanner:
                for basebeacon in basescanner.beaconcoords:
                    for currbeacon in currscanner.beaconcoords:
                        if len(basescanner.distances[basebeacon].intersection(currscanner.distances[currbeacon])) > 10: # Use 10 as not including self. So, 11 matching distances or more
                            samebeacons.append([list(basebeacon), list(currbeacon)]) #The same beacon as seen from diff scanners. Now orientate currbeacon.
                            break #Know correct orientation if offset for each pair is constant

                    if len(basescanner.distances[basebeacon].intersection(currscanner.distances[currbeacon])) > 10:
                        continue

                seperatebeacons = [list(b) for b in currscanner.beaconcoords if list(b) not in [a[1] for a in samebeacons]] #Seperate the unique beacons from ones that coincide with base scanner

                if len(samebeacons) < 12:
                    continue

                seperatebeacons, offset = DetermineOffset(samebeacons, seperatebeacons)

                scannerlocs.append([-i for i in offset])
                seperatebeacons = [[b[0] - offset[0], b[1] - offset[1], b[2] - offset[2]] for b in seperatebeacons]


                toremove.append(currscanner)
                basescanner.AddBeacons(seperatebeacons)

        for scan in toremove:
            scanners.remove(scan)


    print("Answer:", len(basescanner.beaconcoords))

def Part2():
    print("Answer:", max([sum([abs(s1[i]-s2[i]) for i in range(3)]) for s1, s2 in itertools.combinations(scannerlocs, 2)]))


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()