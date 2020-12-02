with open('input.txt', 'r') as file:
    lines = file.readlines()
data = [int(line.replace('\n', '')) for line in lines]

for i in range(len(data)):
    for j in range(len(data)):
            S = data[i] + data[j]
            if S == 2020:
                product = data[i] * data[j] 
                print(product)
