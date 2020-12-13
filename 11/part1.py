import time
import numpy as np
from utils import get_occupied_seats

with open('input.txt', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

initial_grid = list()
for line in lines:
    cells = list()
    for cell in line:
        cells.append(cell)
    initial_grid.append(cells)

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


initial_grid = np.array(initial_grid)
grid = initial_grid
done = False

start = time.process_time()
while not done:

    new_grid = get_new_grid(grid)
    if np.array_equal(grid, new_grid): 
         done = True
    

    grid = np.array(new_grid)
end = time.process_time()

print(get_occupied_seats(grid))
print(f'ran in {end - start} seconds')
