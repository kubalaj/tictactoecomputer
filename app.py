#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

boardState = ["null", "null", "null", "null", "null", "null", "null", "null", "null"]

@app.route("/api/<space>", methods=['GET'])
def makeMove(space):
    boardState[int(space)] = "X"
    spot = miniMax(boardState, "O")
    return str(spot['index'])

#Start MiniMax
#return an array of availableSpots
def availableSpots(board):
    available = []
    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            available.append(i)
    print available
    print board
    return available

# Return if player has won
def isWinning(board, player):
    #horizontal win
    for i in range(3):
        if board[i] == board[i+1] == board[i+2] == player:
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

    #Check for Win or Draw
    if(isWinning(board, "X") != "null"):
        return {'score':-10}
    elif(isWinning(board, "O") != "null"):
        return {'score':10}
    elif len(possibleMoves) == 0:
        return {'score':0}
    #If no win or draw recurssivly call

    listOfMoves = []
    for i in range(len(possibleMoves)):
        moves = {}
        moves['index'] = possibleMoves[i]
        board[possibleMoves[i]] = player
        #Store each move

        if(player == "O"):
            choosenMove = miniMax(board, "O")
            moves['score'] = choosenMove['score']
        else:
            choosenMove = miniMax(board, "X")
            moves['score'] = choosenMove['score']
        board[possibleMoves[i]] = moves["index"]
        listOfMoves.append(moves)

    bestMove = 0
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

#END MiniMax

if __name__ == '__main__':
    app.run()
