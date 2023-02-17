#AI Sudoku Solver
#Yoon Kim
#Februrary 16, 2023


#Initial sudoku board
sudoku_board = [[7,8,0,4,0,0,1,2,0],
                [6,0,0,0,7,5,0,0,9],
                [0,0,0,6,0,1,0,7,8],
                [0,0,7,0,4,0,2,6,0],
                [0,0,1,0,5,0,9,3,0],
                [9,0,4,0,6,0,0,0,5],
                [0,7,0,3,0,0,0,1,2],
                [1,2,0,0,0,7,4,0,0],
                [0,4,9,2,0,6,0,0,7],
]

#Variables for loop
global rows 
global cols 

rows = len(sudoku_board)
cols = len(sudoku_board[0])


#Function to print the board
def set_board(board):
    for i in range(rows):
        if i!=0 and i%3 == 0:
            print('-----------------------')

        for j in range(cols):
            if j != 0 and j%3 == 0:
                print(' | ', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')


#Function to determine if a block is empty
def is_empty(board):
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                return (i,j)
            

#Function to verify if a number is in the right block
def correct(board, num, pos): #pos = (i, j)

    #Checks row if the number is correct
    for i in range(rows):
        if num == board[pos[0]][i] and pos[1] != i:
            return False
        
    #Checks Columns
    for j in range(cols):
        if num == board[j][pos[1]] and pos[0] != j:
            return False
        
    #Checking Square
    x_square = pos[1] // 3
    y_square = pos[0] // 3

    x_start = x_square * 3
    x_stop = x_square * 3 + 3

    y_start = y_square * 3
    y_stop = y_square * 3 + 3

    for i in range(y_start, y_stop):
        for j in range(x_start, x_stop):
            if num == board[i][j] and (i,j) != pos:
                return False
    
    return True

#Function for solving the sudoku board
#Utilizes backtracking algorithm
def solve (board):
    if not is_empty(board):
        return True
    else:
        row, col = is_empty(board)
    
    for i in range(1, 10):
        if correct(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0

    return False


#Results
print("Before: ")
set_board(sudoku_board)
solve(sudoku_board)
print()
print()
print("After: ")
set_board(sudoku_board)