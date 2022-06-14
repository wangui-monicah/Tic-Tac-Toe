
import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
current_Player = "X"
winner = None
game_Running = True


#printing the game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#take player input
def player_Input(board):
    inp = int(input("Enter a number 1-9: "))
    
    if inp >=1 and inp <= 8 and board[inp-1] == "-":
        board[inp-1] = current_Player
    else:
        print("Ooops! That spot is occupied")

#check for win or tie
def check_horizontal(board):
    global winner #if changes in winner happens in this function, it happena in the entire file
    
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] and board[1] != "-":
        winner = board[3] 
        return True

    elif board[6] == board[7] == board[8] and board[2] != "-":
        winner = board[6] 
        return True

def check_vertical(board):
    global winner

    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[1] 
        return True

    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[2] 
        return 
    
def check_diag(board):
    global winner

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2] 
        return True

def check_Tie(board):
    global game_Running
    if "-" not in board:
        print_board(board)
        print(" IT'S A TIE!!!")
        game_Running = False

def check_Win():
    
    if check_diag(board) or check_horizontal(board) or check_vertical(board):
        print("The winner is " + winner)
        #the f changes everything into a string
        

    
    

#switch player
def switch_player():
    global current_Player
    if current_Player == "X":
        current_Player = "O"
    else:
        current_Player = "X"


#computer player
def computer(board):
    while current_Player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()



#check for win or tie again

while game_Running:
    print_board(board)
    player_Input(board)
    check_Win()
    check_Tie(board)
    switch_player()
    computer(board)
    check_Win()
    check_Tie(board)

