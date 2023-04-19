import copy
inputcups = "538914762"
cups = [int(x) for x in inputcups]

#Part 1
currindex = 0
mincup = min(cups)
maxcup = max(cups)

def Move():
    global cups, currindex
    currcup = copy.deepcopy(cups[currindex])
    pickedup = []

    for i in range(currindex + 1, currindex + 4):
        if i < len(inputcups):
            pickedup.append(copy.deepcopy(cups[i]))

        else:
            pickedup.append(copy.deepcopy(cups[i-len(inputcups)]))

    cups = [x for x in cups if x not in pickedup]

    destcup = currcup - 1
    while destcup not in cups:
        destcup -= 1

        if destcup < mincup:
            destcup = maxcup

    destindex = cups.index(destcup)

    for cup in pickedup[::-1]:
        cups.insert(destindex + 1, copy.deepcopy(cup))

    currindex = cups.index(currcup) + 1

    if currindex == len(cups):
        currindex -= len(cups)

def Part1():
    for _ in range(100):
        Move()

    ind = cups.index(1)

    order = ""
    for i in range(ind + 1, len(cups) + ind):
        if i >= len(cups):
            order += str(cups[i-len(cups)])

        else:
            order += str(cups[i])

    print("Answer:", order)


if __name__ == "__main__":
    pass
    #print("Part 1")
    #Part1()

    
#Part 2
inputcups = "538914762"
cups = [int(x) for x in inputcups] + list(range(10, 1000001))
cupdict = {}

currindex = 0

class Node():
    def __init__(self, value = 0, nextnode = None):
        self.next = nextnode
        self.value = value

def SetUpNodes():
    for i in range(1, len(cups)+1): #Lookup dict for cup node according to value
        cupdict[i] = Node(i)

    for i in range(len(cups)): #According to order in cups array, link nodes together
        cupdict[cups[i]].next = cupdict[cups[(i+1)%len(cupdict)]] #Modulus so the linked list loops

def Part2():
    SetUpNodes()

    currcup = cupdict[cups[0]] 
    
    for i in range(10000000):
        pickedup = currcup.next 
        currcup.next = currcup.next.next.next.next #Link curr cup to next node after the 3 after it are removed

        destcupval = currcup.value

        while destcupval in (currcup.value,pickedup.value, pickedup.next.value, pickedup.next.next.value): #Find destiantion cup's value
            destcupval -= 1

            if destcupval == 0:
                destcupval = 1000000

        
        destcup = cupdict[destcupval] #Get destination cup node using lookup table
        pickedup.next.next.next = destcup.next #Set next cup for the third pickup cup to destination cup's next cup
        destcup.next = pickedup #Set destination cup's next cup to first picked up cup

        currcup = currcup.next #Go to next cup
        
    print("Answer:", cupdict[1].next.value * cupdict[1].next.next.value)

if __name__ == "__main__":
    pass
    #print("Part 1")
    Part2()

    

                

        
        
            

        
    
        


    

    


    
    
