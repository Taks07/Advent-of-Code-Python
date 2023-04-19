import copy


class IntCode():
    def __init__(self):
        self.mempointer = 0
        file = open("Input.txt", 'r')
        instructionsarr = file.readline().split(",")
        file.close()

        self.memory = {}
        for i in range(len(instructionsarr)):
            self.memory[i] = instructionsarr[i]

        self.memorybackup = copy.deepcopy(self.memory)

    def RunProgram(self):
        while 1:
            currop = self.memory[self.mempointer][-2:]  # Gets opcode of curr instruction (at mempointer index)
            if int(currop) in (1, 2, 5, 6, 7, 8):
                currmodes = []

                for i in str(self.memory[self.mempointer])[:-2][::-1]:
                    currmodes.append(int(i))  # Gets parameter modes in order

                while len(currmodes) < 2:
                    currmodes.append(0)  # Adds any trailing zeros to modes array

                num1 = self.GetNum(currmodes.pop(0))
                num2 = self.GetNum(currmodes.pop(0))

                self.mempointer += 1  # Index now at position to put result

                if int(currop) in (1, 2, 7, 8):
                    if int(currop) == 1:
                        self.memory[int(self.memory[self.mempointer])] = str(num1 + num2)

                    elif int(currop) == 2:
                        self.memory[int(self.memory[self.mempointer])] = str(num1 * num2)

                    elif int(currop) == 7:
                        if num1 < num2:
                            self.memory[int(self.memory[self.mempointer])] = "1"

                        else:
                            self.memory[int(self.memory[self.mempointer])] = "0"

                    elif int(currop) == 8:
                        if num1 == num2:
                            self.memory[int(self.memory[self.mempointer])] = "1"

                        else:
                            self.memory[int(self.memory[self.mempointer])] = "0"

                    self.mempointer += 1

                else:
                    if int(currop) == 5 and num1 != 0:
                        self.mempointer = num2

                    elif int(currop) == 6 and num1 == 0:
                        self.mempointer = num2

            elif int(currop) == 3:
                self.mempointer += 1
                self.memory[int(self.memory[self.mempointer])] = input("Enter a number: ")
                self.mempointer += 1

            elif int(currop) == 4:
                if len(self.memory[self.mempointer]) == 3:
                    mode = int(self.memory[self.mempointer][0])

                else:
                    mode = 0

                print(self.GetNum(mode))
                self.mempointer += 1

            elif int(currop) == 99:
                return

    def GetNum(self, mode):
        self.mempointer += 1
        if mode == 0:  # Pos mode
            return int(self.memory[int(self.memory[self.mempointer])])

        elif mode == 1:  # Immediate mode
            return int(self.memory[self.mempointer])

    def Reset(self):
        self.mempointer = 0
        self.memory = copy.deepcopy(self.memorybackup)


if __name__ == "__main__":
    comp = IntCode()
    print("Part 1")
    comp.RunProgram()  # Input "1"

    print("\nPart 2")
    comp.Reset()
    comp.RunProgram()  # Input "5"
