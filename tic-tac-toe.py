#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
import unittest

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# The optional function to restart the game
def resetBoard():
    for key in board.keys():
        board[key] = ' '


# TODO: update the gameboard with the user input
def markBoard(position, mark):
    if position in board:
        board[position] = mark


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    print(f"{board[1] if board[1] != ' ' else 1} | {board[2] if board[2] != ' ' else 2} | {board[3] if board[3] != ' ' else 3}")
    print("--+---+--")
    print(f"{board[4] if board[4] != ' ' else 4} | {board[5] if board[5] != ' ' else 5} | {board[6] if board[6] != ' ' else 6}")
    print("--+---+--")
    print(f"{board[7] if board[7] != ' ' else 7} | {board[8] if board[8] != ' ' else 8} | {board[9] if board[9] != ' ' else 9}")



# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    try:
        position = int(position)  
        if 1 <= position <= 9 and board[position] == ' ':
            return True
    except ValueError:
        pass
    return False

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],[4, 5, 6],[7, 8, 9],
    [1, 4, 7],[2, 5, 8],[3, 6, 9],
    [1, 5, 9],[3, 5, 7] 
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for combination in winCombinations:
        if all(board[pos] == player for pos in combination):
            return True
    return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    return all(space != ' ' for space in board.values())


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################
while True: 
    gameEnded = False
    currentTurnPlayer = 'X'

# entry point of the whole program
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")

        if validateMove(move):
            markBoard(int(move), currentTurnPlayer)
            printBoard()

            if checkWin(currentTurnPlayer):
                print(f"Player {currentTurnPlayer} wins!")
                gameEnded = True 

            elif checkFull():
                print("it's a tie!")
                gameEnded = True
            else:
                currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'
        else:
            print("Invalid input. Please enter a number from 1 to 9 that is not already taken.")
        
# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
    restart= input("Do you want another round of game? [yes/no]: ").strip().lower()
    if restart != 'yes':
        print("See you again!")
        break
    else:
        resetBoard()
