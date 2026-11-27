
# ==================================
#       TIC-TAC-TOE GAME
# ==================================


# Create the game board

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


# Player details

current_player = "X"


# Function to display the board

def display_board():

    print()
    print("       TIC-TAC-TOE")
    print()

    print(" ", board[0], "|", board[1], "|", board[2])
    print(" ---+---+---")
    print(" ", board[3], "|", board[4], "|", board[5])
    print(" ---+---+---")
    print(" ", board[6], "|", board[7], "|", board[8])

    print()


# Function to display the current player's turn

def display_turn():

    if current_player == "X":
        print("Player 1's turn (X)")
    else:
        print("Player 2's turn (O)")


# Function to switch players

def switch_player():

    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# Function to take player input with validation

def make_move():

    while True:

        try:
            position = int(input("Enter a position (1-9): "))

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if position < 1 or position > 9:
            print("Invalid position! Enter a number between 1 and 9.")
            continue

        index = position - 1

        if board[index] == "X" or board[index] == "O":
            print("This position is already occupied! Try again.")
            continue

        board[index] = current_player

        print("Move successful!")

        break


# Function to check whether a player has won

def check_winner():

    # Check rows

    if board[0] == board[1] == board[2]:
        return True

    if board[3] == board[4] == board[5]:
        return True

    if board[6] == board[7] == board[8]:
        return True

    # Check columns

    if board[0] == board[3] == board[6]:
        return True

    if board[1] == board[4] == board[7]:
        return True

    if board[2] == board[5] == board[8]:
        return True

    # Check diagonals

    if board[0] == board[4] == board[8]:
        return True

    if board[2] == board[4] == board[6]:
        return True

    return False


# Function to check whether the game is a draw

def check_draw():

    return all(cell == "X" or cell == "O" for cell in board)


# Function to reset the game

def reset_board():

    global board, current_player

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"


# Function to ask whether players want to play again

def play_again():

    while True:

        answer = input(
            "Would you like to play again? (yes/no): "
        ).lower().strip()

        if answer == "yes":
            return True

        elif answer == "no":
            return False

        else:
            print("Invalid choice! Please enter yes or no.")


# ==================================
#          MAIN GAME LOOP
# ==================================

print("Welcome to Tic-Tac-Toe!")

while True:

    # Play the game

    while True:

        display_board()

        display_turn()

        make_move()

        # Check winner

        if check_winner():

            display_board()

            if current_player == "X":
                print("Congratulations! Player 1 (X) wins!")
            else:
                print("Congratulations! Player 2 (O) wins!")

            break

        # Check draw

        if check_draw():

            display_board()

            print("GAME DRAW! Nobody wins.")

            break

        # Switch players

        switch_player()

    # Ask whether players want another round

    if play_again():

        reset_board()

        print("\nStarting a new game!")

    else:

        print("\nThank you for playing Tic-Tac-Toe!")
        print("Goodbye!")

        break
