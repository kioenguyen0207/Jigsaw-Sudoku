import numpy as np
import argparse
from src.modules.constructor import *
from src.modules.find import *
from src.modules.solve import *

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Sudoku solver')
  parser.add_argument('-f','--filename', help='Path to data file', default='sudoku.txt')
  args = parser.parse_args()

  sudoku = construct_sudoku_array(args.filename)
  solve(sudoku)
  print(sudoku)