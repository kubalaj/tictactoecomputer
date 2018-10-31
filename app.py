#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

test = ["X", "X", "O", "X", "O", "O", "null", "X", "O"]

@app.route("/api/<space>", methods=['GET'])
def makeMove(space):
    board[int(space)] = "X"

    #MINIMAX
        #RETURN If End +1 0 -1
        #Go Through Available Spots
        #Call MINIMAX
        #Return Best Value from those calls


    #OLD ALGOR SIMPLE IMPLMENTATION MAYBE GOOD EASY MODE
    #Step 1
    placeForWin = winningMove()
    if placeForWin != "null":
        return(placeForWin)
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

#Start MiniMax
#return an array of availableSpots
def availableSpots(board):
    available = []
    for i in range(9):
        if board[i] == "null":
            available.append(i)
    return available
# Return if player has won
def isWinning(board, player):
    #horizontal win
    for i in range(3):
        if board[i] == board[i+1] == board[i+2] == player:
            return player
    #vertical win
    for i in range(3):
        print board[i]
        print board [i+3]
        print board[i+6]
        if board[i] == board [i+3] == board[i+6] == player:
            return player
    #diagonal win
    if board[0] == board [4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return player
    return("null")




#END MiniMax
def winningMove():
    diagonalWin = diagonalWinningMove()
    if diagonalWin != "null":
        return(diagonalWin)
    verticalWin = verticalWinningMove()
    if verticalWin != "null":
        return(verticalWin)
    horizontalWin = horizontalWinningMove()
    if horizontalWin != "null":
        return(horizontalWin)
    else:
        return("null")

def diagonalWinningMove():
    if board[4] == "null" and (board[0] == "O" and board[8] == "O") or (board[2] == "O" and board[6] == "O"):
        board[4] = "O"
        return("4")
    if board[0] == "null" and (board[4] == "O" and board[8] == "O"):
        board[0] = "O"
        return("0")
    if board[2] == "null" and (board[4] == "O" and board[6] == "O"):
        board[2] = "O"
        return("2")
    if board[6] == "null" and (board[4] == "O" and board[2] == "O"):
        board[6] = "O"
        return("6")
    if board[8] == "null" and (board[4] == "O" and board[0] == "O"):
        board[8] = "O"
        return("8")
    else:
        return("null")

def verticalWinningMove():
    i = 0
    while i < 9:
        if board[i] == "null":
            if i < 3 and board[i + 3] == "O" and board[i + 6] == "O":
                board[i] = "O"
                return(str(i))
            if i >= 3 and i < 6 and board[i - 3] == "O" and board[i + 3] == "O":
                board[i] = "O"
                return(str(i))
            if i >= 6 and board[i - 3] == "O" and board[i - 6] == "O":
                board[i] = "O"
                return(str(i))
            i += 1
        else:
            i += 1
    return("null")

def horizontalWinningMove():
    i = 0
    while i < 9:
        if board[i] == "null":
            if i % 3 == 1 and board[i - 1] == "O" and board[i + 1] == "O":
                board[i] = "O"
                return(str(i))
            if i % 3 == 0 and board[i + 1] == "O" and board[i + 2] == "O":
                board[i] = "O"
                return(str(i))
            if i % 3 == 2 and board[i - 1] == "O" and board[i - 2] == "O":
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
