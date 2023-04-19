import copy
#Read from file
file = open("Input.txt", 'r')
instructionsarr = file.readline().split(",")
file.close()

memory = {}
for i in range(len(instructionsarr)):
    memory[i] = int(instructionsarr[i])

memorybackup = copy.deepcopy(memory)
#Part 1
def RunProgram():
    global memory
    inspointer = 0
    while 1:
        if memory[inspointer] == 1:
            num1 = memory[memory[inspointer + 1]]
            num2 = memory[memory[inspointer + 2]]
            memory[memory[inspointer + 3]] = num1 + num2

            inspointer += 4

        elif memory[inspointer] == 2:
            num1 = memory[memory[inspointer + 1]]
            num2 = memory[memory[inspointer + 2]]
            memory[memory[inspointer + 3]] = num1 * num2

            inspointer += 4

        elif memory[inspointer] == 99:
            inspointer += 1
            return memory[0]

def Part1():
    print("Value at position 0:", RunProgram())

#Part 2
def Part2():
    global memory
    for noun in range(100):
        for verb in range(100):
            memory = copy.deepcopy(memorybackup)

            memory[1] = noun
            memory[2] = verb

            if RunProgram() == 19690720:
                print("Value:",  100 * noun + verb)
                return


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()

