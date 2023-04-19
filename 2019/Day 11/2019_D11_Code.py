import copy

class IntCode():
    def __init__(self, start):
        self.index = 0
        self.mempointer = 0

        self.hull = {(0,0) : start}
        self.paintFlag = True
        self.painterCoords = [[0,0],"N"]
        self.paintedCount = 0

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

                try:
                    num1 = int(self.memory[self.GetNum(currmodes.pop(0))])

                except KeyError:
                    num1 = 0

                try:
                    num2 = int(self.memory[self.GetNum(currmodes.pop(0))])

                except KeyError:
                    num2 = 0

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

                if tuple(self.painterCoords[0]) not in self.hull.keys():
                    currIn = 0

                else:
                    tempDict = {".": 0, "#": 1}
                    currIn = tempDict[self.hull[tuple(self.painterCoords[0])]]

                self.memory[int(self.GetNum(mode))] = currIn
                self.mempointer += 1

            elif int(currop) == 4: #Output instruction
                if len(self.memory[self.mempointer]) == 3:
                    mode = int(self.memory[self.mempointer][0])

                else:
                    mode = 0

                currout = int(self.memory[self.GetNum(mode)])

                if self.paintFlag:
                    if tuple(self.painterCoords[0]) not in self.hull.keys():
                        self.paintedCount += 1

                    if currout == 0:
                        colour = "." #black

                    else:
                        colour = "#" #white


                    self.hull[tuple(self.painterCoords[0])] = colour

                    self.paintFlag = False

                else:
                    dictDeltaCoords = {"N": (1,0), "E": (0,1), "W": (0,-1), "S": (-1,0)}
                    dictChangeDirection = {"N": ("W","E"), "E": ("N","S"), "W": ("S","N"), "S": ("E","W")}

                    if currout == 0:
                        self.painterCoords[0][0] -= dictDeltaCoords[self.painterCoords[1]][0]
                        self.painterCoords[0][1] -= dictDeltaCoords[self.painterCoords[1]][1]

                    else:
                        self.painterCoords[0][0] += dictDeltaCoords[self.painterCoords[1]][0]
                        self.painterCoords[0][1] += dictDeltaCoords[self.painterCoords[1]][1]

                    self.painterCoords[1] = dictChangeDirection[self.painterCoords[1]][currout]

                    self.paintFlag = True


                self.mempointer += 1

            elif int(currop) == 9: #Add to index instruction
                if len(self.memory[self.mempointer]) == 3:
                    mode = int(self.memory[self.mempointer][0])

                else:
                    mode = 0

                self.index += int(self.memory[self.GetNum(mode)])
                self.mempointer += 1


            elif int(currop) == 99: #End program
                return self.paintedCount

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

    def Ranges(self):
        xRange = [0,0]
        yRange = [0,0]

        for coords in self.hull.keys():
            if coords[0] < xRange[0]:
                xRange[0] = coords[0]

            elif coords[0] > xRange[1]:
                xRange[1] = coords[0]

            if coords[1] < yRange[0]:
                yRange[0] = coords[1]

            elif coords[1] > yRange[1]:
                yRange[1] = coords[1]

        return xRange, yRange

    def Draw(self, scale = 10):

        import tkinter
        xRange, yRange = self.Ranges()

        wide = xRange[1] - xRange[0] + 1
        tall = yRange[1] - yRange[0] + 1

        root = tkinter.Tk()
        root.attributes('-topmost', True)

        can = tkinter.Canvas(root, width=wide * scale, height=tall * scale)

        can.pack()

        for rownum in range(yRange[0], yRange[1] + 1):
            for pixelnum in range(xRange[0], xRange[1] + 1):
                if (pixelnum, rownum) not in self.hull:
                    colour = "black"

                elif self.hull[(pixelnum,rownum)] == ".":
                    colour = "black"

                else:
                    colour = "white"

                can.create_rectangle(pixelnum * scale, rownum * scale, (pixelnum * scale) + scale, (rownum * scale) + scale, fill=colour, outline=colour)

        root.mainloop()


if __name__ == "__main__":
    comp = IntCode(".")

    print("Part 1")
    print("Answer:", comp.RunProgram())

    comp = IntCode("#")
    comp.RunProgram()
    comp.Draw()