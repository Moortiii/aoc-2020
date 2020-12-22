import re
import itertools
from collections import defaultdict
from functional import seq

def permute_address(bitmask, decimal_address):
    floating_bits = len([c for c in bitmask if c == 'X'])
    permutations = [
        list(seq) for seq in itertools.product("01", repeat=floating_bits)]

    addresses = []

    for permutation in permutations:
        address = ''
        j = 0

        for i, bit in enumerate(bitmask):
            if bit == 'X':
                address += permutation[j]
                j += 1
            elif bit == '0':
                address += decimal_address[i]
            else:
                address += '1'
                
        addresses.append(address)

    return addresses

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
        decimal_address = re.search(r'[^\D]+', loc)[0]
        masked_address = f'{int(decimal_address):036b}'

        addresses = permute_address(mask, masked_address)

        for address in addresses:
            memory[int(address, 2)] = int(number, 2)

print(sum(memory.values()))