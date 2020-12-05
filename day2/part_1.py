with open("input.txt", "r") as f:
    data = f.read().split('\n')

passwords = []

for i, line in enumerate(data):
    # bruteforce input parsing
    min_num = line.split('-')[0]
    min_num = int(min_num)
    max_num = int(line.split('-')[1].split(' ')[0])
    char = line.split('-')[1].split(' ')[1].split(':')[0]
    password = line.split('-')[1].split(' ')[2]
    
    count = 0

    for character in password:
        if character == char:
            count += 1
    
    if count > max_num or count < min_num:
        continue

    passwords.append(password)

print("Number of passwords in list:", len(data))
print("Number of passwords that are valid:", len(passwords))