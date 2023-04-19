import re,itertools,copy,math

def LoadFile():
    file = open("Input.txt", 'r')

    global planets
    planets = []
    for i,line in enumerate(file):
        temp = []
        match = re.findall(r"\w=(-?\d*)", line)

        temp.append(i)
        temp.append([int(match[0]),int(match[1]),int(match[2])])
        temp.append([0,0,0])

        planets.append(temp)

    file.close()

def RunTurn1():
    copyplanets = copy.deepcopy(planets)

    for planet1, planet2 in itertools.combinations(copyplanets,2):
        for planet in planets:
            if planet[0] == planet1[0]:
                realplanet1 = planet

            elif planet[0] == planet2[0]:
                realplanet2 = planet

        for j in range(3):
            if planet1[1][j] > planet2[1][j]:
                realplanet1[2][j] -= 1
                realplanet2[2][j] += 1

            elif planet1[1][j] < planet2[1][j]:
                realplanet1[2][j] += 1
                realplanet2[2][j] -= 1

    for planet in planets:
        for i in range(3):
            planet[1][i] += planet[2][i]


def Part1():
    LoadFile()

    for i in range(1000):
        RunTurn1()

    systemtotal = 0

    for planet in planets:
        PE = 0
        KE = 0

        for i in range(3):
            PE += abs(planet[1][i])
            KE += abs(planet[2][i])

        systemtotal += PE * KE

    print("Total Energy:",systemtotal)

def LCM(a,b):
    return abs(a*b)//math.gcd(a,b)

def Part2():
    LoadFile()

    periods = []

    for i in range(3):
        count = 0
        original = [(planet[1][i],planet[2][i]) for planet in planets]

        while 1:
            copyplanets = copy.deepcopy(planets)
            for planet1, planet2 in itertools.combinations(copyplanets, 2):
                for planet in planets:
                    if planet[0] == planet1[0]:
                        realplanet1 = planet

                    elif planet[0] == planet2[0]:
                        realplanet2 = planet

                if planet1[1][i] > planet2[1][i]:
                    realplanet1[2][i] -= 1
                    realplanet2[2][i] += 1

                elif planet1[1][i] < planet2[1][i]:
                    realplanet1[2][i] += 1
                    realplanet2[2][i] -= 1

            for planet in planets:
                planet[1][i] += planet[2][i]

            count += 1
            temp = [(planet[1][i],planet[2][i]) for planet in planets]

            if original == temp:
                periods.append(count)
                break

    print("Answer:",LCM(LCM(periods[0],periods[1]),periods[2]))






if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("Part 2")
    Part2()