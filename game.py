import os
import time
import random

#Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


#Print header
def print_header():
    print ("""
#######             #######                  #######
   #    #  ####        #      ##    ####        #     ####  ######
   #    # #    #       #     #  #  #    #       #    #    # #
   #    # #            #    #    # #            #    #    # #####
   #    # #            #    ###### #            #    #    # #
   #    # #    #       #    #    # #    #       #    #    # #
   #    #  ####        #    #    #  ####        #     ####  ######


    """)
#Define the print_board function
def print_board():
    print ("    |    |   ")
    print (" "+board[1]+"  | "+board[2]+"  | "+board[3]+"  ")
    print ("    |    |   ")
    print ("----|----|----")
    print ("    |    |   ")
    print (" "+board[4]+"  | "+board[5]+"  | "+board[6]+"  ")
    print ("    |    |   ")
    print ("----|----|----")
    print ("    |    |   ")
    print (" "+board[7]+"  | "+board[8]+"  | "+board[9]+"  ")
    print ("    |    |   ")

def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player):
        return  True
    else:
        return False

def is_board_full(board):
    if " " in board:
        return False
    else:
        return True

def get_computer_move(board, player):

    #Check for a win
    for i in range(1,10):
        if board[i] == " ":
            board[i] == player
            if is_winner(board, player):
                return i
            else:
                board[i] == " "

    #If  corners or centre is empty choose one.
    if board[1] == " ":
        return 1
    elif board[3] == " ":
        return 3
    elif board[5] == " ":
        return 5
    elif board[7] == " ":
        return 7
    elif board[9] == " ":
        return 9
    else:
        while True:
            move = random.randint(1,10)
            #If the move is blank, go ahead and return, otherwise try again
            if board[move] == " ":
                return  move
                break

while  True:
    os.system("cls")
    print_header()
    print_board()

    #Get player X input
    choice = input("PLease choose an empty space for X. ")
    choice = int(choice)

    #Check to see if space is empty
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Sorry that space is not empty")
        time.sleep(2)

    #Check for X wins
    if is_winner(board, "X"):
        os.system("cls")
        print_header()
        print_board()
        print("X has won! Congrats")
        break

    os.system("cls")
    print_header()
    print_board()

    #Check for a tie (is board full)
    #If board is full, do something
    if is_board_full(board):
        print("Tie!")
        break

    #Get player O input
    choice = get_computer_move(board, "O")

    #Check to see if space is empty
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("Sorry that space is not empty")
        time.sleep(2)

    #Check for O wins
    if is_winner(board, "O"):
        os.system("cls")
        print_header()
        print_board()
        print("O has won! Congrats")
        break

    #Check for a tie (is board full)
    #If board is full, do something
    if is_board_full(board):
        print("Tie!")
        break
