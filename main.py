
INTRO_MESSAGE = """
    Hello! Welcome to Tic Tac Toe game!

    Rules: Player 1 and player 2, representsted by X and O, take turns
    marking the spaces in a 3*3 grid. The player who succeeds in placing
    three of their marks in a horizontal, vertical, or diagonal row wins
"""

BOARD = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

SIGNS = {
    1: "X",
    2: "Y"
}

POSITIONS = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

PLAYER_WON_MESSAGE = "Player {player}, you won!"

def make_choice(player1, player2, count):
    # Decides the turn
    current_player = player2 if count % 2 == 0 else player1

    print(f"Player {current_player}, it is your turn. ")

    while True:
        try:
            choice = input("Use [p] for positions, [1-9] for cells and [b] for board >>> ")
            choice = choice.lower()

            if choice == "p":
                display_board_coordinates()
                continue
            elif choice == "b":
                display_board()
                continue
            else:
                choice = int(choice)
                if choice > 9 or choice < 0:
                    raise ValueError
            
            row, column = POSITIONS.pop(choice)
        except ValueError:
            print("Not an option. Use [p] for positions, [1-9] for cells and [b] for board")
        except KeyError:
            print("Cell is already filled")
        else:
            break


    # Locates player's symbol on the board
    if current_player == player1:
        BOARD[row][column] = player1
    else:
        BOARD[row][column] = player2
 

def display_board():
    rows = len(BOARD)
    print("\n")
    for row in range(rows):
        print(f" {BOARD[row][0]} | {BOARD[row][1]} | {BOARD[row][2]} ")
        if row != rows - 1:
            print("---+---+---")
    print("\n")
    return BOARD

def display_board_coordinates():
    pattern = """ 
     1 | 2 | 3 
    ---+---+---
     4 | 5 | 6  
    ---+---+---
     7 | 8 | 9 
    """
    print(pattern)


def check_board_state(player1, player2):
    winner = False
    # Check the rows
    for i in range (len(BOARD)):
        # rows
        if (BOARD[i][0] == BOARD[i][1] == BOARD[i][2] == player1):
            winner = True
            print(PLAYER_WON_MESSAGE.format(player=player1))
        elif (BOARD[i][0] == BOARD[i][1] == BOARD[i][2] == player2):
            winner = True
            print(PLAYER_WON_MESSAGE.format(player=player2))
        # columns       
        elif (BOARD[0][i] == BOARD[1][i] == BOARD[2][i] == player1):
            winner = True
            print(PLAYER_WON_MESSAGE.format(player=player1))
        elif (BOARD[0][i] == BOARD[1][i] == BOARD[2][i] == player2):
            winner = True
            print(PLAYER_WON_MESSAGE.format(player=player2))

    #diagonals
    winner = check_diagonals(player1, player2)
    return winner

def check_diagonals(player1, player2):
    winner = False
    for player in [player1, player2]:
        if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == player:
            winner = True 
            print(PLAYER_WON_MESSAGE.format(player=player))
        elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == player:
            winner = True
            print(PLAYER_WON_MESSAGE.format(player=player))

    return winner



if __name__ == "__main__":
    print(INTRO_MESSAGE)

    print("Here is the playboard: ")

    display_board_coordinates()
    SIDE_SELECTION_TEXT = ("Player 1, what's your sign? [choose 1 or 2]: \n1: X \n2: O \n>>> "
    )

    while True:
        try:
            choice = int(input(SIDE_SELECTION_TEXT))
            
            if choice == 1:
                player1 = "X"
                player2 = "O"
            elif choice == 2:
                player1 = "O"
                player2 = "X"
            else:
                raise ValueError
            
            print(f"Player 1, you are {player1}")
            print(f"Player 2, you are {player2}")
        except ValueError:
            print("Not an option, please choose 1 or 2")
            continue
        else:
            break

    count = 1
    has_winner = False

    while count < 10 and has_winner == False:
        make_choice(player1, player2, count)
        display_board()
        
        if count == 9:
            print("The board is full. Game over.")
            if not has_winner:
                print("There is a tie. ")

        # Check if here is a winner
        has_winner = check_board_state(player1, player2)
        count += 1

    if has_winner == True:
        print("Game over.")
