""" Advent of code - Day 11 """
from copy import deepcopy

# Addends for i and j in a given direction of travel
addends = {
    "up":    [-1,  0],
    "down":  [ 1,  0],
    "left":  [ 0, -1],
    "right": [ 0,  1],
    "top_l": [-1, -1],
    "top_r": [-1,  1],
    "bot_l": [ 1, -1],
    "bot_r": [ 1,  1]
}

def get_seat(d, i, j):
    """ Returns the seat at [i,j] if it exists, else None """
    if i < 0 or j >= len(d[0]):
        return None

    if i >= len(d) or j < 0:
        return None
     
    return d[i][j]


def get_seat_in_direction(d, i, j, direction):
    """ Get the first seat a person can 'see', in any given direction. A
    person can only see past seats that are empty ('.'). """
    current_i = i + addends[direction][0]
    current_j = j + addends[direction][1]
    previous_seat = None

    while True:
        seat = get_seat(d, current_i, current_j)

        if not seat:
            return previous_seat

        if seat != '.':
            return seat

        current_i += addends[direction][0]
        current_j += addends[direction][1]
        previous_seat = seat


def get_adjacent_seats(d, i, j):
    """ Get the seats in all adjacent directions from i,j """
    return [get_seat_in_direction(d, i, j, m) for m in addends]


def count_occupied_adjacent_seats(seats):
    """ Count the number of occupied seats in a list of seats """
    return len([x for x in seats if x == '#'])


def seatings_are_identical(d1, d2):
    """ Check if two seating options are identical """
    for i in range(len(d1)):
        for j in range(len(d1[0])):
            if d1[i][j] != d2[i][j]:
                return False
    
    return True


def count_occupied_total(d):
    """ Count the number of occupied seats in the entire room """
    occupied = 0

    for i in range(len(d)):
        for j in range(len(d[0])):
            if d[i][j] == '#':
                occupied += 1

    return occupied


def epoch(seat_input):
    """ Perform one epoch of seat switching. All seats are switched
    simultaneously. """
    seats = deepcopy(seat_input)

    for i in range(rows):
        for j in range(columns):
            current_seat = seats[i][j]
            adjacent = get_adjacent_seats(seats, i, j)
            occupied = count_occupied_adjacent_seats(adjacent)

            if current_seat == 'L':
                if occupied == 0:
                    seat_input[i][j] = '#'
                
            if current_seat == '#':
                if occupied >= 5:
                    seat_input[i][j] = 'L'
    
    return seat_input, count_occupied_total(seat_input)


with open("input.txt", "r") as f:
    data = [list(l.strip()) for l in f.readlines()]

rows = len(data)
columns = len(data[0])
seats = deepcopy(data)
previous, _ = epoch(data)

while True:
    next, occupied = epoch(deepcopy(previous))

    if seatings_are_identical(next, previous):
        print("Occcupied seats:", occupied)
        break

    previous = next
