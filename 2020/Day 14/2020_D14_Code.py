import re
file = open("Input.txt")

line = file.readline()
inputdict = {}

while len(line) != 0:
    if line[0:4] == "mask":
        mask = line[7:-1]
        instructions = []

        line = file.readline()

        while line[0:3] == "mem" and len(line) != 0:
            vals = re.compile(r"mem\[(\d+)\] = (\d+)").findall(line)
            instructions.append(vals[0])

            line = file.readline()

        inputdict[mask] = instructions
            
        
#Part 1
def CreateANDMask(mask): #To set bit in specific position to 0
    returnval = ""
    for char in mask:
        if char == "0":
            returnval += "0"

        else:
            returnval += "1"
    return int(returnval, 2)

def CreateORMask(mask):
    returnval = ""
    for char in mask:
        if char == "1":
            returnval += "1"

        else:
            returnval += "0"
    return int(returnval, 2)

def Part1():
    memdict = {}
    for mask in inputdict:
        ANDMask = CreateANDMask(mask)
        ORMask = CreateORMask(mask)


        for address, value in inputdict[mask]:
            value = int(value) & ANDMask
            value = value | ORMask
            memdict[address] = value

    total = 0
    for val in memdict.values():
        total += val

    print("Sum:", total)

#Part 2
def CalculateAddresses(mask, address):
    address = bin(int(address))[2:].zfill(36)
    newaddress = ""
    for i in range(len(mask)):
        if mask[i] == "0":
            newaddress += address[i]

        elif mask[i] == "1":
            newaddress += "1"

        else:
            newaddress += "X"


            
    numX = newaddress.count("X")
    permutations = []

    for permutation in range(2 ** numX):        
        permutations.append(bin(permutation)[2:].zfill(numX))

    addresslist = []
    for permutation in permutations:
        tempaddress = ""
        for char in newaddress:
            if char == "X":
                tempaddress += permutation[0]
                permutation = permutation[1:]

            else:
                tempaddress += char

        addresslist.append(int(tempaddress,2))
    return addresslist
            
            

def Part2():
    memdict = {}

    for mask in inputdict:
        for address, value in inputdict[mask]:
            possaddress = CalculateAddresses(mask, address) #Return list of addresses

            for add in possaddress:
                memdict[add] = int(value)

    total = 0
    for val in memdict.values():
        total += val

    print("Sum:", total)
                
        
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()

        
        
