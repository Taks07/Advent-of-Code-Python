import collections
import copy

with open("Input.txt", 'r') as file:
    paths = collections.defaultdict(list)

    for line in file:
        cavern = line[:-1].split("-")

        paths[cavern[0]].append(cavern[1])
        paths[cavern[1]].append(cavern[0])

def NextCave(currcave, smallcaves, repeat):
    smallcaves = copy.deepcopy(smallcaves)

    if currcave == "end":
        return 1

    if currcave.islower():
        smallcaves.append(currcave)

    numpaths = 0
    for nextcave in paths[currcave]:
        if not (nextcave.islower() and nextcave in smallcaves):
            numpaths += NextCave(nextcave,smallcaves,repeat)

        elif repeat and smallcaves.count(nextcave) == 1 and nextcave != "start":
            numpaths += NextCave(nextcave, smallcaves, False)

    return numpaths

print("Part 1:", NextCave("start", [], False))
print("Part 2:", NextCave("start", [], True))