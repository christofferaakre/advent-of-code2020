import ast
from IPython import embed

with open('formatted.txt', 'r') as file:
     passports = ast.literal_eval(file.read())

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

valid_passports = []

for passport in passports:
    valid = 1   
    for field in required_fields:
        if field not in passport.keys():
            valid = 0
            break

    if valid:
        valid_passports.append(passport)


count = 0

for passport in valid_passports:
    byr = int(passport['byr'])
    iyr = int(passport['iyr'])
    eyr = int(passport['eyr'])
    hgt = passport['hgt']
    hcl = passport['hcl']
    ecl = passport['ecl']
    pid = passport['pid']

    valid = 1

    if not (1920 <= byr <= 2002):
        valid = 0
        continue

    if not (2010 <= iyr <= 2020):
        valid = 0
        continue

    if not (2020 <= eyr <= 2030):
       valid = 0
       continue

    if 'cm' in hgt:
       height = int(hgt.split('cm')[0])
       if not (150 <= height <= 193):
           valid = 0
           continue

    elif 'in' in hgt:
        height = int(hgt.split('in')[0])
        if not (59 <= height <= 76):
            valid = 0
            continue

    else:
        valid = 0
        continue

        
    if not (len(hcl) == 7):
        valid = 0
        continue

    allowed_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
            'b', 'c', 'd', 'e', 'f']
    for char in hcl[1:]:
        if not (char in allowed_chars):
            valid = 0
            break
    if not valid:
        continue

    if not (ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        valid = 0
        continue


    if not (len(pid) == 9):
        valid = 0
        continue

    for char in pid:
        if not (char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            valid = 0
            break
    if not valid:
        continue

    count += valid

print(f'{count} / {len(passports)} are valid')
