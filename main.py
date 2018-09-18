#
# Tick Tac Toe game for first milestone project in Python Bootcamp!
#

import random



def display_board(board):

    #print("*** func: display_board(board) *** ")

    print("\n " + board[7] + "  |  " + board[8] + "  |  " + board[9] + " ")
    print("-" * 15)
    print(" " + board[4] + "  |  " + board[5] + "  |  " + board[6] + " ")
    print("-" * 15)
    print(" " + board[1] + "  |  " + board[2] + "  |  " + board[3] + " ")

def player_input():

    #print("*** func: player_input() *** ")

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

    #print("*** func: place_marker(board, marker, position) *** ")

    if position < 1 or position > 9:
        print("\nERROR: Please position in 1-9. ")
    else:
        board[position] = marker

def win_check(board, mark):

    #print("*** func: win_check(board, mark) *** ")

    gameover = False

    if board[5] == mark:

        # Middle Row
        if board[4] == mark and board[6] == mark:
            print("\nGame over!")
            print("Middle Row for {}".format(mark))
            gameover = True

        # Middle Column
        elif board[8] == mark and board[2] == mark:
            print("\nGame over!")
            print("Middle Column for {}".format(mark))
            gameover = True

        # Bottom Left to Top Right
        elif board[1] == mark and board[9] == mark:
            print("\nGame over!")
            print("Bot left to top right for {}".format(mark))
            gameover = True

        # Bottom Right to Top Left
        elif board[3] == mark and board[7] == mark:
            print("\nGame over!")
            print("Bot right to top left {}".format(mark))
            gameover = True

    # Top Row
    elif board[7] == mark and board [8] == mark and board[9] == mark:
        print("\nGame over!")
        print("Top row for {}".format(mark))
        gameover = True

    # Bottom Row
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        print("\nGame over!")
        print("Bottom Row for {}".format(mark))
        gameover = True

    # Left Column
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        print("\nGame over!")
        print("Left column for {}".format(mark))
        gameover = True

    # Right Column
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        print("\nGame over!")
        print("Right column for {}".format(mark))
        gameover = True
    else:
        pass

    return gameover

def choose_first():
    #print("*** func: choose_first() *** ")
    return (random.randrange(1,100))%2 == 0

def space_check(board, position):
    #print("*** func: space_check(board, position) *** ")
    return board[position] == ' '

def full_board_check(board):
    #print("*** func: full_board_check(board) *** ")
    return not ' ' in board

def player_choice(board):

    #print("*** func: player_choice(board) *** ")

    input_correct = None

    while input_correct != True:

        next_position = input("\nWhat's your next choice?: ")

        if next_position < 1 or next_position > 9:
            print("\nERROR: Please position in 1-9. ")
        else:
            return space_check(board, next_position)

def replay():

    #print("*** func: replay() *** ")

    new_game = None

    redo = None

    while redo != True:

        resp = input("\nDo you want to play again? [Y/N] : ")

        if len(resp) != 1:
            print("\nPlease respond with 'Y' or 'N")

        elif resp[0].upper() == "Y":
            new_game = True
            redo = True
        else:
            new_game = False
            redo = True
    return new_game


# Main Program starts here.

print('\nWelcome to Tic Tac Toe!')
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',]
player1_mark = player_input()
player2_mark = ''

if player1_mark.upper() == "X":
    player2_mark = 'O'
else:
    player2_mark = 'X'


while True:

    # Set the game up here
    player1_turn = None
    game_on = True
    tie = None

    if choose_first() == True:
        player1_turn = True
    else:
        player1_turn = False

    display_board(board)

    while game_on:

        tie = None

        # Player 1 Turn
        if player1_turn == True:
            position = int(input('\nPLAYER 1, Please enter a number: '))

            if position < 1 or position > 9:
                print("\nERROR: Please position in 1-9. ")
            else:
                if space_check(board, position) == False:
                    print("\nERROR: That space isn't free. ")
                else:
                    place_marker(board, player1_mark, position)
                    display_board(board)
                    if win_check(board, player1_mark) == True:
                        game_on = False
                        tie = False
                    else:
                        player1_turn = False

        # Player2's turn.
        else:
            position = int(input('\nPLAYER 2, Please enter a number: '))

            if position < 1 or position > 9:
                print("\nERROR: Please position in 1-9. ")
            else:
                if space_check(board, position) == False:
                    print("\nERROR: That space isn't free. ")
                else:
                    place_marker(board, player2_mark, position)
                    display_board(board)
                    if win_check(board, player2_mark) == True:
                        game_on = False
                        tie = False
                    else:
                        player1_turn = True

        if full_board_check(board) and tie != False:
            print("\nLooks like a tie... nicely done. ")
            break

    if not replay():
        break
    else:
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
