import re
from collections import defaultdict
from functional import seq

def apply_bitmask(bitmask, number):
    output = ''

    for i in range(len(bitmask)):
        mask_value = bitmask[i]

        if mask_value == 'X':
            output += number[i]
        else:
            output += bitmask[i]
    
    return output

with open("input.txt", "r") as f:
    data = f.read().split("mask = ")[1:]

memory = defaultdict(int)

for section in data:
    lines = section.splitlines()
    mask = lines[0]

    writes = (seq(lines[1:])
        .map(lambda x: x.strip())
        .map(lambda x: x.split(' = '))
        .map(lambda xy: (xy[0], f'{int(xy[1]):036b}')))

    for write in writes:
        loc, number = write
        print(type(number))
        address = int(re.search(r'[^\D]+', loc)[0])

        masked_number = int(apply_bitmask(mask, number), 2)

        if masked_number > 0:
            memory[address] = masked_number

print(sum(memory.values()))