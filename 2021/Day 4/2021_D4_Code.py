import copy
with open("Input.txt", 'r') as file:
    boards = []

    guess = file.readline()[:-1].split(",")

    file.readline() #Skip first blank line

    temp = []
    for line in file:
        if line != "\n":
            currline = line[:-1].split(" ")
            currline = [x for x in currline if x != '']

            temp.append(currline)

        else:
            boards.append(temp)
            temp = []
    boards.append(temp)

def MarkNumber(board, num):
    if board[0][0] == "D":
        return

    for row in board:
        for i,val in enumerate(row):
            if val == "X":
                continue

            elif int(val) == num:
                row[i] = "X"

def CheckBoard(board):
    if board[0][0] == "D":
        return False

    for row in board:
        if row == ["X" for i in range(len(row))]:
            return True

    for i in range(len(board)):
        bingo = True
        for row in board:
            if row[i] != "X":
                bingo = False
                break

        if bingo:
            return True

    return False

def CalculateScore(board):
    sum = 0
    for row in board:
        for val in row:
            if val != "X":
                sum += int(val)

    return sum

def Part1():
    for val in guess:
        for board in boards:
            MarkNumber(board,int(val))

            if CheckBoard(board):
                print("Answer:",CalculateScore(board) * int(val))
                return

def Part2():
    completed = 0

    for val in guess:

        for board in boards:
            MarkNumber(board,int(val))

            if CheckBoard(board):
                completed += 1
                if completed == len(boards):
                    print("Answer:", CalculateScore(board) * int(val))
                    return

                else:
                    board[0][0] = "D"








if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()


