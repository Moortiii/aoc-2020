with open('example_input.txt', 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

def split(line, current, max):
    char = line[0]
    print("Character is: ", char)
    print("Difference between max-min:", max - current)

    if len(line) == 1:
        print("Last character is:", char)

        if char == 'F':
            return current
        else:
            return max

    difference = max - current
    half = difference // 2

    lower_half = current + half
    upper_half = max - half

    print("Lower half:", (current, lower_half))
    print("Upper half:", (upper_half, max))

    if char == 'F':
        print("Taking the lower half.")
        print("New range is:", (current, upper_half))
        print("")
        return split(line[1:], current, upper_half)
    elif char == 'B':
        print("Taking the upper half.")
        print("New range is:", (upper_half, max))
        print("")
        return split(line[1:], upper_half, max)
    

# binary space partitioning
def bsp(line, max):
    characters = list(line)

    current = 0
    rows = (current, max)

    for character in characters:
        half = max // 2

        if character == 'B':
            bsp()
            rows = (current, half)
        elif character == 'F':
            rows = (half, max)

    print(characters)

rows = []

for line in data:
    rows.append(split(line[0:7], 0, 127))

for row in rows:
    print("Row is:", row)