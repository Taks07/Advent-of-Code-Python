import copy, functools

with open("Input.txt",'r') as file:
    instructions = []

    for line in file:
        instructions.append(line[:-1].split(" "))

def isnum(s):
    try:
        float(s)

    except:
        return False

    else:
        return True

def Run(num):
    variables = {"w" : 0, "x" : 0, "y" : 0, "z" : 0}

    for ins, *parameter in instructions:
        if ins == "inp":
            variables[temp[parameter[0]]] = num.pop(0)

        else:
            if isnum(parameter[1]):
                par2 = int(parameter[1])

            else:
                par2 = int(variables[temp[parameter[1]]])

            if ins == "add":
                variables[temp[parameter[0]]] =  str(int(variables[temp[parameter[0]]]) + par2)

            elif ins == "mul":
                variables[temp[parameter[0]]] =  str(int(variables[temp[parameter[0]]]) * par2)

            elif ins == "div":
                variables[temp[parameter[0]]] = str(int(variables[temp[parameter[0]]]) // par2)

            elif ins == "mod":
                variables[temp[parameter[0]]] = str(int(variables[temp[parameter[0]]]) % par2)

            else:
                variables[temp[parameter[0]]] = str(int(int(variables[temp[parameter[0]]]) == par2))

    return variables["z"]

#Naive implementation, takes days to run
def Part1Bad():
    for i in range(99999999999999,-1,-1):
        if "0" in str(i):
            continue

        if int(Run(list(str(i)))) == 0:
            print("Answer:",i)
            break

# By manually decompiling the input, the following conditions must be met for a 14 digit number I where I[n] is the nth digit of I:
# I[1] - 2 = I[14]
# I[2] + 3 = I[13]
# I[3] + 7 = I[12]
# I[10] + 5 = I[11]
# I[4] - 5 = I[9]
# I[7] - 3 = I[8]
# I[5] - 1 = I[6]

#The input can be broken into 14 similar blocks, one for each digit in I. In the block, w holds I[n], x & y are reset to 0 and z is the only variable carried between blocks
#In each block the format is:

#inp w
#mul x 0
#add x z
#mod x 26
#div z {A}
#add x {B}
#eql x w
#eql x 0
#mul y 0
#add y 25
#mul y x
#add y 1
#mul z y
#mul y 0
#add y w
#add y {C}
#mul y x
#add z y

#Where A, B and C varies. A only changes between 1 and 26.

#When A == 1, (z%26) + B == I[n] is checked. If True, nothing happens to z. However, looking at the input, the value of B is always above 10.
#Thus this condition is always False. If False, z *= 26 and then z += I[n] + C

#When A is 26, you're essentially only getting the last I[n] + C stored in Z. This is because z has the format M(26) + I[last_n] + C1.
#So, modulusing z filters out the M(26). Thus the condition checked is I[last_n] + C1 + B == I[curr_n].

#If this is True, z //= 26. This essentially removes I[last_n] + C1 from z as I[last_n] + C1 equals a value of I[n] and 0 < I[n] < 10.
#So it is rounded down by integer dividing. It also has the affect of "unlocking" the previous I[n] + C => z = M(26) + I[n_prev] + C_prev
#We know that I[last_n] + C1 is removed. Also, z = M(26) and M(26) = 26(I[n1] + C1 + 26(I[n2] + C2 + M(26)...). So, if dividing by 0, I[n1] + C1 is "released"

#If this is False, z += I[n] + C. Looking at the code, there are 7 {A} = 1 and 7 {A} = 26. We cannot allow this condition to be False as z *= 26 7 times.
#So, we need all these conditions to be True so we can conteract the growth of z. Even having the condition be wrong once means that z = I[n] + C at the end. i.e. not 0

# Part 1
# By prioritizing maximizing I[n] for the smaller n in each condition, you get the largest number: 96299896449997

# Part 2 can then be solved by minimizing I[n] instead

def ValidNums():
    #Gives all valid numbers in I array
    for I14 in range(1,8):
        for I2 in range(1,7):
            for I3 in range(1,3):
                for I10 in range(1,5):
                    for I9 in range(1,5):
                        for I8 in range(1,7):
                            for I6 in range(1,9):
                                I = [None for i in range(14)]

                                I[13] = I14
                                I[1] = I2
                                I[2] = I3
                                I[9] = I10
                                I[8] = I9
                                I[7] = I8
                                I[5] = I6

                                I[0] = I14 + 2
                                I[12] = I2 + 3
                                I[11] = I3 + 7
                                I[10] = I10 + 5
                                I[3] = I9 + 5
                                I[6] = I8 + 3
                                I[4] = I6 + 1

                                yield I

def Part1():
    print("Answer:", max([int("".join([str(i) for i in I])) for I in ValidNums()]))

def Part2():
    print("Answer:", min([int("".join([str(i) for i in I])) for I in ValidNums()]))

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()