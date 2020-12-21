from collections import defaultdict
from functional import seq

def generate_schedule(bus_id, offset):
    i = 1
    yield offset

    while i < 100:
        yield (bus_id * i) + offset
        i += 1

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

# Match Bus IDs with their offsets in the list
offsets = [(offset, bus_id) for offset, bus_id in enumerate(departures)]

# Create generators with the schedules for each bus
schedules = defaultdict(list)

# Create schedules for each bus_id, taking the offset into account
for entry in offsets:
    offset, bus_id = entry
    schedules[bus_id] = generate_schedule(bus_id, offset)

#print(list(schedules[7]))
#print("")
#print(list(schedules[13]))


















# schedules = defaultdict(list)

# for i in range(1068789):
#     for entry in offsets:
#         _, bus_id = entry

#         if bus_id == 'x':
#             continue

#         if i % bus_id == 0:
#             schedules[i].append(i)

# print(schedules)       

        