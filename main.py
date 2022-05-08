import os

width = 7
height = 6
winScore = 4

emptySign = "."
p1Sign = "X"
p2Sign = "O"

board = []
players = {True: p1Sign, False: p2Sign}

for i in range(height):
    row = []
    for j in range(width):
        row.append(emptySign)
    board.append(row)

def printBoard():
    for i in range(height):
        s = ""
        for j in range(width):
            s += board[i][j] + " "
        print(s)

def makeMove(position, sign):
    if position < 1 or position > width:
        return False

    if board[0][position-1] != emptySign:
        return False

    i = height-1
    while board[i][position-1] != emptySign:
        i -= 1

    board[i][position-1] = sign

    return True

def checkWin(sign):
    for i in range(height):
        for j in range(width):
            if board[i][j] == sign:
                if checkWinAux(sign, 1, i-1, j-1, "lu") or checkWinAux(sign, 1, i-1, j, "u") or checkWinAux(sign, 1, i-1, j+1, "ru") or checkWinAux(sign, 1, i, j-1, "l") or checkWinAux(sign, 1, i, j+1, "r") or checkWinAux(sign, 1, i+1, j-1, "ld") or checkWinAux(sign, 1, i+1, j, "d") or checkWinAux(sign, 1, i+1, j+1, "rd"):
                    return True
    return False

def checkWinAux(sign, count, i, j, dir):
    if i < 0 or i >= height or j < 0 or j >= width:
        return False

    if board[i][j] != sign:
        return False

    if count >= winScore - 1:
        return True

    if dir == "lu":
        return checkWinAux(sign, count + 1, i - 1, j - 1, dir)
    elif dir == "u":
        return checkWinAux(sign, count + 1, i - 1, j, dir)
    elif dir == "ru":
        return checkWinAux(sign, count + 1, i - 1, j + 1, dir)
    elif dir == "l":
        return checkWinAux(sign, count + 1, i, j - 1, dir)
    elif dir == "r":
        return checkWinAux(sign, count + 1, i, j + 1, dir)
    elif dir == "ld":
        return checkWinAux(sign, count + 1, i + 1, j - 1, dir)
    elif dir == "d":
        return checkWinAux(sign, count + 1, i + 1, j, dir)
    else:
        return checkWinAux(sign, count + 1, i + 1, j + 1, dir)

player = True
while True:
    os.system("cls")
    printBoard()
    answer = input("Enter position: ")
    if answer.isnumeric():
        if makeMove(int(answer), players[player]):
            if checkWin(players[player]):
                os.system("cls")
                printBoard()
                print(f"Player {'1' if player else '2'} wins!")
                break

            player = not player
input()
