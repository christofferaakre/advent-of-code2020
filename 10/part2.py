with open('input.txt', 'r') as file:
    adapters = [int(line.replace('\n', '')) for line in file.readlines()]

adapters.append(max(adapters) + 3)
adapters.insert(0, 0)

adapters = sorted(adapters)

# dynamig programming
dp = [1]
for i in range(1, len(adapters)):
    dp.append(0)
    j = i - 1
    while i >= 0 and j >= 0 and adapters[i] - adapters[j] <= 3:
        dp[i] += dp[j]
        j -= 1

result = dp[-1]

