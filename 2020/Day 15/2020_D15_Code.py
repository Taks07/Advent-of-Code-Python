file = open("Input.txt", "r")
line = file.readline()[:-1]

inputarr = [int(x) for x in line.split(",")]
diffdict = {}

for val in inputarr:
    diffdict[val] = [inputarr.index(val), 0] #[index of latest time said, diff]

#Part 1 and 2           
def Part1and2(limit):
    while len(inputarr) < limit:
        lastspoken = inputarr[-1]
        nextindex = len(inputarr)

        newval = diffdict[lastspoken][1]
        inputarr.append(newval)

        if newval not in diffdict.keys():
            diffdict[newval] = [nextindex, 0]

        else:
            diffdict[newval] = [nextindex, nextindex - diffdict[newval][0]]
            

    print("Answer:",inputarr[-1])
    
             
if __name__ == "__main__":
    print("Part 1")
    Part1and2(2020)

    print("\nPart 2")
    Part1and2(30000000)
        
