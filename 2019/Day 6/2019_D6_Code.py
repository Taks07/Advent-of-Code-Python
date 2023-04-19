import copy
from collections import deque
DirectOrbits = {}

file = open("Input.txt", 'r')

for line in file:
    contents = line[:-1].split(")")

    if contents[0] not in DirectOrbits.keys():
        DirectOrbits[contents[0]] = [contents[1]]

    else:
        DirectOrbits[contents[0]].append(contents[1])

file.close()


for arr in copy.deepcopy(list(DirectOrbits.values())):
    for obj in arr:
        if obj not in DirectOrbits.keys():
            DirectOrbits[obj] = []

#Part 1
def Count(currobj = "COM", distance = -1, count = 0):
    distance += 1
    count += distance

    if len(DirectOrbits[currobj]) != 0:
      for obj in DirectOrbits[currobj]:

          count = Count(obj, distance, count)

    return count

def Part1():
    print("Count:", Count())

def GetPath(toObj):
    TempOrbits = copy.deepcopy(DirectOrbits)
    currObj = "COM"
    count = -1

    path = deque() # Create deque object to act as stack. Use append() and pop() to push and pop respectively

    while 1:
        count += 1
        path.append(currObj)

        if currObj == toObj:
            return list(path), count

        elif len(TempOrbits[currObj]) == 0:
            while len(TempOrbits[currObj]) == 0:
                count -= 1
                currObj = path.pop()

        else:
            currObj = TempOrbits[currObj].pop()



def Part2():
    YOUpath, YOUcount = GetPath("YOU") # Get path to YOU and SAN as well as jumps needed
    SANpath, SANcount = GetPath("SAN")
    pointcount = 0
    branch = False

    point = YOUpath[0]
    while not branch: # Find common branching point and jumps needed to reach
        pointcount += 1
        if YOUpath[1] != SANpath[1]:
            branch = True

        else:
            YOUpath.pop(0)
            SANpath.pop(0)
            point = YOUpath[0]

    print("Transfers Needed:", YOUcount + SANcount - (2 * pointcount)) #Calculate distance between. Find difference between YOUcount/SANcount and pointcount. Then, sum


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()

