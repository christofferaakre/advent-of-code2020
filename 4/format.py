with open('input.txt', 'r') as file:
    big_str = file.read()


data = big_str.split('\n\n')

passports = []
for passport_data in data:
    passport = {}
    sp = passport_data.split('\n')
    for splits in sp:
        fields = splits.split(' ')
        for field in fields:
            if len(field) > 2:
                key, value = field.split(':')
                passport[key] = value
    passports.append(passport)

with open('formatted.txt', 'w') as file:
    file.write(str(passports))

print(f'formatted file input.txt. new file is formatted.txt. {len(passports)} passports found')
