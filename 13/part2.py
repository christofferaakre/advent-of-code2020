import math
import time
from functools import reduce
from operator import mul

with open('input.txt', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

earliest = int(lines[0])
all_buses = lines[1].split(',')
notes = list()
for bus in all_buses:
    # caveman try except to convert the number strings
    # to integers and keep the 'x's as strings
    try:
        int(bus)
        notes.append(int(bus))
    except:
        notes.append(bus)

start = time.process_time()

done = False
t = 0

while not done:
    satisifed = list()
    for i, note in enumerate(notes):
        if note == 'x':
            continue
        m = (t + i) % note
        if m == 0:
            satisifed.append(note)
            if i == len(notes) - 1:
                done = True
                break
            continue
        else:
            t += reduce(mul, satisifed, 1)
            break

        


end = time.process_time()
result = t
print(result)
print(f'ran in {end - start} seconds')
