import re

file = open("Input.txt", "r")
inputarr = []

appdetails = ""
for line in file:
    if line == "\n":
        inputarr.append(appdetails[:-1])
        appdetails = ""

    else:
        details = line.split(" ")
        appdetails = appdetails + " ".join(details)[:-1] + " "
    
    
#Part 1
def Part1():
    valcount = 0
    for details in inputarr:
        boollist = []
        for substring in ("ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:"):
            boollist.append(substring in details)

        if all(boollist):
            valcount += 1

    print("Valid Passports:",valcount)

#Part 2
def Validate(details):
    field = details.split(" ")
    boolarr = []
    
    for value in field:
        key, data = value.split(":")

        if key == "byr" and int(data) > 1919 and int(data) < 2003:
            boolarr.append(True)

        elif key == "iyr" and int(data) > 2009 and int(data) <2021:
            boolarr.append(True)

        elif key == "eyr" and int(data) > 2019 and int(data) < 2031:
            boolarr.append(True)

        elif key == "hgt":
            if "cm" in data and int(data[:-2]) > 149 and int(data[:-2]) < 194:
                boolarr.append(True)

            elif "in" in data and int(data[:-2]) > 58 and int(data[:-2]) < 77:
                boolarr.append(True)

            else:
                boolarr.append(False)
                break

        elif key == "hcl" and re.compile(r"#([a-z]|[0-9]){6}").search(data) and len(data) == 7:
            boolarr.append(True)

        elif key == "ecl" and data in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            boolarr.append(True)

        elif key == "pid":
            try:
                int(data)

            except:
                boolarr.append(False)
                break

            else:
                if len(data) == 9:
                    boolarr.append(True)

                else:
                    boolarr.append(False)
                    break

        elif key == "cid":
            pass
        
        else:
            boolarr.append(False)
            break

    return all(boolarr)

def Part2():
    valcount = 0
    for details in inputarr:
        boollist = []
        for substring in ("ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:"):
            boollist.append(substring in details)

        if all(boollist):
            if Validate(details):
                valcount += 1
            

    print("Valid Passports:",valcount)

    
if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
