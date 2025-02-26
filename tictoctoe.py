from random import randrange

# Define the board
def create_board():
    return [[str(i + 1) for i in range(9)][i:i+3] for i in range(0, 9, 3)]

# Print the current state of the board
def print_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Check if the game is over: either someone wins, or it's a tie
def check_game_over(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return f"{board[i][0]} wins!"
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return f"{board[0][i]} wins!"
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return f"{board[0][0]} wins!"
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return f"{board[0][2]} wins!"

    # Check for tie
    if all(board[i][j] in ['X', 'O'] for i in range(3) for j in range(3)):
        return "It's a tie!"

    return None  # Game continues

# Make the computer's move
def computer_move(board):
    available_moves = [int(board[i][j]) - 1 for i in range(3) for j in range(3) if board[i][j] not in ['X', 'O']]
    move = randrange(len(available_moves))  # Random move
    row, col = divmod(available_moves[move], 3)
    board[row][col] = 'X'

# Get the user's move
def user_move(board):
    while True:
        try:
            move = int(input("Enter your move: ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("The square is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please choose a number between 1 and 9.")

# Main game loop
def play_game():
    board = create_board()
    print_board(board)

    while True:
        # Computer's move
        computer_move(board)
        print_board(board)
        result = check_game_over(board)
        if result:
            print(result)
            break
        
        # User's move
        user_move(board)
        print_board(board)
        result = check_game_over(board)
        if result:
            print(result)
            break

# Start the game
if __name__ == "__main__":
    play_game()
