import numpy as np

with open("input.txt", "r") as file:
    numbers = [int(line.replace("\n", "")) for line in file.readlines()]

length = 25
not_found = None

for k in range(length, len(numbers)):
    number = numbers[k]
    found = False
    for i_, j_ in np.ndindex(length, length):
        i = i_ + k - length
        j = j_ + k - length
        if i != j:
            x = numbers[i]
            y = numbers[j]
            if number == x + y:
                found = True
                break
    if not found:
        not_found = number
        break


print(not_found)
with open('output.txt', 'w') as file:
    file.write(str(not_found))
