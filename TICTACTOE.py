# ----- Global Variables -----


# Game board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whos turn is it
player = "X"


# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic tac toe
def play_game():

  # Display initial board
  display_board()

  # While the game is still going
  while game_still_going:
    
    # Handle a single turn of an arbitrary player
    handle_turn(player)

    # Check if the game has ended
    check_if_game_over()

    # Flip to the other player
    flip_player()

  # The game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")

  elif winner == None:
    print("Tie.")


# Handle a single turn of an arbitrary player
def handle_turn(player):

  # Current players turn
  print(player + "'s turn.")

  # Current player's decision
  position = input("Choose a position from 1-9: ")

  # Position validity checker
  valid = False
  while not valid:
    
    # Valid position checker
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    # Converts user input to an interger and subracts 1 to give True position on the board
    position = int(position) - 1

    # If the the position is available then break loop
    if board[position] == "-":
      valid = True
    
    # If the position is not available try again
    else:
      print("Space is taken. Try again.")

  # Fills in the position with whoever's turn it was who picked the position(X or O)
  board[position] = player

  # Displays updated board
  display_board()


# Checks if the game is over by checking for a winner or tie
def check_if_game_over():
  
  #checks for a winner
  check_for_winner()

  #checks if it was a tie
  check_if_tie()


#checks for winner
def check_for_winner():

  # Set up global variables
  global winner

  # Check rows
  row_winner = check_rows()

  # Check columns
  column_winner = check_columns()

  # Check diagonals
  diagonal_winner = check_diagonals()

  # Get the winner
  if row_winner:

    # There was a winner
    winner = row_winner

  elif column_winner:

    # There was a winner
    winner = column_winner

  elif diagonal_winner:

    # There was a winner
    winner = diagonal_winner

  else:
    # There was no winner
    winner = None

  return


# Checks if it was a tie
def check_if_tie():

  # Set global variable
  global game_still_going

  # If there are no blank spaces left and no winner that is a tie
  if "-" not in board:

    # Changes game_still_going to False to end game and call a tie
    game_still_going = False

  return


# Checks rows for a winner
def check_rows():

  # Set global variables
  global game_still_going

  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  # If any row does have a match, flag a there is a win
  if row_1 or row_2 or row_3:

    # Changes game_still_going to False to end game and call a winner
    game_still_going = False

  # Return the winner (X or O)
  if row_1:
    return board[0]

  elif row_2:
    return board[3]

  elif row_3:
    return board[6]

  return


# Check columns for winner
def check_columns():
    
  # Set global variables
  global game_still_going

  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  # If any column does have a match, flag a there is a win
  if column_1 or column_2 or column_3:

    # Changes game_still_going to False to end game and call a winner
    game_still_going = False

  # Return the winner (X or O)
  if column_1:
    return board[0]

  elif column_2:
    return board[1]

  elif column_3:
    return board[2]

  return


# Check diaganols for a winner
def check_diagonals():
  
  # Set global variables
  global game_still_going

  # Check if any of the diagonals have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  # If any diagonal does have a match, flag a there is a win
  if diagonal_1 or diagonal_2:

    # Changes game_still_going to False to end game and call a winner
    game_still_going = False

  # Return the winner (X or O)
  if diagonal_1:
    return board[0]

  elif diagonal_2:
    return board[2]

  return


# Switches turns after each player chooses a valid position
def flip_player():

  # Set global variable
  global player

  # If current player was X, then change it to O
  if player == "X":
    player = "O"

    # If the current player was O, then change it to X
  elif player == "O":
    player = "X"

  return


play_game()
