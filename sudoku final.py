import copy

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row-1][i] == num:
            return False
        
    for i in range(9):
        if board[i][col-1] == num:
            return False
        
    row = (row-1)//3 * 3
    col = (col-1)//3 * 3
    
    for i in range(row, row + 3):
        for u in range(col, col + 3):
            if board[i][u] == num:
                return False
            
    return True

def solve_sudoku(board):
    for i in range(1, 10):
        for u in range(1, 10):
            if board[i-1][u-1] == 0:
                for n in range(1, 10):
                    if is_valid(board, i, u, n):
                        board[i-1][u-1] = n
                        if (solve_sudoku(board)):
                            return True
                        board[i-1][u-1] = 0
                return False
    return True

def print_board(board):
    for i in range(9):
        print(board[i])

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0], 
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(puzzle):
    print_board(puzzle)
else:
    print("해답을 찾을 수 없습니다.")
