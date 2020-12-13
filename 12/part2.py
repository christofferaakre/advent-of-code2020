import numpy as np

from utils import rotate_vector

with open('input.txt', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

instructions = [(line[0], float(line[1:])) for line in lines]

position = np.array([0, 0]).astype('float') 
waypoint = np.array([10, 1]).astype('float')

north = np.array([0, 1])
south = np.array([0, -1])
west = np.array([-1, 0])
east = np.array([1, 0])

for instruction in instructions:
    command, argument = instruction
    if command == 'F':
        position += argument * waypoint
    elif command == 'N':
        waypoint += argument * north
    elif command == 'S':
        waypoint += argument * south
    elif command == 'E':
        waypoint += argument * east
    elif command == 'W':
        waypoint += argument * west
    elif command == 'L':
        angle = argument * np.pi / 180
        waypoint = rotate_vector(waypoint, theta=angle)
    elif command == 'R':
        angle = argument * np.pi / 180
        waypoint = rotate_vector(waypoint, theta=-angle)
    
distance = round(sum(abs(position)))
print(distance) 

