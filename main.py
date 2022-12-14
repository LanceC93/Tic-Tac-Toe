#converts numpad number to an array [row#, column#]
def convert_numpad(space):
    row = (space - 1) // 3
    col = (space - 1) % 3
    return [row, col]

#displays current state of the board
def display_board(board):
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("---------")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---------")
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])

#gives the results
def display_results(turn):
    if(turn > 8):
        print("Draw!")
    elif(turn % 2 == 1):
        print("Player 1 Wins!")
    else: 
        print("Player 2 Wins!")

#gives introduction 
def intro():
    print("Welcome to Lance's EPIC Tic Tac Toe. Standard Tic Tac Toe rules. Use numpad numbers to select which square to fill.")
    display_board([["1","2","3"],["4","5","6"],["7","8","9"]])

#plays the game
def play_game(turn, board):
    #tells the players whose turn it is
    if(turn % 2 == 1):
        print("Current Board (Player 1's Turn):")
    else: 
        print("Current Board (Player 2's Turn):")
    display_board(board)

    #assuming an int between 1-9 is provided (could be fixed to not allow those inputs)
    space = int(input("What space do you want to fill?\n"))
    #represents space in [row,col] format
    conv_space = convert_numpad(space)

    #makes sure the space is empty so other players spaces are not taken
    while (board[conv_space[0]][conv_space[1]] != " "):
        space = int(input("Space is already filled. What space do you want to fill?\n"))
        conv_space = convert_numpad(space)

    #fills space if it is empty with an x or o depending on whos turn it is
    if(turn % 2 == 1):
        board[conv_space[0]][conv_space[1]] = "X"
    else:
        board[conv_space[0]][conv_space[1]] = "O"

#verifys if the game is over and returns false boolean value if it is (could be a better algorithm, could be worth returning to)
def verify(turn, board):
    #checks if the board has been filled with no winner
    if(turn > 8):
        return 0

    #checks columns for a win
    for i in range(0,3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != " "):
            return 0
        
    #checks rows for a win
    for i in range(0,3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != " "):
            return 0
        
    #checks diagonals
    front_diagonal = board[0][0] == board[1][1] and board[1][1] == board[2][2]
    back_diagonal = board[2][0] == board[1][1] and board[1][1] == board[0][2]
    if((front_diagonal or back_diagonal) and board[1][1] != " "):
        return 0
    
    #returns true if none of the win conditions have been met
    return 1

def main():
    #give instructions
    intro()

    #records the turn number
    turn = 1
    #represents the blank spaces of the board
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]

    #continues playing the game until it is a win or draw
    play_game(turn, board)      #if this isnt in front of the loop the final board does not display the final move made
    while (verify(turn, board)):
        turn += 1
        play_game(turn, board)

    #gives final board and win message
    display_board(board)
    display_results(turn)

if __name__ == "__main__":
    main()