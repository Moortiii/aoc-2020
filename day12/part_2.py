with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

instructions = []

for entry in data:
    operation = list(entry)
    direction = operation[0]
    amount = int(''.join(operation[1:]))
    instructions.append((direction, amount))

waypoint = (10, 1) # east, north
ship_degrees = 90
ship_direction = 'E'
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

def move(east, north, waypoint, amount):
    east += waypoint[0] * amount
    north += waypoint[1] * amount

    return east, north

def turn(waypoint, direction, ship_direction, ship_degrees, amount):
    # Calculate new path of travel
    if direction == 'L':
        ship_degrees = (ship_degrees - amount) % 360
    elif direction == 'R':
        ship_degrees = (ship_degrees + amount) % 360

    # Convert degrees to direction
    new_direction = None

    if ship_degrees == 90:
        new_direction = 'E'
    elif ship_degrees == 180:
        new_direction = 'S'
    elif ship_degrees == 270:
        new_direction = 'W'
    else:
        new_direction = 'N'
    
    return new_direction, ship_degrees

def manhattan_distance(x, y):
    return abs(x) + abs(y)


for instruction in instructions:
    direction, amount = instruction
    print(f"Instruction: {direction}, {amount}")

    print(
        "CURRENT - ",
        "East:", east,
        "North:", north,
        "Direction:", ship_direction,
        "Degrees:", ship_degrees,
        "Waypoint", waypoint,
    )

    if direction in 'NSEW': # adjust direction and travel
        waypoint = move_waypoint(waypoint[0], waypoint[1], direction, amount)
    elif direction in 'LR': # turn the ship
        ship_direction, ship_degrees = turn(waypoint, ship_degrees, amount)
    elif direction == 'F': # travel in current direction
        east, north = move(east, north, waypoint, amount)
    
    print(
        "REPLACE - ",
        "East:", east,
        "North:", north,
        "Direction:", ship_direction,
        "Degrees:", ship_degrees,
        "Waypoint", waypoint,
        "\n"
    )

print(
    "FINAL - ",
    "East:", east,
    "North:", north,
    "Direction:", ship_direction,
    "Degrees:", ship_degrees,
    "Waypoint", waypoint,
    "\n"
)

print("Manhattan distance:", manhattan_distance(east, north))