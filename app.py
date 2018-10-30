#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

board= ["null", "null", "null", "null", "null", "null", "null", "null", "null"]

@app.route("/api/<space>", methods=['GET'])
def makeMove(space):
    board[int(space)] = "X"
    #Step 1
    placeForWin = winningMove("win")
    if placeForWin != "null":
        return(placeForWin)
    #Step 2
    placeToBlock = winningMove("block")
    if placeToBlock != "null":
        return(placeToBlock)
    #Step 3
    centerPlacement = placeInCenter()
    if centerPlacement != "null":
        return(centerPlacement)
    # Step 4
    cornerPlacement = placeInCorner()
    if cornerPlacement != "null":
        return(cornerPlacement)
    #Step 5
    sidePlacement = placeOnSides()
    if sidePlacement != "null":
        return(sidePlacement)
    return ("null")


def winningMove(winOrBlock):
    diagonalWin = diagonalWinningMove(winOrBlock)
    if diagonalWin != "null":
        return(diagonalWin)
    verticalWin = verticalWinningMove(winOrBlock)
    if verticalWin != "null":
        return(verticalWin)
    horizontalWin = horizontalWinningMove(winOrBlock)
    if horizontalWin != "null":
        return(horizontalWin)
    else:
        return("null")

def diagonalWinningMove(winOrBlock):
    if winOrBlock == "win":
        toMatch = "O"
    if winOrBlock == "block":
        toMatch = "X"
    if board[4] == "null" and (board[0] == toMatch and board[8] == toMatch) or (board[2] == toMatch and board[6] == toMatch):
        board[4] = "O"
        return("4")
    if board[0] == "null" and (board[4] == toMatch and board[8] == toMatch):
        board[0] = "O"
        return("0")
    if board[2] == "null" and (board[4] == toMatch and board[6] ==toMatch):
        board[2] = "O"
        return("2")
    if board[6] == "null" and (board[4] == toMatch and board[2] == toMatch):
        board[6] = "O"
        return("6")
    if board[8] == "null" and (board[4] == toMatch and board[0] == toMatch):
        board[8] = "O"
        return("8")
    else:
        return("null")

def verticalWinningMove(winOrBlock):
    if winOrBlock == "win":
        toMatch = "O"
    if winOrBlock == "block":
        toMatch = "X"
    i = 0
    while i < 9:
        if board[i] == "null":
            if i < 3 and board[i + 3] == toMatch and board[i + 6] == toMatch:
                board[i] = "O"
                return(str(i))
            if i >= 3 and i < 6 and board[i - 3] == toMatch and board[i + 3] == toMatch:
                board[i] = "O"
                return(str(i))
            if i >= 6 and board[i - 3] == toMatch and board[i - 6] == toMatch:
                board[i] = "O"
                return(str(i))
            i += 1
        else:
            i += 1
    return("null")

def horizontalWinningMove(winOrBlock):
    if winOrBlock == "win":
        toMatch = "O"
    if winOrBlock == "block":
        toMatch = "X"
    i = 0
    while i < 9:
        if board[i] == "null":
            if i % 3 == 1 and board[i - 1] == toMatch and board[i + 1] == toMatch:
                board[i] = "O"
                return(str(i))
            if i % 3 == 0 and board[i + 1] == toMatch and board[i + 2] == toMatch:
                board[i] = "O"
                return(str(i))
            if i % 3 == 2 and board[i - 1] == toMatch and board[i - 2] == toMatch:
                board[i] = "O"
                return(str(i))
            i += 1
        else:
            i += 1
    return("null")

def placeInCenter():
    if board[4] != "X" and board[4] == "null":
        board[4] = "O"
        return('4')
    return("null")

def placeInCorner():
    if board[0] != "X" and board[0] == "null":
        board[0] = "O"
        return('0')
    if board[2] != "X" and board[2] == "null":
        board[2] = "O"
        return('2')
    if board[6] != "X" and board[6] == "null":
        board[6] = "O"
        return('6')
    if board[8] != "X" and board[8] == "null":
        board[8] = "O"
        return('8')
    return ("null")

def placeOnSides():
    if board[1] != "X" and board[1] == "null":
        board[1] = "O"
        return('1')
    if board[3] != "X" and board[3] == "null":
        board[3] = "O"
        return('3')
    if board[5] != "X" and board[5] == "null":
        board[5] = "O"
        return('5')
    if board[7] != "X" and board[7] == "null":
        board[7] = "O"
        return('7')
    return ("null")

if __name__ == '__main__':
    app.run()
