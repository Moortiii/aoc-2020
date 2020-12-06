with open('input.txt', 'r') as f:
    data = f.read()

groups = data.split('\n\n')
groups = [group.replace('', '') for group in groups]
groups = [group.split('\n') for group in groups]

sum = 0

for group in groups:
    combined = ''.join(group)
    counter = 0

    for letter in set(combined):
        if combined.count(letter) == len(group):
            counter += 1
        
    sum += counter

print("Number of questions to which everyone answered yes:", sum)