cardkey = 8458505
doorkey = 16050997

#Part 1
def FindLoopNum(key):
    subjectnum = 7
    value = 1
    loopnum = 0
    
    while value != key:
        loopnum += 1

        value *= subjectnum
        value = value % 20201227

    return loopnum

def GetEncryptionKey(cardkey, doorloop):
    subjectnum = cardkey
    value = 1
    
    for _ in range(doorloop):
        value *= subjectnum
        value = value % 20201227

    return value
        

def Part1():
    cardloop = FindLoopNum(cardkey)
    doorloop = FindLoopNum(doorkey)

    print("Encryption Key:", GetEncryptionKey(cardkey, doorloop))

if __name__ == "__main__":
    print("Part 1")
    Part1()
