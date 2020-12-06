with open('input.txt', 'r') as f:
    data = f.read()

groups = data.split('\n\n')
groups = [group.replace('\n', '') for group in groups]
groups = [set(group) for group in groups]

sum = 0

for group in groups:
    sum += len(group)

print("Number of unique answers:", sum)