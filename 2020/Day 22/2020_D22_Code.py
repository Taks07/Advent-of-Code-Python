import copy
file = open("Input.txt", "r")

next(file)

P1 = []
line = file.readline()[:-1]
while len(line) != 0:
    P1.append(int(line))
    line = file.readline()[:-1]

next(file)

P2 = []
line = file.readline()[:-1]
while len(line) != 0:
    P2.append(int(line))
    line = file.readline()[:-1]

file.close()

#Part 1
def PlayRound():
    P1Val = P1.pop(0)
    P2Val = P2.pop(0)

    if P1Val > P2Val:
        P1.append(P1Val)
        P1.append(P2Val)

    else:
        P2.append(P2Val)
        P2.append(P1Val)

def Part1():
    while len(P1) != 0 and len(P2) != 0:
        PlayRound()

    if len(P1) == 0:
        winner = P2[::-1]

    else:
        winner = P1[::-1]

    total = 0
    for i,card in enumerate(winner,1):
        total += i*card

    print("Total:",total)
        
#Part 2
file = open("Input.txt", "r")

next(file)

P1 = []
line = file.readline()[:-1]
while len(line) != 0:
    P1.append(int(line))
    line = file.readline()[:-1]

next(file)

P2 = []
line = file.readline()[:-1]
while len(line) != 0:
    P2.append(int(line))
    line = file.readline()[:-1]

file.close()

def PlayRoundRecursive(P1Card = copy.deepcopy(P1), P2Card = copy.deepcopy(P2)):
    P1Cards = copy.deepcopy(P1Card)
    P2Cards = copy.deepcopy(P2Card)
    
    P1Hands = []
    P2Hands = []

    while len(P1Cards) != 0 and len(P2Cards) != 0:
        
        if P1Cards in P1Hands and P2Cards in P2Hands:
            return "P1", P1Cards
    
        P1Hands.append(copy.deepcopy(P1Cards))
        P2Hands.append(copy.deepcopy(P2Cards))
    
        P1Val = P1Cards.pop(0)
        P2Val = P2Cards.pop(0)

        if P1Val <= len(P1Cards) and P2Val <= len(P2Cards):
            winner, _ = PlayRoundRecursive(copy.deepcopy(P1Cards[:P1Val]), copy.deepcopy(P2Cards[:P2Val]))

            if winner == "P1":
                P1Cards.append(P1Val)
                P1Cards.append(P2Val)

            else:
                P2Cards.append(P2Val)
                P2Cards.append(P1Val)
                                           

        else:
            if P1Val > P2Val:
                P1Cards.append(P1Val)
                P1Cards.append(P2Val)

            else:
                P2Cards.append(P2Val)
                P2Cards.append(P1Val)

    if len(P1Cards) == 0:
        return "P2", P2Cards

    else:
        return "P1", P1Cards

def Part2():
    _, cards = PlayRoundRecursive()

    total = 0
    for i,card in enumerate(cards[::-1],1):
        total += i*card

    print("Total:",total)

    
        

if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
