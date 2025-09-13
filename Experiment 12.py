
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
   
    for row in board:
        if all(s == player for s in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        print(f"Player {player}'s turn")
        
     
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != " ":
                print("Cell already occupied, try again!")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter numbers between 0 and 2.")
            continue
        
        board[row][col] = player
        
        
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
      
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        
        player = "O" if player == "X" else "X"


tic_tac_toe()
