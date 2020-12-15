import time

import numpy as np

start = time.process_time()

with open('input.txt', 'r') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]

lines.append('END OF FILE')
sections = list()
i = 0
section = list()
for line in lines:
    if 'mask = ' in line or 'END OF FILE' in line:
        i += 1
        if len(section) > 0:
            sections.append(section)
            section = list()
    section.append(line)

mask = 'X' * 36
memory_size = 2 ** 16
memory = list(np.zeros(shape=(memory_size), dtype=int ))

for section in sections:
    mask = section[0].split('= ')[1]
    instructions = section[1:]
    for instruction in instructions:
        address = int(instruction.split(']')[0][4:])
        value = int(instruction.split('= ')[1])
        binary = f'{value:036b}'
        masked = list()
        for i in range(36):
            if mask[i] == '0':
                masked.append('0')
            elif mask[i] == '1':
                masked.append('1')
            elif mask[i] == 'X':
                masked.append(binary[i])
        masked = ''.join(masked)
        masked_value = int(masked, 2)
        memory[address] = masked_value

result = sum(memory)
print(result)
end = time.process_time()
print(f'ran in {end - start} seconds')
