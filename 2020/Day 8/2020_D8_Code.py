file = open("Input.txt", "r")
inputarr = []

for line in file:
    instruction = line.split(" ")
    opcode, operand = instruction[0], int(instruction[1].strip("\n"))
    inputarr.append([opcode, operand])

file.close()

#Part 1
def Part1():
    acc = 0
    pos = 0
    executed = []
    while True:
        opcode, operand = inputarr[pos][0], inputarr[pos][1]
        executed.append(pos)
            
        if opcode == "jmp":
            pos += operand

        else:
            if opcode == "acc":
                acc += operand

            pos += 1

        if pos in executed:
            break
    print("Accumulator:", acc)

#Part 2                   
def Part2():
    acc = 0
    pos = 0
    executed = []
    
    save = {"acc": "", "pos": "", "executed": []}

    changed = []
    altered = False
    
    while True:
        opcode, operand = inputarr[pos][0], inputarr[pos][1]
        if opcode == "acc":
            acc += operand
            executed.append(pos)
            pos += 1

        elif opcode == "jmp":
            if not altered and pos not in changed:
                save["acc"] = acc
                save["pos"] = pos
                save["executed"] = [x for x in executed]

                pos += 1
                altered = True

            else:   
                executed.append(pos)
                pos += operand

        else:
            if not altered and pos not in changed:
                save["acc"] = acc
                save["pos"] = pos
                save["executed"] = [x for x in executed]

                pos += operand
                altered = True

            else:    
                executed.append(pos)
                pos += 1

        try:
            inputarr[pos]

        except IndexError:
            break

        if pos in executed:
            acc = save["acc"]
            pos = save["pos"]
            executed = [x for x in save["executed"]]
            changed.append(pos)

            opcode, operand = inputarr[pos][0], inputarr[pos][1]
            altered = False
            
    print("Accumulator:", acc)
    
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2() 
