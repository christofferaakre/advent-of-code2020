with open("input.txt", "r") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

P = list()

instructions = list()

for i, line in enumerate(lines):
    command = line.split(" ")[0]
    argument = int(line.split(" ")[1])
    instruction = (command, argument)
    if command == "jmp" or command == "nop":
        P.append({"line": i, "command": command, "argument": argument})
    instructions.append(instruction)


terminated = False

for p in P:
    if terminated:
        break
    line = p["line"]
    command = p["command"]
    argument = p["argument"]
    new_command = "jmp" if command == "nop" else "nop"

    # we need a copy of the list, not a reference,
    # so we cannot simply write new_instructions = instructions
    new_instructions = list(instructions) 

    new_instructions[line] = (new_command, argument)

    lines_executed = list()
    accumulator = 0

    i = 0
    no_infinite_loop = True

    failed_at = None
    while no_infinite_loop:
        if i >= len(new_instructions):
            terminated = True
            break
        command, argument = new_instructions[i]

        if i in lines_executed:
            no_infinite_loop = False
            failed_at = i
            break

        lines_executed.append(i)

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
