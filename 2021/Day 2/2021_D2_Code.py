instructions = []

with open("Input.txt",'r') as file:
    for line in file:
        instructions.append(tuple(line[:-1].split(" ")))

def Part1():
    pos = [0,0] #[horizontal, depth]

    for ins, val in instructions:
        if ins == "forward":
            pos[0] += int(val)

        elif ins == "down":
            pos[1] += int(val)

        else:
            pos[1] -= int(val)

    print("Answer:", pos[0]*pos[1])

def Part2():
    aim = 0
    pos = [0,0] #[horizontal, depth]

    for ins, val in instructions:
        if ins == "forward":
            pos[0] += int(val)
            pos[1] += aim * int(val)

        elif ins == "down":
            aim += int(val)

        else:
            aim -= int(val)

    print("Answer:", pos[0]*pos[1])

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()

