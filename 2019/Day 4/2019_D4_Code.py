input = "245182-790572"

#Part 1
p1allowed = []
def Part1():
    count = 0
    lower,higher = input.split("-")

    for num in range(int(lower), int(higher) + 1):
        adjflag = False
        incflag = True

        for digit_i in range(len(str(num))-1):
            if str(num)[digit_i] == str(num)[digit_i + 1]:
                adjflag = True

            if str(num)[digit_i] > str(num)[digit_i + 1]:
                incflag = False
                break

        if adjflag and incflag:
            count += 1
            p1allowed.append(num)

    print("Passwords:", count)

#Part 2
def Part2():
    count = 0

    for num in p1allowed:
        valid = False
        numsplit = []
        section = ""

        digit_i = 0
        while digit_i < len(str(num)):
            if len(section) == 0:
                section += str(num)[digit_i]
                digit_i += 1

            elif str(num)[digit_i] in section:
                section += str(num)[digit_i]
                digit_i += 1

            else:
                numsplit.append(section)
                section = ""

        numsplit.append(section)

        for sect in numsplit:
            if len(sect) == 2:
                valid = True
                break

        if valid:
            count += 1

    print("Passwords:", count)


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
