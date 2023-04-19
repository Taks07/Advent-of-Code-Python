file = open("Input.txt", 'r')
input = list(file.readline())
file.close()

imageLayers = []
def CreateImage(wide, tall):
    while len(input) > 0:
        layer = []

        for i in range(tall):
            row = ""

            for j in range(wide):
                row += input.pop(0)

            layer.append(row)

        imageLayers.append(layer)

def CountNum(layer,num):
    zeroes = 0
    if layer == None:
        return 1000000000000000000000

    for row in layer:
        zeroes += row.count(str(num))

    return zeroes

def Part1():
    wantedlayer = None

    for layer in imageLayers:
        if CountNum(layer,0) < CountNum(wantedlayer,0):
            wantedlayer = layer

    print("Answer:", CountNum(wantedlayer,1) * CountNum(wantedlayer,2))

def Part2(wide, tall, scale):
    image = [["" for i in range(wide)] for i in range(tall)]

    for layer in imageLayers:
        for i in range(tall):
            for j in range(wide):
                if image[i][j] == "" and layer[i][j] in ('0', '1'):
                    image[i][j] = layer[i][j]

    import tkinter

    root = tkinter.Tk()
    root.attributes('-topmost', True)

    can = tkinter.Canvas(root, width = wide * scale, height = tall * scale)

    can.pack()

    for rownum in range(len(image)):
        for pixelnum in range(len(image[0])):
            if image[rownum][pixelnum] == "0":
                colour = "black"

            else:
                colour = "white"

            can.create_rectangle(pixelnum * scale, rownum * scale,(pixelnum * scale) + scale, (rownum * scale) + scale, fill = colour, outline = colour)

    root.mainloop()






if __name__ == "__main__":
    wide = 25
    tall = 6
    scale = 10

    CreateImage(wide, tall)
    print("Part 1")
    Part1()

    print("Part 2\n")
    Part2(wide, tall, scale)