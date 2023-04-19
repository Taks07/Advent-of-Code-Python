file = open("Input.txt", "r")
rules = []
passwords = []

for line in file:
    temp = line.split(":")
    rules.append(temp[0])
    passwords.append(temp[1][1:-1])

file.close()

#Part 1
def Part1():
    valcount = 0
    for i in range(len(rules)):
        charcount = 0
        ranges, character = rules[i].split(" ")
        lower, upper = ranges.split("-")      
        
        for char in passwords[i]:
            if char == str(character):
                charcount += 1

        if charcount >= int(lower) and charcount <= int(upper):
            valcount += 1

    print("Answer:",valcount)

#Part 2
def Part2():
    valcount = 0

    for i in range(len(rules)):
        positions, character = rules[i].split(" ")
        pos1, pos2 = positions.split("-")
        pos1flag = pos2flag = False

        count = 0
        for char in range(len(passwords[i])):
            count += 1

            if count == int(pos1):
                if passwords[i][char] == character:
                    pos1flag = True

            if count == int(pos2):
                if passwords[i][char] == character:
                    pos2flag = True         

        if pos1flag != pos2flag: #!= is XOR operator.
            valcount += 1

    print("Answer:", valcount)
                    
        
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
