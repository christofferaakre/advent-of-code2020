with open('input.txt', 'r') as file:
     data  = file.read()

groups = data.split('\n\n')
   
S = 0
for group in groups:
    questions = sorted(set(group.replace('\n', '')))
    S += len(questions)

print(S)

