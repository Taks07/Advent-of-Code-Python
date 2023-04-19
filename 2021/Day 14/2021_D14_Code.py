import copy

with open("Input.txt", 'r') as file:
    template = file.readline()[:-1]
    file.readline()

    insertrules = {}
    for line in file:
        splitline = line[:-1].split(" -> ")
        insertrules[splitline[0]] = splitline[1]

templatedict = {}
for pair in insertrules:
    templatedict[pair] = 0

for i in range(len(template) - 1):
    if template[i:i+2] in templatedict:
        templatedict[template[i:i + 2]] += 1


def GrowPolymer():
    copydict = copy.deepcopy(templatedict)

    for pair in templatedict:
        if templatedict[pair] != 0:
            insert = insertrules[pair]

            copydict[pair[0] + insert] += templatedict[pair]
            copydict[insert + pair[1]] += templatedict[pair]
            copydict[pair] -= templatedict[pair]

    return copydict

def Answer(rounds):
    global templatedict
    for i in range(rounds):
        templatedict = GrowPolymer()

    symbols = {}

    for val in insertrules.values():
        symbols[val] = 0

    for pair in templatedict:
        symbols[pair[0]] += templatedict[pair]
        symbols[pair[1]] += templatedict[pair]

    symbols = [int(i/2) for i in symbols.values()]
    print("Answer:", max(symbols) - min(symbols) + 1)

    for pair in insertrules:
        templatedict[pair] = 0

    for i in range(len(template) - 1):
        if template[i:i + 2] in templatedict:
            templatedict[template[i:i + 2]] += 1

if __name__ == "__main__":
    print("Part 1")
    Answer(10)

    print("\nPart 2")
    Answer(40)