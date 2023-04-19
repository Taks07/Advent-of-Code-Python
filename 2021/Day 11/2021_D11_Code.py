import itertools


class Octopus():
    def __init__(self,power):
        self.power = power
        self.flashed = False
        self.checked = False

    def CheckFlash(self):
        if not self.checked:
            self.power += 1
            self.checked = True

        if not self.flashed and self.power > 9:
            self.power = 0
            self.flashed = True
            return True

        return False

    def ResetFlags(self):
        self.checked = False
        self.flashed = False


class Cavern():
    def __init__(self):
        self.numflash = 0

        with open("Input.txt", 'r') as file:
            self.octopi = []

            for line in file:
                row = []
                for power in line[:-1]:
                    row.append(Octopus(int(power)))

                self.octopi.append(row)

    def RunStep(self):
        stop = False

        while not stop:
            stop = True

            for row,line in enumerate(self.octopi):
                for col,octopus in enumerate(line):
                    if octopus.CheckFlash():
                        self.numflash += 1
                        stop = False

                        deltas = itertools.product((0,1,-1), repeat = 2)

                        for dcol,drow in deltas:
                            if -1 < row + drow < len(self.octopi) and -1 < col + dcol < len(self.octopi[0]) and not self.octopi[row+drow][col+dcol].flashed:
                                self.octopi[row+drow][col+dcol].power += 1

        for line in self.octopi:
            for octopus in line:
                octopus.ResetFlags()

    def CheckSimulataneous(self):
        for line in self.octopi:
            for octopus in line:
                if octopus.power != 0:
                    return False

        return True

    def Visualise(self):
        for line in self.octopi:
            for octopus in line:
                print(octopus.power, end = '')

            print("")

        print("")




def Part1():
    cavern = Cavern()

    for i in range(100):
        cavern.RunStep()

    print("Number of Flashes:", cavern.numflash)

def Part2():
    cavern = Cavern()

    stop = False
    i = 0

    while not stop:
        i += 1
        cavern.RunStep()

        stop = cavern.CheckSimulataneous()

    print("Turn:", i)





if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
