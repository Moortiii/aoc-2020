with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

instructions = []

for entry in data:
    operation = list(entry)
    direction = operation[0]
    amount = int(''.join(operation[1:]))
    instructions.append((direction, amount))

ship_degrees = 90
ship_direction = 'E'
east = 0
north = 0

def move(east, north, direction, amount):
    if direction == 'E':
        east += amount
    elif direction == 'W':
        east -= amount
    elif direction == 'N':
        north += amount
    elif direction == 'S':
        north -= amount

    return east, north

def turn(ship_degrees, direction, amount):
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
    )

    if direction in 'NSEW': # adjust direction and travel
        east, north = move(east, north, direction, amount)
    elif direction in 'LR': # turn the ship
        ship_direction, ship_degrees = turn(ship_degrees, direction, amount)
    elif direction == 'F': # travel in current direction
        east, north = move(east, north, ship_direction, amount)
    
    print(
        "REPLACE - ",
        "East:", east,
        "North:", north,
        "Direction:", ship_direction,
        "Degrees:", ship_degrees,
        "\n"
    )

print(
    "FINAL - ",
    "East:", east,
    "North:", north,
    "Direction:", ship_direction,
    "Degrees:", ship_degrees
)

print("Manhattan distance:", manhattan_distance(east, north))