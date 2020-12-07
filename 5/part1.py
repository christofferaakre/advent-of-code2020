from utils import get_ID

with open('input.txt', 'r') as file:
    boarding_passes = [line.replace('\n', '') for line in file.readlines()]

highest_ID = 0

for boarding_pass in boarding_passes:
    ID = get_ID(boarding_pass)
    if ID > highest_ID:
        highest_ID = ID

print(highest_ID)

