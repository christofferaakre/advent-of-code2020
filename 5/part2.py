from utils import get_ID

from IPython import embed
with open('input.txt', 'r') as file:
    boarding_passes = [line.replace('\n', '') for line in file.readlines()]


IDs = list()
for boarding_pass in boarding_passes:
    ID = get_ID(boarding_pass)
    IDs.append(ID)


my_ID = None

for x in range(min(IDs), max(IDs) + 1):
    if x in IDs:
        continue
    else:
        my_ID = x
        break
print(my_ID)
