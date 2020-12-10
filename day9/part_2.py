def calculate_sums(numbers):
    """ Calculate and return a list with the sum of
    every number pair in given list of numbers """
    sums = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]: # may not be equal
                continue
            
            sums.append(numbers[i] + numbers[j])
    
    return sums

filename = "input.txt"

with open(filename, "r") as f:
    data = f.readlines()

numbers = [int(line.strip()) for line in data]

PREAMBLE_LEN = 25

head = 0
tail = head + PREAMBLE_LEN
violation = -1

# Find the violating number
while True:
    if tail == len(numbers):
        break

    sums = calculate_sums(numbers[head:tail])
    head += 1
    next_number = numbers[tail]
    tail = head + PREAMBLE_LEN

    if next_number not in sums:
        violation = next_number
        break

print(violation)

# Find a contiguos set of numbers that
# sum to the violation number
head = 0
tail = 1

while True:
    current_range = numbers[head:tail + 1]
    _sum = sum(current_range)

    if _sum == violation:
        print(current_range)
        break
    
    if _sum > violation:
        head += 1
    else:
        tail += 1

_min = min(current_range)
_max = max(current_range)

print("Encryption weakness:", _min + _max)
