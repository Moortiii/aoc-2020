import numpy as np
import math

with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

instructions = []

for entry in data:
    operation = list(entry)
    direction = operation[0]
    amount = int(''.join(operation[1:]))
    instructions.append((direction, amount))

waypoint = (10, 1) # east, north
east = 0
north = 0


def move_waypoint(east, north, direction, amount):
    if direction == 'E':
        east += amount
    elif direction == 'W':
        east -= amount
    elif direction == 'N':
        north += amount
    elif direction == 'S':
        north -= amount

    return east, north

def move_ship(east, north, waypoint, amount):
    east  += waypoint[0] * amount
    north += waypoint[1] * amount

    return east, north

def rotate_origin_only(waypoint, direction, radians):
    """Only rotate a point around the origin (0, 0)."""
    x, y = waypoint

    radians = np.radians(radians)

    if direction == 'L':
        radians = -radians

    xx = x * math.cos(radians) + y * math.sin(radians)
    yy = -x * math.sin(radians) + y * math.cos(radians)

    return round(xx), round(yy)

def rotate_waypoint(waypoint, direction, amount):
    theta = np.radians(amount)
    
    print("Amount:", amount)
    if direction == 'L':
        theta = -theta
    
    r = np.array((
        (np.cos(theta), -np.sin(theta)),
        (np.sin(theta),  np.cos(theta))
    ))

    print("Rotation:", r.dot(waypoint))

    return np.floor(r.dot(waypoint))

def manhattan_distance(x, y):
    return abs(x) + abs(y)


for instruction in instructions:
    direction, amount = instruction
    print(f"Instruction: {direction}, {amount}")

    print(
        "CURRENT - ",
        "East:", east,
        "North:", north,
        "Waypoint", waypoint,
    )

    if direction in 'NSEW':
        waypoint = move_waypoint(waypoint[0], waypoint[1], direction, amount)
    elif direction in 'LR':
        waypoint = rotate_origin_only(waypoint, direction, amount)
    elif direction == 'F':
        east, north = move_ship(east, north, waypoint, amount)
    
    print(
        "REPLACE - ",
        "East:", east,
        "North:", north,
        "Waypoint", waypoint,
        "\n"
    )

print(
    "FINAL - ",
    "East:", east,
    "North:", north,
    "Waypoint", waypoint,
    "\n"
)

print("Manhattan distance:", manhattan_distance(east, north))