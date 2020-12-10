with open("input.txt", "r") as f:
    data = f.readlines()

jolt_ratings = [int(line.strip()) for line in data]
jolt_ratings.append(0) # charging outlet

jolt_lookup = {}

for i, rating in enumerate(jolt_ratings):
    jolt_lookup[rating] = [
        j for j in range(rating + 1, rating + 4) if j in jolt_ratings]

_max = max(jolt_ratings)
jolt_lookup[_max] = [_max + 3]

for rating in sorted(jolt_lookup.items()):
    print(rating)

print("")

while True:
    all_assigned = True

    for key, rating in sorted(jolt_lookup.items()):
        if len(rating) == 1:
            for r in jolt_lookup:
                if r != key:
                    try:
                        possible = None

                        if len(jolt_lookup[r]) != 1:
                            possible = jolt_lookup[r].remove(rating[0])
                    except ValueError:
                        pass

                    if possible:
                        jolt_lookup[r] = possible

        else:
            all_assigned = False

    if all_assigned:
        break
    
one_diffs = 0
three_diffs = 0

for key, value in jolt_lookup.items():
    rating = value[0]

    if rating - key == 1:
        one_diffs += 1
    elif rating - key == 3:
        three_diffs += 1

print(one_diffs)
print(three_diffs)

print(one_diffs * three_diffs)
