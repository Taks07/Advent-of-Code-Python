file = open("Input.txt", "r")

wires = []
for line in file:
    wires.append(line.split(","))
file.close()

#Part 1
panel = {"0 0":"O"}
intersections = {}

def Part1():
    for wire in wires:
        x = 0
        y = 0
        currwire = []

        for instruction in wire:
            dx = 0
            dy = 0
            s = ""

            if instruction[0] == "R":
                dx = 1
                s = "-"

            elif instruction[0] == "L":
                dx = -1
                s = "-"

            elif instruction[0] == "U":
                dy = 1
                s = "|"

            else:
                dy = -1
                s = "|"

            for i in range(int(instruction[1:])):
                x += dx
                y += dy
                key = str(x) + " " + str(y)

                if key in panel.keys() and key not in currwire:
                    panel[key] = "+"
                    intersections[key] = 0

                else:
                  panel[key] = s

                currwire.append(key)

    distances = []
    for key, val in panel.items():
        if val == "+":
            x, y = key.split(" ")
            x = abs(int(x))
            y = abs(int(y))

            distance = x + y
            distances.append(distance)

    print("Smallest Distance:", min(distances))

#Part 2
def Part2():
    for wire in wires:
        x = 0
        y = 0
        steps = 0
        for instruction in wire:
            dx = 0
            dy = 0

            if instruction[0] == "R":
                dx = 1

            elif instruction[0] == "L":
                dx = -1

            elif instruction[0] == "U":
                dy = 1

            else:
                dy = -1

            for i in range(int(instruction[1:])):
                x += dx
                y += dy
                steps += 1
                key = str(x) + " " + str(y)

                if key in intersections.keys():
                    intersections[key] += steps

    print("Minimum Distance:", min(intersections.values()))


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()




