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

while True:
    if tail == len(numbers):
        break

    sums = calculate_sums(numbers[head:tail])
    head += 1
    next_number = numbers[tail]
    tail = head + PREAMBLE_LEN

    if next_number not in sums:
        print("XMAS Violation:", next_number)
        break

    
    
