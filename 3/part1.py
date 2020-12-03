from IPython import embed
import math
right = 3
down = 1


with open('formatted.txt', 'r') as file:
    lines = [line for line in file.readlines()]


scaling_factor = math.ceil(len(lines) / len(lines[0]) * right / down) + 1

data = list()
for line in lines:
    terrain = list()
    for position in line.replace('\n', '') * scaling_factor :
           terrain.append(int(position))
    data.append(terrain)


trees = 0

for i in range(len(data) // down):
    position = (right * i, down * i)
    x, y = position
    print(x, y)
    tree = data[y][x]
    trees += tree 

print(trees)

