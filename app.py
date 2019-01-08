#!flask/bin/python
from flask import Flask, request
from flask_cors import CORS
import sys
import logging
import json

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
CORS(app)

@app.route("/api/<state>", methods=['GET'])
def makeMove(state):
    board = formatBoard(state)
    spot = miniMax(board, "O")
    board[int(spot['index'])] = "O"
    return json.dumps(board)

@app.route("/api/win/<state>", methods=['GET'])
def isTerminalState(state):
    formattedBoard = formatBoard(state)
    if(len(availableSpots(formattedBoard)) == 0):
        return "DRAW, PLAY AGAIN?"
    elif(isWinning(formattedBoard, "O") == "O"):
        return "COMPUTER WINS! PLAY AGAIN?"
    else:
        return "false"

def formatBoard(board):
    board = board.split(",")
    for space in range(len(board)):
        if type(board[space]) == str:
            board[space] = (board[space].encode('UTF8'))
        if board[space] != "O" and board[space] != "X":
            board[space] = int(board[space])
    return board

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
    elif len(possibleMoves) <= 1:
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
