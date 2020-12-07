def get_ID(boarding_pass: str):
    minimum = 0
    maximum = 127
    i = 0
    while maximum > minimum:
        delta = maximum - minimum + 1
        change = delta // 2
        letter = boarding_pass[i]
        if letter == 'F':
           maximum -= change 
        if letter == 'B':
            minimum += change
        i += 1
    row = maximum
    
    minimum = 0
    maximum = 7
    while maximum > minimum:
        delta = maximum - minimum + 1
        change = delta // 2
        letter = boarding_pass[i]
        if letter == 'R':
            minimum += change
        if letter == 'L':
            maximum -= change
        i += 1

    column = maximum
    ID = 8 * row + column
    return ID

