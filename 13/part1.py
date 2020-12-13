import math

with open('input.txt', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]


earliest = int(lines[0])
all_buses = lines[1].split(',')
buses = [int(bus) for bus in all_buses if bus != 'x']

lowest = 10000000
best_bus = 0

for bus in buses:
    time_to_wait = math.ceil(earliest / bus) * bus - earliest
    if time_to_wait < lowest:
        lowest = time_to_wait
        best_bus = bus


result = lowest * best_bus
print(result)



