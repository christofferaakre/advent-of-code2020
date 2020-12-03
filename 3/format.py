with open('input.txt', 'r') as file:
    lines = file.readlines()

with open('formatted.txt', 'w') as file:
    for line in lines:
        file.write(line.replace('.', '0').replace('#', '1'))
