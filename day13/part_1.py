from collections import defaultdict

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

earliest_time = int(data[0])
intervals = [int(d) for d in data[1].split(',') if d != 'x']
smallest_interval = min(intervals)

travel_times = defaultdict(list)

for interval in intervals:
    if interval == 'x':
        continue

    iterations = (earliest_time // smallest_interval) + 5

    for i in range(iterations):
        travel_times[interval].append(i * interval)

options = []

for interval in intervals:
    i = earliest_time

    while True:
        if i in travel_times[interval]:
            options.append((i, interval))
            break
        
        i += 1

print(options)

best_option = min(options, key=lambda x: x[0])
arrival_time = best_option[0]
bus_to_take  = best_option[1]

print("Time to wait:", arrival_time - earliest_time)
print("Output:", (arrival_time - earliest_time) * bus_to_take)