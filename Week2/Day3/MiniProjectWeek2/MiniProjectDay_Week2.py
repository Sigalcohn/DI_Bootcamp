#Tic Tac Toe Game
TicTacToe= [         #step1 representing a3x3 grid with a 2D list, each cell in the grid is empty
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]     
]

def display_board(TicTacToe):  #function to display the current state of the board
   print (  "   1  2  3")
   
   for i  in range (3):
       print (i + 1," ", "|".join(TicTacToe[i]))  #vertical 
       print ("    -+-+-")  #horizontal


def player_input(player):  #function to get player input
    while True:
       print ("Player", player, "turn")
       
       row= (input ("Enter row umber (1-3): ")) 
       column = (input ("Enter column number (1-3): "))
       
       if row in ["1", "2","3"] and column in ["1", "2", "3"]: 
           
           row = int(row)-1
           column = int(column)-1
           
           if TicTacToe [row] [column] == " ":
              print ("Valid move")
              return row, column
           else:
              print ("already taken")
                   
    else:
      print ("Invalid input")
      
def check_win(board, player):
    
    for row in board:
        if row [0] == row [1] == row [2] == player:  #check for horizontal win
            return True
    for column in range (3):
        if board [0][column] == board [1][column] == board [2][column] == player:  #check for vertical win
            return True
    if board [0][0] == board [1][1] == board [2][2] == player:
        return True
    if board [0][2] == board [1][1] == board [2][0] == player:
        return True
    
    return False


def check_tie(board):
        for row in board:
            for cell in row:
                if cell == " ":
                    return False  #if there is an empty cell, the game is not a tie
        return True  #if there are no empty cells, the game is a tie
print (check_tie(TicTacToe))  #calling the function to check if the game is a tie

def play():
    player= "X"  #starting player
    while True:
        display_board(TicTacToe)  #display the current state of the board
        row, column = player_input(player)  #get player input
        TicTacToe[row][column] = player  #update the board with the player's move
        
        if check_win(TicTacToe, player):  #check if the current player has won
            display_board(TicTacToe)
            print ("Player", player, "wins!")
            break
        elif check_tie(TicTacToe):  #check if the game is a tie
            display_board(TicTacToe)
            print ("Its a tie")
            break
        
        if player == "X":  #switch players
            player = "O"
        else:
            player = "X"
play()  #start the game
