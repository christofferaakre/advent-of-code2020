import numpy as np

def get_new_grid(grid):
    new_grid = np.array(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            cell = grid[i][j]
            neighbors = list()
            if i > 0:
                neighbors.append(grid[i-1][j])
                if j > 0:
                    neighbors.append(grid[i-1][j-1])
                if j < grid.shape[1] - 1:
                    neighbors.append(grid[i-1][j+1])
            
            if j > 0:
                neighbors.append(grid[i][j-1])
            if j < grid.shape[1] - 1:
                neighbors.append(grid[i][j+1])
            
            if i < grid.shape[0] - 1 :
                neighbors.append(grid[i+1][j])
                if j > 0:
                    neighbors.append(grid[i+1][j-1])
                if j < grid.shape[1] - 1:
                    neighbors.append(grid[i+1][j+1])

            if cell == 'L' and '#' not in neighbors:
                new_grid[i][j] = '#'
            if cell == '#' and neighbors.count('#') >= 4:
                new_grid[i][j] = 'L'
    return new_grid

def get_occupied_seats(grid):
    return np.count_nonzero(grid == '#')


