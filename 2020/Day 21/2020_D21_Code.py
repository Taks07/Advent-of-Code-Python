import re, copy
file = open("Input.txt", "r")
ingredientslist = []
allergenslist = []

allingredients = []
allallergens = []
regex = re.compile("(.+) \(contains (.+)\)")

for line in file:
    ingredient, allergen = regex.findall(line)[0]
    ingredient = ingredient.split(" ")
    allergens = allergen.split(", ")

    for i in ingredient:
        if i not in allingredients:
            allingredients.append(i)

    for a in allergens:
        if a not in allallergens:
            allallergens.append(a)

    ingredientslist.append(ingredient)
    allergenslist.append(allergens)

file.close()

#Part 1
def CheckIngredient(ingredient):
    possallergens = []
    impossallergens = []
    for i in range(len(ingredientslist)):
        if ingredient in ingredientslist[i]:
            for a in allergenslist[i]:
                if a not in possallergens and a not in impossallergens:
                    possallergens.append(a)

        else:
            for a in allergenslist[i]:
                if not a in impossallergens:
                    impossallergens.append(a)

    for a in impossallergens:
        if a in possallergens:
            possallergens.remove(a)

    if len(possallergens) == 0:
        return True, possallergens

    else:
        return False, possallergens
            
    

def Part1():
    safeingredients = []
    for i in allingredients:
        noallergens,_ =  CheckIngredient(i)
        if noallergens:
            safeingredients.append(i)

    total = 0
    for inglist in ingredientslist:
        for i in safeingredients:
            if i in inglist:
                total += 1

    print("Total:", total)

#Part 2
def Part2():
    possdict = {}
    for i in allingredients:
        noallergens,allergens =  CheckIngredient(i)
        if not noallergens:
            possdict[i] = allergens

    allergendict = {}
    length = len(possdict)
    
    while length != len(allergendict):
        for key in possdict:
            if len(possdict[key]) == 1:
                val = possdict[key][0]
                allergendict[key] = val
                break

        possdict.pop(key)

        for key in possdict:
            if val in possdict[key]:
                possdict[key] = [x for x in possdict[key] if x != val]

    sortedvals = sorted(allergendict.values())
    sorteddict = []

    for val in sortedvals:
        for key in allergendict:
            if allergendict[key] == val:
                sorteddict.append(key)
                break
    print("Answer:", ",".join(sorteddict))
            

    
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()

        

        
                       
