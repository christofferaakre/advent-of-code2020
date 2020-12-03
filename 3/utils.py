import math

def count_trees(data_file: str = 'formatted.txt', right: int = 1, down: int = 1) -> int:
     with open(data_file, 'r') as file:
            lines = [line for line in file.readlines()]
        
            scaling_factor = math.ceil(len(lines) / len(lines[0]) * right
                    / down) + 2
     data = list()
     for line in lines:
         terrain = list()
         for position in line.replace('\n', '') * scaling_factor :
                terrain.append(int(position))
         data.append(terrain)
     
     trees = 0
     i = 0 
     for i in range(len(data) // down):    
         position = (right * i, down * i)
         x, y = position
         tree = data[y][x] if data[y] else [0 for i in range(len(data[0]))]
         trees += tree
     return trees 
