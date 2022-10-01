#displays current state of the board
def display_board(board):
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[0] + " | " + board[1] + " | " + board[2])

#gives introduction 
def intro():
    print("Welcome to Lance's EPIC Tic Tac Toe. Standard Tic Tac Toe rules. Use numpad numbers to select which square to fill.")
    display_board(["1","2","3","4","5","6","7","8","9"])

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

    #makes sure the space is empty so other players spaces are not taken
    while (board[space - 1] != " "):
        space = int(input("Space is already filled. What space do you want to fill?\n"))

    #fills space if it is empty with an x or o depending on whos turn it is
    if(turn % 2 == 1):
        board[space - 1] = "X"
    else:
        board[space - 1] = "O"

#verifys if the game is over and returns false boolean value if it is
def verify(turn, board):
    if(turn >= 10):
        return 0
    return 1

def main():
    #give instructions
    intro()
    #records the turn number
    turn = 1
    #represents the blank spaces of the board
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    #continues playing the game until it is a win or draw
    while (verify(turn, board)):
        play_game(turn, board)
        turn += 1

if __name__ == "__main__":
    main()