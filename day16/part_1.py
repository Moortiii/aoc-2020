from functional import seq

def extract_ranges(section, keyword):
    return (seq(section)
        .map(lambda x: x.split(f"{keyword}: "))
        .map(lambda x: x[-1])
        .map(lambda x: x.split(" or "))
        .map(lambda xy: (xy[0].split('-'), xy[1].split('-')))
        .map(lambda xy: (
            (range(int(xy[0][0]), int(xy[0][1]) + 1)),
            (range(int(xy[1][0]), int(xy[1][1]) + 1)),
        ))
        .head())

with open("input.txt", "r") as f:
    data = f.read()

sections = data.split("\n\n")
rules = sections[0].split("\n")
keywords = [rule.split(': ')[0] for rule in rules]
all_ranges = [
    extract_ranges(rule, keyword) for rule, keyword in zip(rules, keywords)]

own_ticket = (seq(sections[1])
    .map(lambda x: x.split("your ticket:\n"))
    .map(lambda x: x[-1])
    .map(lambda x: x.split(","))
    .head())

nearby_tickets = (seq(sections[2])
    .map(lambda x: x.split("nearby tickets:\n"))
    .map(lambda x: x[-1])
    .map(lambda x: x.split("\n"))
    .head())

invalid_values = []

for ticket in nearby_tickets:
    values = [int(number) for number in ticket.split(',')]

    for value in values:
        valid_value = False

        for _ranges in all_ranges:
            for _range in _ranges:
                if value in _range:
                    valid_value = True

        if not valid_value:
            invalid_values.append(value)

print(sum(invalid_values))