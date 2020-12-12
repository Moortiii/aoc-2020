from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

jolt_ratings = [int(line.strip()) for line in data]
jolt_ratings.append(0) # charging outlet

jolts = {}

for i, rating in enumerate(jolt_ratings):
    jolts[rating] = [
        j for j in range(rating + 1, rating + 4) if j in jolt_ratings]

_max = max(jolt_ratings)
jolts[_max] = [_max + 3] # final adapter

permutations = []

# create all permutations, then remove elements that
# have no possible matches to get the valid ones
for key, rating in jolts.items():
    values = jolts[key]

    if len(values) == 1:
        continue

    for value in values:
        permutation = deepcopy(jolts)
        permutation[key] = [value]
        print("Permutation:", permutation)
        permutations.append(permutation)

for permutation in permutations:
    for key, values in sorted(permutation.items()):
        print(values)

    print("")

# valid_permutations = []

# for permutation in permutations:
#     _max = max(jolt_ratings)
#     permutation[_max] = [_max + 3] # final adapter

#     keys_to_remove = []

#     for key, values in permutation.items():
#         rating = values[0]
#         supported_ratings = range(rating + 1, rating + 4)

#         print(values)

#         if rating not in supported_ratings:
#             keys_to_remove.append(key)

#     _permutation = deepcopy(permutation)

#     for key in keys_to_remove:
#         #print(key, _permutation)
#         _permutation = _permutation.pop(key)
    
#     valid_permutations.append(_permutation)

# print(len(valid_permutations))
            


