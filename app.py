#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

board= ["null", "null", "null", "null", "null", "null", "null", "null", "null"]

@app.route("/api/<space>", methods=['GET'])
def makeMove(space):
    board[int(space)] = "X"
    board[3] = "O"
    cornerMove = placeInCorner()
    print cornerMove
    return ('3')

def placeInCorner():
    if board[0] != "X" and board[0] != "null":
        board[0] = "O"
        return(0)
    if board[2] != "X" and board[2] != "null":
        board[2] = "O"
        return(2)
    if board[6] != "X" and board[6] != "null":
        board[6] = "O"
        return(6)
    if board[8] != "X" and board[8] != "null":
        board[8] = "O"
        return(8)
    return()

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
