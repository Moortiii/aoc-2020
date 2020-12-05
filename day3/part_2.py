with open("input.txt", "r") as f:
    data = f.readlines()
    
original_data = [line.strip() for line in data]

steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []

for step in steps:
    data = original_data

    current_column = 0
    current_row = 0
    trees_encountered = 0
    step_size_x = step[0]
    step_size_y = step[1]

    # pre-compute how many times we have to repeat the pattern
    original_pattern_width = len(data[0])
    number_of_rows = len(data) + step_size_y
    number_of_colums = (number_of_rows * step_size_x) + 1
    repetitions_needed = (number_of_colums // original_pattern_width) + 1

    # print("Step size:", step[1], ",", step[0])
    # print("Pattern height:", len(data))
    # print("Number of rows:", number_of_rows)
    # print("Number of columns:", number_of_colums)
    # print("Original pattern width:", original_pattern_width)
    # print("Number of repetitions:", repetitions_needed)
    # print("")

    # repeat the biome pattern, could also do
    # modulo wrap-around
    data = [(line * repetitions_needed) for line in data]

    pattern_width = len(data[0])

    while True:
        current_column += step_size_x
        current_row += step_size_y

        if current_column > len(data[0]) - 1 or current_row > len(data) - 1:
            break

        square = data[current_row][current_column]
            
        if square == '#':
            new_line = list(data[current_row])
            new_line[current_column] = 'X'
            data[current_row] = ''.join(new_line)
            trees_encountered += 1
        else:
            new_line = list(data[current_row])
            new_line[current_column] = 'O'
            data[current_row] = ''.join(new_line)
        
    results.append(trees_encountered)

print(results)