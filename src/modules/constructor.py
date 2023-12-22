import numpy as np

def construct_sudoku_array(fileName = 'Sudoku.txt'):
    with open(fileName) as f:
        file_content = list(filter((lambda x: x != ',' and x != '\n'), list(f.read())))
    sudoku_array = np.array(file_content, dtype=int).reshape(9, 9)
    return sudoku_array