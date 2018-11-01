# Tic Tac Toe With MiniMax

The following project is a tic tac toe game built with react, hitting a locally ran python and flask back end. The game is a demonstration of the Mini Max Algorithm making the computer AI unbeatable. This API is also setup on heroku


# Build Notes

In order to use this game it is suggested that you build the backend first.

## Backend Build
Building
  - Download the most recent version of python https://www.python.org/downloads/
  - Install the virtual env
      - `cd backend-ai`
      - `python3 -m venv venv`

  - Activate Env

  `. venv/bin/activate`
  - Run flask
    - `export FLASK_APP=computer_service.py`
    - `flask run`

## Frontend Build

Once you have the backend running change directories to the main project. Navigate to the front end folder and follow the instructions below. NOTE: Project was built on `npm v6.4.1` and `node v8.9.4`
- `git clone https://github.com/kubalaj/tictactoe`
- `cd tictactoe/tic-tac-toe`

Then run:

- `npm start`

This project was bootstrapped with the Create React App. All documentation for additional functionality that comes out of the box with that framework is listed in the `tic-tac-toe` directory

# Structure And Methodologies
#### Version Control
This project was build with the mentality of using the [gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). You will see a number of feature branches that were merged into the master branch as a development process. A similar workflow should be kept for contributions to this code base.

# Common Errors
- Sometimes the backend, due to technical debt and future planned work, gets out of sync with the game. This will cause the game to execute and decide a winner before there is an actual winner. If this ever happens either restart the backend client, followed by refresh of the front end client(RECOMMENDED), or try to get to the end of the game where you can click `Yes`, when asked to play again.

# TODO
#### Tests
- A TDD or BDD framework has so many benefits. It would have been nice to add some form of tests to help prevent regression and assure confidence in releases of the code.

#### Refactor State Management
- State is both stored on the front end and the back end. We can solve this by passing the state to the back end. Some work was made towards this goal but, was not completed. The work is stored in the `clientSideState` branch.

#### Introduce Alpha Beta Pruning
- The following algorithm could be made better by implementing [Alpha-beta prunning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning). Seeing as the problem is finite set of clickable squares, performance isn't too big of a concern and this work item can be put off.
