N = 8  
def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print("\n" + "-" * 20 + "\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row):
    if row >= N:
        print_solution(board)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve_nqueens(board, row + 1) or res
            board[row][col] = 0  
    return res


if __name__ == "__main__":
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens(board, 0):
        print("No solution exists")
