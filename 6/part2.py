from IPython import embed

with open('input.txt', 'r') as file:
     data  = file.read()

groups = data.split('\n\n')
   
S = 0
for group in groups:
    members = group.split('\n')
    members = [member for member in members if len(member) > 0]
    answers = list()
    count = 0
    N = len(members)
    for member in members:
        for question in member:
            answers.append(question)

    unique_questions = set(answers)
    for question in unique_questions:
        occurences = answers.count(question)
        if occurences == N:
            count += 1
    S += count
            
        
print(S)
