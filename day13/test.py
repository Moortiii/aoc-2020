from collections import defaultdict
from functional import seq

with open("input.txt", "r") as f:
    data = f.readlines()

data = (seq(data)
    .map(lambda x: x.strip())
    .map(lambda x: x.split(','))
    .flatten()
    .map(lambda x: int(x) if x != 'x' else x)
)

# The first line is no longer relevant
departures = data[1:]

# Match Bus IDs with their offets in the list
offsets = [(offset + 1, bus_id) for offset, bus_id in enumerate(departures)]

# Create generators with the schedules for each bus
schedules = defaultdict(list)

def generate_schedule(bus_id):
    i = 1

    while i < 100:
        yield i * bus_id
        i += 1

for entry in offsets:
    offset, bus_id = entry

    if bus_id == 'x':
        continue

        
    schedules[bus_id] = generate_schedule(bus_id)

output = '\t'

for entry in offsets:
    _, bus_id = entry
    output += str(bus_id)
    output += "\t"

output += "\n"

for i in range(1, 100):
    output += str(i)
    
    for entry in offsets:
        offset, bus_id = entry
        schedule = schedules[bus_id]

        if bus_id == 'x':
            output += "\t."
        elif i % bus_id == 0:
            output += "\tD"
        else:
            output += "\t."

    output += "\n"

print(output)
