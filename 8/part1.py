with open("input.txt", "r") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

# instructions will be encoded as tuples (command, argument)
instructions = list()

for line in lines:
    instruction = (line.split(" ")[0], int(line.split(" ")[1]))
    instructions.append(instruction)

lines_executed = list()
accumulator = 0

i = 0
no_infinite_loop = True

while no_infinite_loop:
    if i in lines_executed:
        no_infinite_loop = False
        break
    lines_executed.append(i)
    command, argument = instructions[i]

    if command == "nop":
        i += 1
        continue
    if command == "acc":
        accumulator += argument
        i += 1
        continue
    if command == "jmp":
        i += argument
        continue

print(accumulator)
