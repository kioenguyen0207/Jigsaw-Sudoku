import numpy as np
from .find import *

def solve(sudoku_array):
    empty_index = find_empty(sudoku_array)
    if not empty_index:
        return True
    available_numbers = find_available_numbers(sudoku_array, empty_index[0], empty_index[1])
    if len(available_numbers) == 0:
        return False
    for x in available_numbers:
        sudoku_array[empty_index] = x
        if solve(sudoku_array):
            return True
        sudoku_array[empty_index] = 0
    return False