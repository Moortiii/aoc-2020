from collections import namedtuple
from tqdm import tqdm
from copy import deepcopy

filename = "input.txt"

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

    if op_text in "nop":
        instruction_set[line_number] = instruction_set[line_number]._replace(op=f'jmp {amount}')
    else:
        instruction_set[line_number] = instruction_set[line_number]._replace(op=f'nop {amount}')

    return instruction_set

def run_instructions(_set):
    i = 0
    acc = 0
    iterations = 0

    while True:
        if i == len(_set):
            return acc
        
        if iterations > 100000:
            return -1

        op, _ = _set[i]

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
    result = run_instructions(_set)

    if result != -1:
        results.append(result)

print(results)