import re
file = open("Input.txt", "r")
rulesdict = {}

line = file.readline()

while line != "\n":
    temp = line[:-1].split(":")
    temparr = []

    if "|" in temp[1]:
        val = temp[1].strip(" ").split("|")

        for choice in val:
            temparr.append(choice.strip(" ").split(" "))

    elif '"' in temp[1]:
        temparr = temp[1].strip(" ").strip('"')

    else:
        temparr = temp[1].strip(" ").split(" ")

    rulesdict[temp[0]] = temparr

    line = file.readline()

messagearr = []

line = file.readline()

while line != "\n":
    messagearr.append(line[:-1])
    line = file.readline()
    
#Part 1
def MakeRegex(rule = "0", prevrule = None, recursion = 0):
    rulecontent = rulesdict[rule]
    regex = ""

    if rule == prevrule:
        recursion += 1

    else:
        recursion = 0

    if recursion == 10:
        return ""
        
    if type(rulecontent) is str:
        return rulecontent

    else:
        if type(rulecontent[0]) is str:
            for subrule in rulecontent:
                regex += MakeRegex(subrule, rule, recursion)

        else:
            choice1 = rulecontent[0]
            choice2 = rulecontent[1]

            tempchoice1 = ""
            for subrule in choice1:
                tempchoice1 += MakeRegex(subrule, rule, recursion)

            choice1 = tempchoice1

            tempchoice2 = ""
            for subrule in choice2:
                tempchoice2 += MakeRegex(subrule, rule, recursion)

            choice2 = tempchoice2

            regex += "(?:"+choice1+"|"+choice2+")"
            
    return regex


def Part1():         
    regex = MakeRegex() 

    count = 0

    for message in messagearr:
        if re.fullmatch(re.compile(regex), message):
            count += 1

    print("Count:",count)


if __name__ == "__main__":
    print("Part 1")
    Part1()

#Part 2
rulesdict["8"] = [["42"],["42","8"]]
rulesdict["11"] = [["42", "31"],["42","11", "31"]]

def Part2():         
    regex = MakeRegex()

    count = 0

    for message in messagearr:
        if re.fullmatch(re.compile(regex), message):
            count += 1

    print("Count:",count)

if __name__ == "__main__":
    print("\nPart 2")
    Part2()
                
            
