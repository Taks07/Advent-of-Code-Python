import copy

with open("Input.txt", 'r') as file:
    inputdict = {}

    for line in file:
        patterns, output = line[:-1].split("|")
        patterns = patterns.strip().split(" ")
        output = output.strip().split(" ")

        inputdict[tuple(patterns)] = tuple(output)

def Part1():
    count = 0
    for output in inputdict.values():
        for num in output:
            if len(num) in (2,3,4,7):
                count += 1

    print("Answer:", count)

def FindOutputNum(pattern, output):
    numbers = {}

    for pat in pattern: #find 1,7,4 & 8
        temp = {2:1, 3:7, 4:4, 7:8}

        if len(pat) in (2,3,4,7):
            numbers[pat] = temp[len(pat)]
    pattern = [pat for pat in pattern if pat not in numbers.keys()]

    for pat in pattern: #find 3
        if len(pat) == 5 and set(list(numbers.keys())[list(numbers.values()).index(1)]).issubset(set(pat)):
            numbers[pat] = 3

    for pat in pattern: #find 9
        if len(pat) == 6 and set(list(numbers.keys())[list(numbers.values()).index(3)]).issubset(set(pat)):
            numbers[pat] = 9

    pattern = [pat for pat in pattern if pat not in numbers.keys()]

    for pat in pattern: # Find 0 & 6
        if len(pat) == 6:
            if set(list(numbers.keys())[list(numbers.values()).index(7)]).issubset(set(pat)):
                numbers[pat] = 0

            else:
                numbers[pat] = 6
    pattern = [pat for pat in pattern if pat not in numbers.keys()]

    for pat in pattern: #Find 2 & 5
        if set(pat).issubset(list(numbers.keys())[list(numbers.values()).index(6)]):
            numbers[pat] = 5

        else:
            numbers[pat] = 2

    num = ""

    for out in output:
        for pat in numbers:
            if set(out) == set(pat):
                num += str(numbers[pat])
                break

    return int(num)


def Part2():
    sum = 0
    for pattern in inputdict:
        sum += FindOutputNum(pattern, inputdict[pattern])

    print("Answer:", sum)


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
