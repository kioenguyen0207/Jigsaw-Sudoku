from src.modules.constructor import *
from src.modules.find import *
from src.modules.solve import *
import numpy as np

def test_overall():
  result = np.load('src/tests/sample_result.npy')
  sudoku = construct_sudoku_array('Sudoku.txt')
  solve(sudoku)
  assert (result == sudoku).all()