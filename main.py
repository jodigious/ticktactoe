#
# Tick Tac Toe game for first milestone project in Python Bootcamp!
#

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

    while input_correct != True:
        player1 = input("\nPlease pick a marker 'X' or 'O': ")

        if player1.upper() != 'X' and player1.upper() != 'O':
            print("\nERROR: Please choose either 'X' or 'O'. ")
        elif len(player1) != 1:
            print("\nERROR: please pick one character. ")
        else:
            player1 = player1.upper()
            input_correct = True

def place_marker(board, marker, position):

    position = int(input('Please enter a number: '))

    if position < 1 or position > 9:
        print("\nERROR: Please position in 1-9. ")
    else:
        board[position] = marker


def win_check(board, mark):
    pass

def choose_first():
    pass

def space_check(board, position):
    pass

def full_board_check(board):
    pass

def player_choice(board):
    pass

def reply():
    pass




board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',]
display_board(board)



display_board(board)
