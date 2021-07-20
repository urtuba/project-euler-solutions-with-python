# Project Euler 11 - Largest product in a grid
# GitHub: urtuba

import numpy as np

def load_2d_array(filename: str) -> np.ndarray:
    '''
    Reads a txt file into 2d numpy integer array.

    :param filename: name of the txt file.
    :return: 2d numpy array
    '''
    with open(filename, 'r') as file:
        array_2d = np.loadtxt(filename, dtype=np.int32, ndmin=2)
    return array_2d

def largest_product_of_quarts(array_2d: np.ndarray) -> int:
    '''
    Returns largest product of four adjacent integers in the given 2D array.
    Adjacency can occur horizontally, vertically or diagonally.

    :param array_2d: 2d array, n x n.
    :return: largest product of 4 adjacent numbers
    '''
    
    # hidden helper functions
    def _max_quart_product_of_rows(array_2d: np.ndarray) -> int:
        dim = len(array_2d)
        maximum = 0
        for row in array_2d:
            for i in range(dim-3):
                temp = np.product(row[i:i+4])
                if maximum < temp: maximum = temp
        return maximum

    def _max_quart_product_of_cols(array_2d: np.ndarray) -> int:
        dim = len(array_2d)
        maximum = 0
        for col in array_2d.transpose():
            for i in range(dim-3):
                temp = np.product(col[i:i+4])
                if maximum < temp: maximum = temp
        return maximum

    def _max_quart_product_of_diags(array_2d: np.ndarray) -> int:
        dim = len(array_2d)
        diags = [array_2d.diagonal(i) for i in range(-dim+1, dim)]
        diags.extend([array_2d[:,::-1].diagonal(i) for i in range(-dim+1, dim)])
        diags = list(filter(lambda n: len(n) > 3, diags))

        maximum = 0
        for diag_line in diags:
            diag_len = len(diag_line)
            for i in range(diag_len-3):
                temp = np.product(diag_line[i:i+4])
                if maximum < temp: maximum = temp
        return maximum

    # actual function body
    rows_max = _max_quart_product_of_rows(array_2d)
    cols_max = _max_quart_product_of_cols(array_2d)
    diags_max = _max_quart_product_of_diags(array_2d)
    return max(rows_max, cols_max, diags_max)

if __name__ == '__main__':
    matrix = load_2d_array('s011-input.txt')
    result = largest_product_of_quarts(matrix)
    print (result)