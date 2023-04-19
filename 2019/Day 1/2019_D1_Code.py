
file = open("Input.txt", 'r')

modulesmass = []
for line in file:
    modulesmass.append(int(line))

file.close()

#Part 1
def Part1():
    sum = 0

    for module in modulesmass:
        sum += ((module//3)-2)

    print("Sum of Fuel Requirements:", sum)

#Part 2
def Part2():
    sum = 0

    for module in modulesmass:
        currfuel = ((module // 3) - 2)

        while currfuel > 0:
            sum += currfuel
            currfuel = ((currfuel // 3) - 2)

    print("Sum of Fuel Requirements:", sum)

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()