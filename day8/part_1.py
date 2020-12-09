from collections import namedtuple

filename = "input.txt"
#filename = "example_input.txt"

with open(filename, "r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

Instruction = namedtuple('Instruction', ['op', 'has_run'])
instructions = {}

for i, line in enumerate(data):
    instructions[i] = Instruction(op=line, has_run=False)

i = 0
acc = 0

for instruction in instructions.values():
    print(instruction)

while True:
    print("Current op index", i)
    op, _ = instructions[i]
    instructions[i] = instructions[i]._replace(has_run=True)

    if "nop" in op:
        print("Nop detected.")
        print("Moving to next instruction")

    if "acc" in op:
        amount = int(op.split(" ")[1])
        acc += amount
        print("Acc detected", amount)
        print("Accumulator set to", acc)
    
    if "jmp" in op:
        amount = int(op.split(" ")[1])
        next_instruction = (i + amount) % (len(instructions) - 1)
        print("Jump detected:", amount)
        print("Jumping from", i, "to", next_instruction)
        i = next_instruction - 1

    i += 1

    op, has_run = instructions[i]

    if has_run:
        print("Loop detected @", op)
        break

print("Accumulator before loop:", acc)