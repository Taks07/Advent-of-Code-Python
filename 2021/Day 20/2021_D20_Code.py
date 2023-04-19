import copy

with open("Input.txt", 'r') as file:
    enhancer = file.readline()[:-1]
    file.readline() #skip gap

    image = []
    for line in file:
        image.append(line[:-1])

imagecoords = {} #coord:pixel

for row in range(len(image)):
    for col in range(len(image[0])):
        imagecoords[(col,row)] = image[row][col]


def Enhance(timesran):
    copyimagecoords = copy.deepcopy(imagecoords)

    maxes = [max([col for col,_ in imagecoords]), max([row for _, row in imagecoords])] #[maxcol, maxrow]
    mins = [min([col for col,_ in imagecoords]), min([row for _, row in imagecoords])]

    for row in range(mins[1] - 1, maxes[1] + 2):
        for col in range(mins[0] - 1, maxes[0] + 2):
            numfrombin = Search((col,row), timesran, copyimagecoords)
            imagecoords[(col, row)] = enhancer[numfrombin]

def Search(coords, timesran, copyimagecoords):
    binnumber = ""

    temp = {".":"0", "#":"1"}

    for drow in (-1,0,1):
        for dcol in (-1,0,1):
            currcoord = (coords[0] + dcol, coords[1] + drow)

            if currcoord not in copyimagecoords:
                if timesran % 2 == 0: #Infinite field of pixels flip between dark and light each enhancement
                    binnumber += "0"

                else:
                    binnumber += "1"

            else:
                binnumber += temp[copyimagecoords[currcoord]]

    return int(binnumber,2)

def Run(num):
    for i in range(num):
        Enhance(i)

    print("Answer:", sum([1 for i in imagecoords.values() if i == "#"]))

if __name__ == "__main__":
    print("Part 1")
    Run(2)

    print("\nPart 2")
    Run(48)