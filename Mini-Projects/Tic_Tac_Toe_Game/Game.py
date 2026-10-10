 
# Tic-Tac-Toe Game

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def has_won(player):
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [6, 4, 2]]
    for a, b, c in lines:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False


def has_tied():
    for spot in board:
        if spot != "X" and spot != "O":
            return False
    return True


# ----+--Main Game--+----
print("Welcome to Tic Tac Toe!")
player = "X"

while True:
    show_board()
    choice = input(f"Player {player} Type a number from 1 to 9 : ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Please select a number from 1 to 9")
        continue

    spot = int(choice) - 1

    if board[spot] == "X" or board[spot] == "O":
        print("Please select another number, this one is already taken")
        continue

    board[spot] = player

    if has_won(player):
        show_board()
        print(f"Player {player} has WON!!")
        break

    if has_tied():
        show_board()
        print("The game has Tied!!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"


