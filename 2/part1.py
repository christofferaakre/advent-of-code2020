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
                'minimum': int(minimum),
                'maximum': int(maximum)
        })

count = 0

for passwd in formatted:
    minimum = passwd['minimum']
    maximum = passwd['maximum']
    password = passwd['password']
    char = passwd['character']
    occurences = len([m.start() for m in re.finditer(char,
      password)])
    if occurences >= minimum and occurences <= maximum:
        count += 1

print(count)
