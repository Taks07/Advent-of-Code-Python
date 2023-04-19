file = open("Input.txt", "r")
inputarr = []

for line in file:
    inputarr.append(line[:-1])

file.close()

#Part 1
def Part1():
    xpos = 0
    treecount = 0
    lenx = len(inputarr[0])

    for ypos in range(1, len(inputarr)):
        xpos += 3
        if xpos > lenx-1:
            xpos -= lenx

        if inputarr[ypos][xpos] == "#":
            treecount += 1
    print("Trees Hit:",treecount)
        
#Part 2
def TreesEncountered(xshift, yshift):
    xpos = 0
    treecount = 0
    lenx = len(inputarr[0])

    for ypos in range(yshift, len(inputarr), yshift):
        xpos += xshift
        if xpos > lenx-1:
            xpos -= lenx

        if inputarr[ypos][xpos] == "#":
            treecount += 1
    return treecount

def Part2():
    answer = TreesEncountered(1,1)*TreesEncountered(3,1)*TreesEncountered(5,1)*TreesEncountered(7,1)*TreesEncountered(1,2)
    print("Answer:", answer)

    
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart2")
    Part2()


