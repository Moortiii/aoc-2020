from collections import defaultdict
from functional import seq

earliest_timestamp = 0

def generate_schedule(limit, bus_id, earliest_timestamp):
    i = earliest_timestamp // bus_id

    while i < (earliest_timestamp + limit) // bus_id:
        yield i * bus_id
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

# Match Bus IDs with their offets in the list
offsets = [(offset + 1, bus_id) for offset, bus_id in enumerate(departures)]

# Create generators with the schedules for each bus
schedules = defaultdict(list)

for entry in offsets:
    offset, bus_id = entry

    if bus_id == 'x':
        continue

    schedules[bus_id] = generate_schedule(100, bus_id, earliest_timestamp)


for _ in range(10):
    for schedule in schedules.values():
        try:
            print(next(schedule))
            print("")
        except:
            pass

























# schedules = defaultdict(list)

# for i in range(1068789):
#     for entry in offsets:
#         _, bus_id = entry

#         if bus_id == 'x':
#             continue

#         if i % bus_id == 0:
#             schedules[i].append(i)

# print(schedules)       

        