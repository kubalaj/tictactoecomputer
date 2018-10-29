#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

test = [
    {
            'id': 1,
            'description': 'it works!'
    }
]

@app.route('/api/v1.0/get_move', methods=['GET'])
def get_move():
    return jsonify({'test': test})

@app.route('/api/v1.0/is_winner', methods=['GET'])
def is_winner():
    return jsonify({'test': test})
#0 Check to see if there is a Winner
#1 Need a Function to See Computer Can Make Move To Win game
#2 Need Function to see if there is a move Player would make to # WARNING:
#3 Need a function to place in corner
#4 If no Corners see if center is free
#5 if center is not free go to sides


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
