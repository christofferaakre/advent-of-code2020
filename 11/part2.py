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
            directions = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)
                    ]
            seen_directions = set()
            count = 0
            while len(seen_directions) < len(directions):
                count += 1
                for direction in directions:
                    if direction not in seen_directions:
                        x = i + count * direction[0]
                        y = j + count * direction[1]
                        if x < 0 or y < 0:
                            seen_directions.add(direction)
                            continue
                        try:
                            neighbor = grid[x][y]
                            if neighbor != '.':
                                seen_directions.add(direction)
                                neighbors.append(neighbor)

                        except:
                            seen_directions.add(direction)

            if cell == 'L' and '#' not in neighbors:
                new_grid[i][j] = '#'
            if cell == '#' and neighbors.count('#') >= 5:
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
