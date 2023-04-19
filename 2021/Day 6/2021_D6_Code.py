with open("Input.txt", 'r') as file:
    lanternfish = list(map(int,file.readline().split(",")))

def Simulate(numdays):
    days = [0 for i in range(9)]  # The number of fish on that particular day of gestation period

    for fish in lanternfish:
        days[fish] += 1

    for i in range(numdays):
        fishtoday = days.pop(0)
        days.append(fishtoday)
        days[6] += fishtoday

    print("Answer:", sum(days))


if __name__ == "__main__":
    print("Part 1")
    Simulate(80)

    print("Part 2")
    Simulate(256)