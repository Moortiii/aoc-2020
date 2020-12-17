from copy import deepcopy
from tqdm import tqdm
import itertools

with open("input.txt", "r") as f:
    data = f.readlines()

jolt_ratings = [int(line.strip()) for line in data]
jolt_ratings.append(0) # charging outlet
jolt_ratings = sorted(jolt_ratings)
jolts = {}

for i, rating in enumerate(jolt_ratings):
    jolts[rating] = [
        j for j in range(rating + 1, rating + 4) if j in jolt_ratings]

_max = max(jolt_ratings)
jolts[_max] = [_max + 3] # final adapter
jolts[_max + 3] = []

acc = 0

def recurse(jolts, _key, acc):
    return

    for jolt in jolts.items():
        key, values = jolt
        print(key)

        if key < _key:
            continue

        if len(values) > 1:
            acc += len(values) - 1
            return recurse(jolts, key, acc)

        return acc

def search(jolts, key, acc):
    for jolt in jolts.items():
        key, values = jolt

        if len(values) > 1:
            for value in values:
                return search(jolts, key, acc)
    
    return acc

for jolt in jolts.items():
    key, values = jolt

    if len(values) > 1:
        for i in range(len(values)):
            if jolts[]
    print(key, values)

# loop over all the items in the dict
# if we hit a key with more than one item in it
    # add the number of items - 1 to the accumulator
    # select one of the items and go back to the start















    #print(key, values)


# permutations = itertools.   (*sorted(values))

# with open("output.txt", "w") as f:
#     for permutation in permutations:
#         x = ''.join(str(list(set(permutation))))
#         f.write(x)
#         f.write('\n')



# print("Calculated all permutations")

# valid = []

# for permutation in tqdm(permutations):
#     permutation = list(set(permutation))
#     current_power = 0

#     for jolt in permutation:
#         if jolt > current_power + 3:
#             break

#         current_power = jolt
#     else:
#         valid.append(permutation)

