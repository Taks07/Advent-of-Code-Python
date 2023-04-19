with open("Input.txt", 'r') as file:
    sumcal = 0
    calories = []

    for line in file:
        if len(line) == 1:
            calories.append(sumcal)
            sumcal = 0

        else:
            sumcal += int(line)

calories = sorted(calories, reverse=True)

def Part1():
    print("Ans:", max(calories))

def Part2():
    print("Ans:", sum(calories[0:3]))


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()





