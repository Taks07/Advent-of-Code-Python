import re
fieldregex = re.compile(r"(\D+): (\d+-\d+) or (\d+-\d+)")

fielddict = {}
othertickets = []

file = open("Input.txt", "r")

line = file.readline().strip("\n")
while len(line) != 0: #Get fields
    if re.match(fieldregex, line):
        vals = re.findall(fieldregex, line)[0]
        fielddict[vals[0]] = [vals[1].split("-"), vals[2].split("-")]

    
    line = file.readline().strip("\n")


next(file) #Skip one line
yourticket = file.readline().strip("\n").split(",")

for i in range(2):
    next(file)

line = file.readline().strip("\n")
while len(line) != 0:
    othertickets.append(line.split(","))
    line = file.readline().strip("\n")

#Part 1
def Part1():
    invalidvals = []
    invalidtickets = []
    for ticket in othertickets:
        for val in ticket:
            invalid = True
            for first, second in fielddict.values():
                if (int(first[0]) <= int(val) <= int(first[1])) or (int(second[0]) <= int(val) <= int(second[1])):
                    invalid = False
                    break
                
            if invalid:
                invalidtickets.append(ticket)
                invalidvals.append(int(val))

    for ticket in invalidtickets:
        othertickets.remove(ticket)

        
                
    print("Answer:", sum(invalidvals))

#Part 2
def Part2():
    yourticketdict = {}
    possiblefields = {}
    for field in fielddict:
        first, second = fielddict[field]
        fieldnumpossible = [x for x in range(len(yourticket))]
        
        for fieldnum in range(len(yourticket)):
               
            for ticket in othertickets:
                if (not (int(first[0]) <= int(ticket[fieldnum]) <= int(first[1]))) and (not (int(second[0]) <= int(ticket[fieldnum]) <= int(second[1]))):
                    fieldnumpossible.remove(fieldnum)
                    break

        possiblefields[field] = fieldnumpossible

    while len(yourticketdict) != len(yourticket):
        for key in possiblefields:
            if len(possiblefields[key]) == 1:
                val = possiblefields[key][0]
                yourticketdict[key] = yourticket[val]
                break

        possiblefields.pop(key)

        for key in possiblefields:
            if val in possiblefields[key]:
                possiblefields[key] = [x for x in possiblefields[key] if x != val]

    total = 1
    for key in yourticketdict:
        if "departure" in key:
            total *= int(yourticketdict[key])

    print("Answer:",total)

    
             
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()

          
                


               
        

    
