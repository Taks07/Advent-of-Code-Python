file = open("Input.txt", "r")
inputarr = []

for line in file:
    inputarr.append(line[:-1])

inputarr = [int(x) for x in inputarr]
inputarr.append(0)
inputarr.append(max(inputarr) + 3)
sortedlist = sorted(inputarr)

file.close()

#Part 1
def Part1():
    count1 = 0
    count3 = 0

    for i in range(len(inputarr)-1):
        if sortedlist[i+1] - sortedlist[i] == 1:
            count1 += 1

        elif sortedlist[i+1] - sortedlist[i] == 3:
            count3 += 1

    print("Answer:", count1*count3)

#Part 2
def ValidCombos():
    validcombdict = {}

    for i in range(len(inputarr) - 1):
        numcomb = []
        for j in range(1,4):
            try:
                if sortedlist[i + j] - sortedlist[i] in (1, 2, 3):            
                    numcomb.append([sortedlist[i], sortedlist[i + j]])

            except IndexError:
                break
        validcombdict[sortedlist[i]] = numcomb
        
    return validcombdict

combdict = ValidCombos()

def memoize(func): #memoization decorator
    cache = {}

    def memoized_func(*args): #wrapper
        if args in cache:
            return(cache[args])

        result = func(*args)
        cache[args] = result
        return result
    return memoized_func

@memoize
def Count(num):
    count = 0
    global combdict
    while len(combdict[num]) == 1:
        num = combdict[num][0][1]

        if num == sortedlist[-1]:
            return count


    count += len(combdict[num])-1

   
    for x, y in combdict[num]:
        count += Count(y)
    return count

    

def Part2():
    global combdict
    counter = Count(0)
    print("Answer:", counter + 1)
          

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
    
    
