# TODO: check of 3x3 in puzzle guess valid

def find_valid(puzzle, row, col, guess):
  
  # check for row
  if guess in puzzle[row]:
    return False
  
  # check for col  
  # puzzle[0][2], puzzle[1][2], puzzle[2][2] by this you will get each items in col 
  col_val = [puzzle[i][col] for i in range(9)]
  if guess in col_val:
    return False
  
  # and for check 3x3
  

def sudoku(puzzle):
  pass

