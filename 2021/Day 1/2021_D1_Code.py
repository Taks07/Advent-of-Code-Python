file = open("Input.txt", 'r')

depths = []

for line in file:
    depths.append(int(line))


def Part1():
    prev = 1000000000
    counter = 0
    for depth in depths:
        if depth > prev:
            counter += 1

        prev = depth

    print("Answer:", counter)

def Part2():
    prev = 1000000000000000000
    counter = 0

    offset = 0
    while (offset + 2) < len(depths):
        tempsum = 0

        for i in range(3):
            tempsum += depths[offset + i]


        if tempsum > prev:
            counter += 1

        prev = tempsum

        offset += 1

    print("Answer:", counter)


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()

