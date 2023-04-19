file = open("Input.txt", "r")
inputarr = []

for line in file:
    inputarr.append(int(line))
file.close()

#Part 1
def Part1():
    for val in inputarr:
        if (2020-val) in inputarr:
            print("Value 1:",val,
                  "\nValue 2:", 2020-val,
                  "\nAnswer:", (2020-val)*val)
            return

#Part 2       
def Part2():
    for val1 in inputarr:
        for val2 in inputarr:
            if (2020-val1-val2) in inputarr:
                print("Value 1:",val1,
                      "\nValue 2:", val2,
                      "\nValue 3:", 2020-val1-val2,
                      "\nAnswer:", (2020-val1-val2) * val1 * val2)
                return


if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
                      
                
        
