import re
containingbag = re.compile(r"(.+)bags ")
bagsinside = re.compile(r"(\d|no other)(.+?) ?bag(?:s)?")
bagdict = {}

file = open("Input.txt", "r")

for line in file:
    container = containingbag.search(line).group(1).strip()
    contents = bagsinside.findall(line)

    for i in range(len(contents)):
        contents[i] = [contents[i][0],contents[i][1].strip()]
        

    if contents[0][0] == "no other":
        contents = [[0, ""]]
        
    bagdict[container] = contents

#Part 1
has_gold = []
no_gold = []

def CheckInside(bagarray):
    gold = False
    
    for bagdetails in bagarray:    
        if (bagdetails[1] in has_gold or bagdetails[1] == "shiny gold") and not gold:
            gold = True

        elif (bagdetails[1] in no_gold or bagdetails[0] == 0) and not gold:
            pass

        elif not gold:
            gold = CheckInside(bagdict[bagdetails[1]])

    return gold
        
    
def Part1():
    count = 0
    for container in bagdict.keys():
        gold = CheckInside(bagdict[container])

        if gold:
            count += 1
            has_gold.append(container)

        else:
            no_gold.append(container)

    print("Count:",count)

#Part 2
def NumBagsInside(bagarray, number):
    thiscount = 0

    for bagdetails in bagarray:
        thiscount += number * int(bagdetails[0])

        if bagdetails[1] != "":
            thiscount += number * NumBagsInside(bagdict[bagdetails[1]], int(bagdetails[0]))

    return thiscount

        

def Part2():
    print("Count:",NumBagsInside(bagdict["shiny gold"], 1))

    
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
        
