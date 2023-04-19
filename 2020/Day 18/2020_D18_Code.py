def ConvertString(string):
    arraystring = []
    i = 0

    while i != len(string): 
        if string[i] != " ":
            if string[i] == "(":
                leftbracket = 1
                rightbracket = 0
                insidestring = ""

                while leftbracket != rightbracket:
                    i += 1

                    if string[i] != " ":
                        if string[i] == ")":
                            rightbracket += 1

                            if leftbracket != rightbracket:
                                insidestring += string[i]

                        else:
                            if string[i] == "(":
                                leftbracket +=1

                            insidestring += string[i]

                insertvalue = ConvertString(insidestring)

            else:
                insertvalue = string[i]

            arraystring.append(insertvalue)

        i += 1

    return arraystring

file = open("Input.txt", "r")
inputarr = []
for line in file:
    inputarr.append(ConvertString(line[:-1]))

file.close()
                    
#Part 1
def Equation(val1, val2, operator):
    if operator == "+":
        return (val1 + val2)

    else:
        return (val1 * val2)
    
def EvaluateArray(equation):
    while len(equation) != 1:
        value = 0
        val1, operator, val2 = equation.pop(0), equation.pop(0), equation.pop(0)

        if type(val1) is list:
            val1 = EvaluateArray(val1)

        if type(val2) is list:
            val2 = EvaluateArray(val2)

        value += Equation(int(val1), int(val2), operator)

        equation.insert(0, value)

    return equation[0]
    
def Part1():
    total = 0
    for equation in inputarr:
        total += EvaluateArray(equation)

    print("Total:", total)

if __name__ == "__main__":
    print("Part 1")
    Part1()

#Part 2
import copy
file = open("Input.txt", "r")
inputarr = []
for line in file:
    inputarr.append(ConvertString(line[:-1]))

file.close()

def AddPrecedence(equation):
    i = 0
    length = len(equation)
    
    while i < length:
        if type(equation[i]) is list:
            equation.insert(i, AddPrecedence(equation.pop(i)))
        
        if equation[i-1] == "+":
            val1 = equation.pop(i)
            operator = equation.pop(i-1)
            val2 = equation.pop(i-2)

            i -= 2
            equation.insert(i, [val2, operator, val1])
            length -= 2
        i+=1

    return equation

def EvaluateArray2(equation):
    while len(equation) == 1:
        equation = equation[0]
    
    while len(equation) != 1:
        value = 0
        val1, operator, val2 = equation.pop(0), equation.pop(0), equation.pop(0)

        if type(val1) is list:
            val1 = EvaluateArray2(val1)

        if type(val2) is list:
            val2 = EvaluateArray2(val2)

        value += Equation(int(val1), int(val2), operator)

        equation.insert(0, value)


    return equation[0]

def Part2():
    total = 0
    for eq in inputarr:
        total += EvaluateArray2(AddPrecedence(eq))

    print("Total:", total)

if __name__ == "__main__":
    print("\nPart 2")
    Part2()
        
            

        
            

        

        
        
        
