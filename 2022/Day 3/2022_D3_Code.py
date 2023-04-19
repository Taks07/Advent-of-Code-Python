with open("Input.txt", 'r') as file:
    rucksacks = []
    for line in file:
        half = len(line)//2
        rucksack = [set(line[:half]), set(line[half:-1])]
        rucksacks.append(rucksack)

def ConvertPriority(letter):
    if letter >= 'a' and letter <= 'z':
        return ord(letter) - 96

    else:
        return ord(letter) - 38


def Part1():
    sum = 0
    for rucksack in rucksacks:
        sum += ConvertPriority(list(rucksack[0] & rucksack[1])[0])

    print("Ans:", sum)

def Part2():
    sum = 0
    for group in groups:
        sum += ConvertPriority(list(group[0] & group[1] & group[2])[0])

    print("Ans:", sum)


if __name__ == "__main__":
    print("Part 1")
    Part1()

    with open("Input.txt", 'r') as file:
        groups = []

        line = file.readline()[:-1]

        while len(line) > 0:
            group = []
            for i in range(3):
                group.append(set(line))
                line = file.readline()[:-1]

            groups.append(group)

    print("Part 2")
    Part2()







