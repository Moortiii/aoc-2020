import sys

with open('input.txt', 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

for i in range(len(data)):
    for j in range(len(data)):
        if int(data[i]) + int(data[j]) == 2020:
            print(data[i], data[j])
            print("Multiplied:", int(data[i]) * int(data[j]))
            sys.exit()