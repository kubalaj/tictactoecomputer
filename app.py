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
    winningPlacement = winningMove()
    if winningPlacement != "null":
        return(winningPlacement)
    # print winningPlacement
    #Step 3
    # centerPlacement = placeInCenter()
    # if centerPlacement != "null":
    #     return(centerPlacement)
    # Step 4
    cornerPlacement = placeInCorner()
    if cornerPlacement != "null":
        return(cornerPlacement)
    #Step 5
    sidePlacement = placeOnSides()
    if sidePlacement != "null":
        return(sidePlacement)
    return ("null")


def winningMove():
    i = 0
    nullCount = 0
    zeroCount = 0
    nullSpace = -1
    while i < 9:
        if board[i] == "X":
            i = i + 3 - i % 3
            continue
        if board[i] == "null":
            nullCount += 1
            nullSpace = i
        if board[i] == "O":
            zeroCount += 1
        if nullCount == 1 and zeroCount == 2:
            board[nullSpace] = "0"
            return(str(nullSpace))
        if i % 3 == 0 and i != 0:
            nullCounter = 0
            winningCounter = 0
            nullSpace = -1
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

# @app.route('/api/v1.0/get_move', methods=['GET'])
# def get_move():
#     return jsonify({'test': test})
#
# @app.route('/api/v1.0/is_winner', methods=['GET'])
# def is_winner():
#     return jsonify({'test': test})
#0 Check to see if there is a Winner
#1 Need a Function to See Computer Can Make Move To Win game
#2 Need Function to see if there is a move Player would make to # WARNING:
#3 Need a function to place in corner
#4 If no Corners see if center is free
#5 if center is not free go to sides


if __name__ == '__main__':
    app.run()
