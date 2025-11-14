import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show(b):
    for r in range(3):
        print(f" {b[r * 3]} | {b[r * 3 + 1]} | {b[r * 3 + 2]} ")
        if r < 2:
            print("---+---+---")
def winner_check(b, player):
    if b[0] == player:
        if b[1] == player and b[2] == player:
            return player
        if b[3] == player and b[6] == player:
            return player
        if b[4] == player and b[8] == player:
            return player
    if b[1] == player and b[4] == player and b[7] == player:
        return player
    if b[2] == player:
        if b[4] == player and b[6] == player:
            return player
        if b[5] == player and b[8] == player:
            return player
    if b[3] == player and b[4] == player and b[5] == player:
        return player
    if b[6] == player and b[7] == player and b[8] == player:
        return player
    return None
def winner(b):
    if(winner_check(b, 'X') == None):
        if(winner_check(b, 'O') == None):
            return None
        else:
            return 'O'
    else:
        return 'X'

def play():
    board = [str(i) for i in range(9)]
    turn = "X"
    while any(cell.isdigit() for cell in  board ):
        clear_screen()
        print("Tic-Tac-Toe\n")
        show( board )
        print(f"\n{turn}'s turn!")
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if 0 <= move < 9 and  board[move].isdigit():
            board[move] = turn
            winner_result = winner(board)
            if winner_result:
                clear_screen()
                print("Tic-Tac-Toe\n")
                show(board)
                print(f"\n{winner_result} wins!")
                return
            turn = "O" if turn == "X" else "X"
        else:
            print("Spot is taken or out of range. Try again.")
    clear_screen()
    print("Tic-Tac-Toe\n")
    show(board)
    print("\nIt's a draw!")

play()
