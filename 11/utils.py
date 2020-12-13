import numpy as np

def get_occupied_seats(grid):
    return np.count_nonzero(grid == '#')


