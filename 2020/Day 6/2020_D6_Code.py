file = open("Input.txt", "r")
inputarr = []

string = ""
people = 0

for line in file:
    if line == "\n":
        inputarr.append([string, people])
        string = ""
        people = 0

    else:
        string = string + line[:-1]
        people += 1
        
file.close()

#Part 1
def Part1():   
    totalcount = 0

    for answers in inputarr:
        groupcount = 0
        alphabetlist = []
        
        for yes in answers[0]:
            if yes not in alphabetlist:
                alphabetlist.append(yes)
                groupcount += 1

        totalcount += groupcount


    print("Sum of Counts:", totalcount)

#Part 2
def Part2():
    totalcount = 0

    for answers in inputarr:
        groupcount = 0
        alphabetlist = []

        for yes in answers[0]:
            if yes not in alphabetlist:
                alphabetlist.append(yes)

                if answers[0].count(yes) == answers[1]:
                    groupcount += 1

        totalcount += groupcount

    print("Sum of Counts:", totalcount)

    

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart2")
    Part2()
