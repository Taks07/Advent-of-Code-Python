file = open("Input.txt", "r")

departuretime = int(file.readline()[:-1])
schedule = []

for busid in file.readline().split(","):
    schedule.append(busid)

schedule = [[i,int(d)] for i,d in enumerate(schedule) if d != "x"]

file.close()

#Part 1
def Part1():
    correctbusid = schedule[0][1]
    for _,thisbusid in schedule:
        if thisbusid != "x":
            if (thisbusid * (departuretime//thisbusid + 1)) < (correctbusid * (departuretime//correctbusid + 1)):
                correctbusid = thisbusid
            
    print("Answer:", correctbusid * (correctbusid * (departuretime//correctbusid + 1) - departuretime))

#Part 2
def Part2():
    time = 0
    jump = schedule[0][1]

    for diff, busid in schedule[1:]:
        while (time + diff) % busid != 0:
            time += jump

        jump *= busid
    print("Answer:", time)
        


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
    
        
