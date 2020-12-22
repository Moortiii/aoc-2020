from collections import defaultdict
from tqdm import tqdm

with open("input.txt", "r") as f:
    data = f.read()

# Puzzle input
starting_numbers = [int(num) for num in data.split(',')]

# Track the current turn
turn = 1

# Track when starting_numbers were previously mentioned
turns = defaultdict(list)

for number in starting_numbers:
    turns[number].append(turn) 
    turn += 1

last_number = starting_numbers[-1]
next_number = 0

nth_number = 2020

pbar = tqdm(total=nth_number)

for i in range(turn, nth_number + 1):
    #print(f"Turn {turn} - Number: {last_number}")

    if len(turns[last_number]) == 1:
        next_number = 0
        #print(f"{last_number} had not been spoken. Next number: {last_number}")
    else:
        previously_spoken = turns[last_number]
        #print(f"{last_number} has been spoken before, at turns {turns[last_number]}")
        next_number = previously_spoken[-1] - previously_spoken[-2]
        previously_spoken.pop(-2)
        
    #print(f"Next number: {next_number}")
    #print("")

    last_number = next_number
    turns[last_number].append(turn)
    turn += 1
    pbar.update(1)

print(f"Final number: {next_number}")
