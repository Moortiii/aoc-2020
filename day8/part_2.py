from collections import namedtuple
from tqdm import tqdm
from copy import deepcopy

filename = "input.txt"
#filename = "example_input.txt"

with open(filename, "r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

Instruction = namedtuple('Instruction', ['op', 'has_run'])
instructions = {}

for i, line in enumerate(data):
    instructions[i] = Instruction(op=line, has_run=False)

def create_instruction_set(_instructions, line_number):
    instruction_set = deepcopy(_instructions)

    op, _ = instruction_set[line_number]

    if op.split(" ")[0] not in ["jmp", "nop"]:
        return instruction_set

    amount = op.split(" ")[1]
    op_text = op.split(" ")[0]

    #print(instruction_set[line_number])

    if op_text in "nop":
        instruction_set[line_number] = instruction_set[line_number]._replace(op=f'jmp {amount}')
        #print(instruction_set[line_number])
    else:
        instruction_set[line_number] = instruction_set[line_number]._replace(op=f'nop {amount}')
        #print(instruction_set[line_number])

    #print("")

    return instruction_set

def run_instructions(_set):
    i = 0
    acc = 0
    iterations = 0

    while True:
        if i == len(_set) or i == len(_set) - 1:
            print(i)
            return 999
        
        if iterations > 100000:
            return -1

        op, _ = instructions[i]
        instructions[i] = instructions[i]._replace(has_run=True)

        if "acc" in op:
            amount = int(op.split(" ")[1])
            acc += amount
        
        if "jmp" in op:
            amount = int(op.split(" ")[1])
            next_instruction = (i + amount)
            i = next_instruction - 1

        i += 1
        iterations += 1

instruction_sets = [
    create_instruction_set(instructions, i) for i in range(len(instructions))]

results = []

for _set in tqdm(instruction_sets):
    #for op, _ in _set.values():
        #print(op)
    
    #print("")
    result = run_instructions(_set)

    if result != -1:
        results.append(result)

print(results)