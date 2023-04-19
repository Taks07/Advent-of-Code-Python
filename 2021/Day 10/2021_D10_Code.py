import copy

with open("Input.txt", 'r') as file:
    lines = []

    for line in file:
        lines.append(line[:-1])

def Part1():
    copylines = copy.deepcopy(lines)
    illegalchars = {")" : [0,3], "]" : [0,57], "}" : [0,1197], ">" : [0,25137]}

    dict = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}

    for line in copylines:
        corrupted = False
        closing = []

        for symbol in line:
            if symbol in dict.keys():
                closing.append(dict[symbol])

            else:
                if closing.pop() != symbol:
                    illegalchars[symbol][0] += 1
                    corrupted = True

        if corrupted:
            lines.remove(line)


    errorscore = 0
    for count, score in illegalchars.values():
        errorscore += count * score

    print("Total Error Score:", errorscore)

def Part2():
    scoresdict = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
    dict = {"(": ")", "[": "]", "{": "}", "<": ">"}
    linescores = []

    for line in lines:
        closing = []

        for symbol in line:
            if symbol in dict.keys():
                closing.append(dict[symbol])

            elif symbol == closing[-1]:
                closing.pop()

        totalscore = 0
        for symbol in closing[::-1]:
            totalscore *= 5
            totalscore += scoresdict[symbol]

        linescores.append(totalscore)

    linescores = sorted(linescores)

    print("Middle Score:", linescores[int(len(linescores)/2)])

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()