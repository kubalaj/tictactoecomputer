#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

boardState = [0, 1, 2, 3, 4, 5, 6, 7, 8]

@app.route("/api/restart", methods=['GET'])
def restart():
    boardState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
@app.route("/api/<space>", methods=['GET'])
def makeMove(space):
    if(isWinning(boardState, "X"):
        return "HUMAN WINS! PLAY AGAIN?"
    if(isWinning(boardState, "X"):
        return "COMPUTER OVERLOAD WINS! PLAY AGAIN?"
    if(len(availableSpots(boardState)) == 0):
        return "DRAW, PLAY AGAIN?"
    boardState[int(space)] = "X"
    spot = miniMax(boardState, "O")
    boardState[spot['index']] = "O"
    return str(spot['index'])

def availableSpots(board):
    available = []
    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            available.append(i)
    return available

# Return if player has won
def isWinning(board, player):
    #horizontal win
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] == player:
            return player
    #vertical win
    for i in range(3):
        if board[i] == board [i+3] == board[i+6] == player:
            return player
    #diagonal win
    if board[0] == board [4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return player
    return("null")

def miniMax(board, player):
    possibleMoves = availableSpots(board)

    #Check if Win
    if(isWinning(board, "X") != "null"):
        return {'score':-10}
    elif(isWinning(board, "O") != "null"):
        return {'score':10}
    elif len(possibleMoves) == 0:
        return {'score':0}

    #Initiate Recursion for developing all possible moves with scores
    listOfMoves = []
    for i in range(len(possibleMoves)):
        moves = {}
        moves['index'] = board[possibleMoves[i]]
        board[possibleMoves[i]] = player

        if(player == "O"):
            choosenMove = miniMax(board, "X")
            moves['score'] = choosenMove['score']
        else:
            choosenMove = miniMax(board, "O")
            moves['score'] = choosenMove['score']
        board[possibleMoves[i]] = moves["index"]
        listOfMoves.append(moves)

    #Check for the actual Best Move
    if player == "O":
        bestScore = -10000
        for move in range(len(listOfMoves)):
            if listOfMoves[move]['score'] > bestScore:
                bestScore = listOfMoves[move]['score']
                bestMove = move
    else:
        bestScore = 10000
        for move in range(len(listOfMoves)):
            if listOfMoves[move]['score'] < bestScore:
                bestScore = listOfMoves[move]['score']
                bestMove = move
    return listOfMoves[bestMove]

if __name__ == '__main__':
    app.run()
