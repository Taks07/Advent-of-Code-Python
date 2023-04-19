file = open("Input.txt", "r")
inputarr = []

for line in file:
    inputarr.append(int(line[:-1]))

file.close()

#Part 1
def Part1():
    for i in range(25,len(inputarr)):
        end = True
        
        for val in inputarr[i-25:i]:
            if (inputarr[i] - val) in inputarr[i-25:i-1]:
                end = False

        if end:
            print("Value:", inputarr[i])
            return inputarr[i]

#Part 2
def Part2(sumval):
    for i in range(len(inputarr)):
        numlist = []
        pointer = i

        while sum(numlist) < sumval:
            numlist.append(inputarr[pointer])
            pointer += 1

        if sum(numlist) == sumval:
            print("Answer:", max(numlist) + min(numlist))
            break
  

    
if __name__ == "__main__":
    print("Part 1")
    part2input = Part1()

    print("\nPart 2")
    Part2(part2input)

                
                
                
            
        
