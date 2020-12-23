from functional import seq
from collections import defaultdict

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

invalid_tickets = []

for ticket in nearby_tickets:
    values = [int(number) for number in ticket.split(',')]

    for value in values:
        valid_value = False

        for _ranges in all_ranges:
            for _range in _ranges:
                if value in _range:
                    valid_value = True

        if not valid_value:
            invalid_tickets.append(ticket)

valid_tickets = list(set(nearby_tickets) - set(invalid_tickets))
valid_tickets = [ticket.split(',') for ticket in valid_tickets]

_rules = { k: v for k,v in zip(keywords, all_ranges)}

matches = defaultdict(list)

for i in range(len(valid_tickets[0])):
    for keyword, ranges in _rules.items():
        valid_for_all = True

        for j in range(len(valid_tickets)):
            value = valid_tickets[j][i]

            if not any([int(value) in _range for _range in ranges]):
                valid_for_all = False

        if valid_for_all:
            matches[keyword].append(i)

while True:
    single_values = {k: v for k, v in matches.items() if len(v) == 1}

    for key, values in single_values.items():
        taken_value = list(values)[0]

        for _key, match in matches.items():
            if len(match) > 1:
                if taken_value in match:
                    matches[_key].remove(taken_value)
    
    if len(single_values) == len(matches):
        break

fields = []

for key, values in matches.items():
    if "departure" in key:
        fields.append(values[0])

values = [int(own_ticket[i]) for i in fields]
print((seq(values).reduce(lambda x, y: x * y)))
