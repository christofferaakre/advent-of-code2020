import time

import numpy as np

from utils import get_binary_permutations, get_occurences, mask_string

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
memory = dict()

for section in sections:
    mask = section[0].split('= ')[1]
    instructions = section[1:]
    for instruction in instructions:
        address = int(instruction.split(']')[0][4:])
        binary_address = mask_string(f'{address:036b}', mask)
        value = int(instruction.split('= ')[1])

        addresses = list()
        floating = get_occurences('X', mask)
        n = len(floating)
        permutations = [permutation for permutation in
                get_binary_permutations(length=n)]

        for permutation in permutations:
            address = list(binary_address)
            for i, bit in enumerate(permutation):
                index = floating[i]
                address[index] = bit
            address = int(''.join(address), 2)
            addresses.append(address)

        for address in addresses:
            memory[address] = value


result = sum(memory.values())
print(result)
end = time.process_time()
print(f'ran in {end - start} seconds')
