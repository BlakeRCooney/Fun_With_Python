# Define the amount of spaces on the board
board = [" " for i in range(9)]

# Print the board layout
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Defining each player and their corisponding X or O
def player_move(icon):
    
    if icon == "X":
        player_number = 1
    elif icon == "O":
        player_number = 2
        
    print("Your turn player {}".format(player_number))
    
    # Asking users input to place marker on the board
    choice = int(input("Make your move, choices (1-9): ").strip())
    if board[choice -1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken! Please Choose another space!")
        
# Defining all of the winning possibilities
def winner_of_game(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
# Determining what is considered to be a draw
def is_draw():
    if " " not in board:
        return True
    else:
        return False
# Determining a winner of the game    
while True:
    print_board()
    player_move("X")
    print_board()
    if winner_of_game("X"):
        print("Player 1 Wins! Congradulations!")
        break
    elif is_draw():
        print("It is a draw!")
        break
    player_move("O")
    if winner_of_game("O"):
        print_board()
        print("Player 2 Wins! Congradulations!")
        break
   

    
    
    
