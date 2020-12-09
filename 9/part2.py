import numpy as np

with open("input.txt", "r") as file:
    numbers = [int(line.replace("\n", "")) for line in file.readlines()]

with open("output.txt", "r") as file:
    target_number = int(file.read())


start = 0
found = None

while not found:
    S = 0
    i = start
    adds = list()
    while S < target_number:
        number = numbers[i]
        if number == target_number:
            break
        S += number
        adds.append(number)
        i += 1
        if S == target_number:
            found = adds
            break
    start += 1


result = min(found) + max(found)
print(result)
