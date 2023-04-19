import collections

with open("Input.txt", 'r') as file:
    paths = collections.defaultdict(list)

    for line in file:
        cavern = line[:-1].split("-")

        paths[cavern[0]].append(cavern[1])
        paths[cavern[1]].append(cavern[0])

def NextCave(takenpath, repeat):
    if takenpath[-1] == "end":
        return 1

    numpaths = 0

    for nextcave in paths[takenpath[-1]]:
        if not (nextcave.islower() and nextcave in takenpath):
            numpaths += NextCave(takenpath + [nextcave,], repeat)

        elif repeat and takenpath.count(nextcave) == 1 and nextcave != "start":
            numpaths += NextCave(takenpath + [nextcave,], False)

    return numpaths

def Part1():
    print("Number of Paths:", NextCave(["start"], False))

def Part2():
    print("Number of Paths", NextCave(["start"], True))

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
