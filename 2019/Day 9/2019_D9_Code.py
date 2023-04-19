import copy

class IntCode():
    def __init__(self):
        self.index = 0
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
            if int(currop) in (1, 2, 5, 6, 7, 8): #For instructions with 2 parameters and location
                currmodes = []

                for i in str(self.memory[self.mempointer])[:-2][::-1]:
                    currmodes.append(int(i))  # Gets parameter modes in order

                while len(currmodes) < 3:
                    currmodes.append(0)  # Adds any trailing zeros to parameter modes array

                num1 = int(self.memory[self.GetNum(currmodes.pop(0))])
                num2 = int(self.memory[self.GetNum(currmodes.pop(0))])

                if int(currop) in (1, 2, 7, 8):
                    setpointer = int(self.GetNum(currmodes.pop(0)))

                    if int(currop) == 1: #Add instruction
                        self.memory[setpointer] = str(num1 + num2)

                    elif int(currop) == 2:  #Multiply instruction
                        self.memory[setpointer] = str(num1 * num2)

                    elif int(currop) == 7: #Less than instruction
                        if num1 < num2:
                            self.memory[setpointer] = "1"

                        else:
                            self.memory[setpointer] = "0"

                    elif int(currop) == 8: #Equals instruction
                        if num1 == num2:
                            self.memory[setpointer] = "1"

                        else:
                            self.memory[setpointer] = "0"

                    self.mempointer += 1

                else:
                    self.mempointer += 1
                    if int(currop) == 5 and num1 != 0: #Jump if true instruction
                        self.mempointer = num2

                    elif int(currop) == 6 and num1 == 0: #Jump if false instruction
                        self.mempointer = num2

            elif int(currop) == 3: #Input instruction
                if len(self.memory[self.mempointer]) == 3:
                    mode = int(self.memory[self.mempointer][0])

                else:
                    mode = 0

                self.memory[int(self.GetNum(mode))] = input("Enter a number: ")
                self.mempointer += 1

            elif int(currop) == 4: #Output instruction
                if len(self.memory[self.mempointer]) == 3:
                    mode = int(self.memory[self.mempointer][0])

                else:
                    mode = 0

                print(self.memory[self.GetNum(mode)])
                self.mempointer += 1

            elif int(currop) == 9: #Add to index instruction
                if len(self.memory[self.mempointer]) == 3:
                    mode = int(self.memory[self.mempointer][0])

                else:
                    mode = 0

                self.index += int(self.memory[self.GetNum(mode)])
                self.mempointer += 1


            elif int(currop) == 99: #End program
                return

    def GetNum(self, mode):
        self.mempointer += 1

        try:
            if mode == 0:  # Pos mode
                return int(self.memory[self.mempointer])

            elif mode == 1:  # Immediate mode
                return self.mempointer

            elif mode == 2: #Relative mode
                return int(self.memory[self.mempointer]) + self.index

        except KeyError:
            return 0

    def Reset(self):
        self.mempointer = 0
        self.memory = copy.deepcopy(self.memorybackup)

if __name__ == "__main__":
    comp = IntCode()

    print("Part 1")
    comp.RunProgram()
