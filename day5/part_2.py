with open('input.txt', 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

def convert_char(char):
    """ Convert input to binary so that we can reuse
    the same function for both rows and columns """
    if char == 'F' or char == 'L':
        return 0
    
    return 1

def bsp(line, current, max):
    """ Binary Space Partitioning algorithm """
    char = convert_char(line[0])

    if len(line) == 1:
        if char == 0:
            return current

        return max

    difference = max - current
    half = difference // 2
    upper_half = max - half
    lower_half = current + half

    if char == 0:
        return bsp(line[1:], current, lower_half)

    return bsp(line[1:], upper_half, max)

seats = []

for line in data:
    row = bsp(line[0:7], 0, 127)
    column = bsp(line[7:], 0, 7)
    seat_id = row * 8 + column
    seats.append((row, column, seat_id))

seat_ids = [seat_id for _, _, seat_id in seats]
valid_seats = set(range(min(seat_ids), max(seat_ids)))

print("Missing seat:", valid_seats - set(seat_ids))