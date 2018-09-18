#
# Tick Tac Toe game for first milestone project in Python Bootcamp!
#

import random



def display_board(board):

    if len(board) == 10:
        print("\n " + board[7] + "  |  " + board[8] + "  |  " + board[9] + " ")
        print("-" * 15)
        print(" " + board[4] + "  |  " + board[5] + "  |  " + board[6] + " ")
        print("-" * 15)
        print(" " + board[1] + "  |  " + board[2] + "  |  " + board[3] + " ")
    else:
        print("\nERROR: Please input appropriate board parameters.")



def player_input():

    input_correct = None
    player1 = ''

    while input_correct != True:

        player1 = input("\nPlease pick a marker 'X' or 'O': ")

        if player1.upper() != 'X' and player1.upper() != 'O':
            print("\nERROR: Please choose either 'X' or 'O'. ")
        elif len(player1) != 1:
            print("\nERROR: please pick one character. ")
        else:
            player1 = player1.upper()
            input_correct = True

    return player1



def place_marker(board, marker, position):

    position = int(input('Please enter a number: '))

    if position < 1 or position > 9:
        print("\nERROR: Please position in 1-9. ")
    else:
        board[position] = marker



def win_check(board, mark):
    if board[5] == mark:

        # Middle Row
        if board[4] == mark and board[6] == mark:
            print("\nGame over!")

        # Middle Column
        elif board[8] == mark and board[2] == mark:
            print("\nGame over!")

        # Bottom Left to Top Right
        elif board[1] == mark and board[9] == mark:
            print("\nGame over!")

        # Bottom Right to Top Left
        elif board[3] == mark and board[7]:
            print("\nGame over!")

    # Top Row
    elif board[7] == mark and board [8] == mark and board[9] == mark:
        print("\nGame over!")

    # Borrom Row
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        print("\nGame over!")

    # Left Column
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        print("\nGame over!")

    # Right Column
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        print("\nGame over!")
    else:
        print("\nLet's keep playing!")



def choose_first():
    return (random.randrange(1,2))%2 == 0



def space_check(board, position):
    return board[position] == ' '



def full_board_check(board):
    for i in board:
        if i != ' ':
            return True
        else:
            return False



def player_choice(board):

    input_correct = None

    while input_correct != True:

        next_position = input("\nWhat's your next choice?: ")

        if position < 1 or position > 9:
            print("\nERROR: Please position in 1-9. ")
        else:
            return space_check(board, next_position)



def reply():

    new_game = None

    x = None

    while x != True

        resp = input("\nDo you want to play again? [Y/N] : ")

        if len(resp) != 1:
            print("\nPlease respond with 'Y' or 'N")

        elif resp[0].upper() == "Y":
            new_game = True
            x = True
        else:
            new_game = False
            x = True
    return new_game





board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',]

# Main Program starts here.
print('\nWelcome to Tic Tac Toe!')

while True:

    # Set the game up here
    pass

    while game_on:

        # Player 1 Turn


        # Player2's turn.

            pass

    if not replay():
        break
# break