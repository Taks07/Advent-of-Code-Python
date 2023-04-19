with open("Input.txt", 'r') as file:
    rounds = []
    for line in file:
        rounds.append(line.split())

def CalculateScore(yourMove, opponentMove):
    if yourMove == opponentMove:
        return 3

    elif yourMove == "rock":
        if opponentMove == "paper":
            return 0

        return 6

    elif yourMove == "paper":
        if opponentMove == "scissors":
            return 0

        return 6

    else:
        if opponentMove == "rock":
            return 0

        return 6


def Part1():
    moves = {'A': "rock", 'X': "rock", 'B': "paper", 'Y': "paper", 'C': "scissors", 'Z': "scissors"}
    scores = {"rock": 1, "paper": 2, "scissors": 3}


    score = 0

    for round in rounds:

        score += CalculateScore(moves[round[1]], moves[round[0]]) + scores[moves[round[1]]]

    print("Ans:", score)

def MoveScore(opponentMove, result):
    scores = {"rock": 1, "paper": 2, "scissors": 3}

    if result == 'Y':
        return scores[opponentMove]

    elif result == 'X':
        if opponentMove == "rock":
            return 3

        elif opponentMove == "paper":
            return 1

        else:
            return 2

    else:
        if opponentMove == "rock":
            return 2

        elif opponentMove == "paper":
            return 3

        else:
            return 1


def Part2():
    moves = {'A': "rock", 'B': "paper", 'C': "scissors"}

    resultScores = {'X': 0, 'Y': 3, 'Z': 6}
    score = 0

    for round in rounds:
        score += MoveScore(moves[round[0]], round[1]) + resultScores[round[1]]

    print("Ans:", score)



if __name__ == "__main__":
    print("Part 1")
    Part1()

    print("\nPart 2")
    Part2()
