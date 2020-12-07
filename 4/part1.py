import ast
from IPython import embed

with open('formatted.txt', 'r') as file:
     passports = ast.literal_eval(file.read())

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

count = 0

for passport in passports:
    valid = 1   
    for field in required_fields:
        if field not in passport.keys():
            valid = 0
            break

    count += valid

print(f'{count} / {len(passports)} passports are valid')
