with open("input.txt", "r") as f:
    data = f.read().split('\n')

passwords = []

for i, line in enumerate(data):
    # bruteforce input parsing
    index_1 = int(line.split('-')[0])
    index_2 = int(line.split('-')[1].split(' ')[0])
    character = line.split('-')[1].split(' ')[1].split(':')[0]
    password = line.split('-')[1].split(' ')[2]
    
    match_1 = password[index_1 - 1] == character
    match_2 = password[index_2 - 1] == character

    # xor
    if match_1 != match_2:
        passwords.append(password)

print("Number of passwords in list:", len(data))
print("Number of passwords that are valid:", len(passwords))