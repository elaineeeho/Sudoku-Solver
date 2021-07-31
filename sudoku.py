# I coded this program by following along a youtube video to learn python

from pprint import pprint


def find_next_empty(puzzle):
    # finds the next row, col that has not been filled, returns the row, col 
    # returns (None, None) if there is not one

    for z in range(9):
        for c in range(9): 
            if puzzle[z][c] == -1:
                # returns the row and column
                return z, c
    #returned if no spaces are empty 
    return None, None 

def is_reasonable(puzzle, guess, row, col):
    #decides whether or not the guess is reasonable in the puzzle based on the rules of sudoku
    #returns true or false based on whether or not it is reasonable
    # checks the row first to see if it is reasonable
    row_vals = puzzle[row]
    if guess in row_vals:
        #guess is not valid if it has already been used in puzzle
        return False 
    #checks to see if the value in the column works for the puzzle
    column_vals = [puzzle[i][col] for i in range(9)]
    if guess in column_vals:
        #returns false if the column value cannot be used
        return False

    #checks whether or not the value can be used in the square
    #formulas used to check
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                #returns false if it is not valid
                return False
    #returns true if the row, col fits all the requirements 
    return True

def solve_sudokupuzzle(puzzle):
    
    #chooses a spot in the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # if there are no more spots that are reasonable than the puzzle is done
    if row is None: 
        return True 
    
    # if there is a spot to guess, then the program chooses a number between 1-9
    for guess in range(1, 10): 
        # the guess is checked for validity 
        if is_reasonable(puzzle, guess, row, col):
           #places the guess in the spot if it is a reasonable answer
            puzzle[row][col] = guess
            if solve_sudokupuzzle(puzzle):
                return True
        
        #tries a new number if the guess does not work or "true" is not returned in the program
        puzzle[row][col] = -1

    # if all options are tried and true is still not returned, the puzzle is deemed "unsolveable"
    return False

if __name__ == '__main__':
    testingBoard = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudokupuzzle(testingBoard))
    pprint(testingBoard)