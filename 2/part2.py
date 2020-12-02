import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

formatted = []
for line in lines:
    split = line.replace('\n', '').split(': ')
    password = split[1]
    split2 = split[0].split(' ')
    character = split2[1]
    rang = split2[0].split('-')
    minimum = rang[0]
    maximum = rang[1]
    formatted.append({
                'password': password,
                'character': character,
                'minimum': int(minimum) - 1,
                'maximum': int(maximum) - 1
        })

count = 0

for passwd in formatted:
    password = passwd['password']
    minimum = passwd['minimum']
    maximum = passwd['maximum']
    char = passwd['character']

    index_count = 0
    for index in [minimum, maximum]:
        character = password[index]
        if character == char:
            index_count += 1

    if index_count == 1:
        count += 1

print(count)
