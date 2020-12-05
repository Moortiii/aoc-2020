with open('example_input.txt', 'r') as f:
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

    # print("Character is: ", char)
    # print("Difference between max-min:", max - current)

    if len(line) == 1:
        #print("Last character is:", char)
        if char == 0:
            return current

        return max

    difference = max - current
    half = difference // 2
    upper_half = max - half
    # lower_half = current + half

    # print("Lower half:", (current, lower_half))
    # print("Upper half:", (upper_half, max))

    if char == 0:
        # print("Taking the lower half.")
        # print("New range is:", (current, upper_half))
        # print("")
        return bsp(line[1:], current, upper_half)

    # print("Taking the upper half.")
    # print("New range is:", (upper_half, max))
    # print("")
    return bsp(line[1:], upper_half, max)

rows = []

for line in data:
    rows.append(bsp(line[0:7], 0, 127))

for row in rows:
    print("Row is:", row)