def is_safe(board, row, col, n):
    
    # condition 1 -> checking previous columns
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    # condition 2 -> checking upper diagonal ( ofc left )
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # condition 3 -> checking lower diagonal ( ofc left )
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    
    return True

def solve_n_queens(board, col, n):

    if col >= n:
        return True
    
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, col+1, n):
                return True

            board[row][col] = 0
    return False

# ofc to print board and to flex
def print_board(board):
    for row in board:
        print(row)

# start func -> to create board list and other stuff
def start(n):

    # creating board to flex
    board = [[0] * n for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print_board(board)

    else:
        print("No solution exists!")

n = 4
start(n)

