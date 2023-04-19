import copy, sys

file = open("Input.txt", "r")
inputarr = []

for line in file:
    instruction = line.split(" ")
    operand, value = instruction[0], int(instruction[1].strip("\n"))
    inputarr.append([operand, value])

file.close()

#Part 1
acc = 0
pos = 0
executed = []

def ExecuteCode1(operand, value):
    global acc, pos, executed
    executed.append(pos)
        
    if operand == "jmp":
        pos += value

    else:
        if operand == "acc":
            acc += value

        pos += 1

    if pos not in executed:
        ExecuteCode1(inputarr[pos][0], inputarr[pos][1])

def Part1():
    ExecuteCode1(inputarr[0][0], inputarr[0][1])
    print("Accumulator:", acc)

#Part 2
acc = 0
pos = 0
executed = []
save = {"acc": "", "pos": "", "executed": []}

changed = []

def ExecuteCode2(operand, value, altered):
    global acc, pos, executed, save

    if operand == "acc":
        acc += value
        executed.append(pos)
        pos += 1

    elif operand == "jmp":
        if not altered and pos not in changed:
            save["acc"] = acc
            save["pos"] = pos
            save["executed"] = [x for x in executed]

            ExecuteCode2("nop", value, True)

        else:   
            executed.append(pos)
            pos += value

    else:
        if not altered and pos not in changed:
            save["acc"] = acc
            save["pos"] = pos
            save["executed"] = [x for x in executed]

            ExecuteCode2("jmp", value, True)

        else:    
            executed.append(pos)
            pos += 1

    if pos not in executed:
        try:
            ExecuteCode2(inputarr[pos][0], inputarr[pos][1], altered)

        except IndexError:
            return

    else:
        acc = save["acc"]
        pos = save["pos"]
        executed = [x for x in save["executed"]]
        changed.append(pos)

        ExecuteCode2(inputarr[pos][0], inputarr[pos][1], False)
                
            
def Part2():
    ExecuteCode2(inputarr[0][0], inputarr[0][1], False)
    print("Accumulator:", acc)
    
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    sys.setrecursionlimit(1000000)
    Part2() #For Part 2 to work, comment out Part1(). If not, memory error: stack overflow => not enough RAM.
