theBoard = {
    "Top_L": " ", "Top_M": " ", "Top_R": " ",
    "Middle_L": " ", "Middle_M": " ", "Middle_R": " ",
    "Bottom_L": " ", "Bottom_M": " ", "Bottom_R": " "
}
turn = "X"


def printboard(board):
    print(board["Top_L"], "+", board["Top_M"], "+", board["Top_R"])
    print("- + - + -")
    print(board["Middle_L"], "+", board["Middle_M"], "+", board["Middle_R"])
    print("- + - + -")
    print(board["Bottom_L"], "+", board["Bottom_M"], "+", board["Bottom_R"])


def play(board):
    global turn
    print("Its Turn for ", turn, ".")
    print("Click Space to skip position and ", turn, "to enter value.")
    for i in board.keys():
        if board[i] == " ":
            q = input(""+i+": ")
            q = q.upper()
            if q == turn:
                board[i] = q
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"

                break

    return board


printboard(theBoard)
for j in range(9):
    theBoard = play(theBoard)
    printboard(theBoard)
