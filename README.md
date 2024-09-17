# Sudoku Solver

This Python project implements a Sudoku solver using the backtracking algorithm. It takes a 9x9 Sudoku puzzle and fills in the missing numbers (represented by .) to complete the puzzle according to the rules of Sudoku.

## Table of Contents
- [Description](#description)
- [How the Algorithm Works](#how-the-algorithm-works)
- [Code Explanation](#code-explanation)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [Conclusion](#conclusion)

## Description

The Sudoku Solver solves any valid 9x9 Sudoku puzzle using a backtracking approach. The goal of Sudoku is to fill the grid with digits (1–9) such that:
1. Each row contains the digits 1–9 without repetition.
2. Each column contains the digits 1–9 without repetition.
3. Each of the nine 3x3 sub-grids (boxes) contains the digits 1–9 without repetition.

## How the Algorithm Works

The algorithm uses backtracking, 1. Copy the code to your Python environment.
2. Define your Sudoku board using a 9x9 grid, where empty cells are represented by ..
3. Call the solveSudoku function to solve the puzzle.
4. Use printBoard to print both the original and solved Sudoku boards.

### Steps to Run:
1. Set up the board with initial values.
2. Call the solveSudoku method to solve the board.
3. Print the solved board to verify the solution.

## Example

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
## Requirements

- Python 3.x installed
- No external libraries are needed

## Conclusion

This project provides an effective way to solve Sudoku puzzles using the backtracking algorithm. Feel free to extend this project or integrate it with a graphical interface to make it more interactive!

---

Let me know if you'd like to tweak any part of the README!a brute-force technique to search for the correct solution by trying all possibilities.

1. It scans the grid to find an empty cell.
2. For the empty cell, it tries placing each number from 1 to 9 and checks if it is valid.
3. If placing the number is valid, it moves forward and recursively fills in the next empty cell.
4. If placing a number leads to an invalid state, the algorithm backtracks, undoes the move, and tries the next number.
5. The process repeats until the puzzle is solved.

## Code Explanation

### 1. isValid function
This helper function checks if placing a specific number (num) in a particular cell (row, column) is valid. The function validates this by checking:
- The row: Ensures that num doesn't already exist in the current row.
- The column: Ensures that num doesn't exist in the current column.
- The 3x3 sub-grid: Ensures that num is not present in the 3x3 box that the cell belongs to.

def isValid(board, row, col, num):
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 sub-grid
    boxRowStart = (row // 3) * 3
    boxColStart = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[boxRowStart + i][boxColStart + j] == num:
                return False

    return True
### 2. backtrack function
The main recursive function that solves the puzzle. It works by:
- Finding an empty cell (denoted by .).
- Attempting to fill it with digits from 1 to 9.
- Checking if the placement is valid using isValid. If it is valid, it proceeds by calling itself recursively to solve the next empty cell.
- If no valid number can be placed, it backtracks by resetting the current cell and trying the next number.

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
### 3. solveSudoku function
The main function that triggers the solving process. It initializes the backtracking by calling the backtrack function.

def solveSudoku(self, board):
    backtrack(board)
### 4. printBoard function
A utility function to print the Sudoku board in a human-readable format.

def printBoard(board):
    for row in board:
        print(" ".join(row))
## Usage
1. Copy the code to your Python environment.
2. Define your Sudoku board using a 9x9 grid, where empty cells are represented by ..
3. Call the solveSudoku function to solve the puzzle.
4. Use printBoard to print both the original and solved Sudoku boards.

### Steps to Run:
1. Set up the board with initial values.
2. Call the solveSudoku method to solve the board.
3. Print the solved board to verify the solution.

## Example

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
## Requirements

- Python 3.x installed
- No external libraries are needed

## Conclusion

This project provides an effective way to solve Sudoku puzzles using the backtracking algorithm. Feel free to extend this project or integrate it with a graphical interface to make it more interactive!
