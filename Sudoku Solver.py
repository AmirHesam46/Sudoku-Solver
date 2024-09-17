class Solution(object):
    def solveSudoku(self, board):
        def isValid(board, row, col, num):
            # Check if num is not in the current row
            for i in range(9):
                if board[row][i] == num:
                    return False

            # Check if num is not in the current column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check if num is not in the current 3x3 sub-box
            boxRowStart = (row // 3) * 3
            boxColStart = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[boxRowStart + i][boxColStart + j] == num:
                        return False

            return True

        def backtrack(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if isValid(board, i, j, num):
                                board[i][j] = num
                                if backtrack(board):
                                    return True
                                board[i][j] = '.'  # Backtrack
                        return False
            return True

        backtrack(board)

# Test the solveSudoku function with a sample Sudoku puzzle
def printBoard(board):
    for row in board:
        print(" ".join(row))

# Example Sudoku puzzle
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

print("Original Sudoku board:")
printBoard(board)

solver = Solution()
solver.solveSudoku(board)

print("\nSolved Sudoku board:")
printBoard(board)