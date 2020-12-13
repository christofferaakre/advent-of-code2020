import numpy as np

from utils import get_new_grid, get_occupied_seats

with open('input.txt', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

initial_grid = list()
for line in lines:
    cells = list()
    for cell in line:
        cells.append(cell)
    initial_grid.append(cells)

initial_grid = np.array(initial_grid)
grid_history = [initial_grid]

done = False
count = 0


grid = initial_grid
while not done:

    new_grid = get_new_grid(grid)
    count += 1
    if np.array_equal(grid, new_grid): 
         done = True
    

    grid = np.array(new_grid)


print(get_occupied_seats(grid))
