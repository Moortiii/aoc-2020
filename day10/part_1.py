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

while True:
    all_assigned = True

    for key, rating in jolts.items():
        if len(rating) != 1:
            all_assigned = False
            continue

        for r in jolts:
            if r == key or len(jolts[r]) == 1:
                continue
            
            if rating[0] not in jolts[r]:
                continue

            options = jolts[r].remove(rating[0])
            jolts[r] = options if options else jolts[r]

    if all_assigned:
        break
    
diffs = [0, 0]

for key, values in jolts.items():
    difference = values[0] - key

    if difference == 1:
        diffs[0] += 1
    elif difference == 3:
        diffs[1] += 1

print(diffs[0] * diffs[1])
