import numpy as np

from utils import rotate_vector

with open('input.txt', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

instructions = [(line[0], float(line[1:])) for line in lines]

position = np.array([0, 0]).astype('float') 
facing = np.array([1, 0])

north = np.array([0, 1])
south = np.array([0, -1])
west = np.array([-1, 0])
east = np.array([1, 0])

for instruction in instructions:
    command, argument = instruction
    if command == 'F':
        position += argument * facing
    elif command == 'N':
        position += argument * north
    elif command == 'S':
        position += argument * south
    elif command == 'E':
        position += argument * east
    elif command == 'W':
        position += argument * west
    elif command == 'L':
        angle = argument * np.pi / 180
        facing = rotate_vector(facing, theta=angle)
    elif command == 'R':
        angle = argument * np.pi / 180
        facing = rotate_vector(facing, theta=-angle)
    
distance = round(sum(abs(position)))
print(distance) 

