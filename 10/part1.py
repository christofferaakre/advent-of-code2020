with open('input.txt', 'r') as file:
    adapters = [int(line.replace('\n', '')) for line in file.readlines()]

adapters.append(max(adapters) + 3)
adapters.insert(0, 0)

adapters = sorted(adapters)
diffs = list()

for i in range(1, len(adapters)):
    adapter = adapters[i]
    prev = adapters[i-1]
    difference = adapter - prev
    diffs.append(difference)

ones = diffs.count(1)
threes = diffs.count(3)
result = ones * threes
print(result)
