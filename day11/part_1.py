""" Advent of code - Day 11 """
from copy import deepcopy

def get_seat(d, i, j):
    if i < 0 or j >= len(d[0]):
        return None

    if i >= len(d) or j < 0:
        return None
     
    return d[i][j]


def get_adjacent_seats(d, i, j):
    up    = get_seat(d, i-1, j)
    down  = get_seat(d, i+1, j)
    left  = get_seat(d, i, j-1)
    right = get_seat(d, i, j+1)
    top_l = get_seat(d, i-1, j-1)
    top_r = get_seat(d, i-1, j+1)
    bot_l = get_seat(d, i+1, j-1)
    bot_r = get_seat(d, i+1, j+1)

    return [
        up, down, left, right,
        top_r, top_l, bot_l, bot_r
    ]


def occupied_adjacent(d):
    return len([x for x in d if x == '#'])


def seatings_are_identical(d1, d2):
    for i in range(len(d1)):
        for j in range(len(d1[0])):
            #print(d1[i][j], d2[i][j], hex(id(d1[i][j])), hex(id(d2[i][j])))

            if d1[i][j] != d2[i][j]:
                return False
    
    return True


def occupied_total(d):
    occupied = 0

    for i in range(len(d)):
        for j in range(len(d[0])):
            if d[i][j] == '#':
                occupied += 1

    return occupied


with open("input.txt", "r") as f:
    data = f.readlines()

data = [l.strip() for l in data]
data = [list(l) for l in data]

def epoch(d):
    seats = deepcopy(d)

    for i in range(len(d)):
        for j in range(len(d[0])):
            current_seat = seats[i][j]
            adjacent = get_adjacent_seats(seats, i, j)
            occupied = occupied_adjacent(adjacent)

            if current_seat == 'L':
                if occupied == 0:
                    d[i][j] = '#'
                
            if current_seat == '#':
                if occupied >= 5:
                    d[i][j] = 'L'
    
    return d, occupied_total(d)

previous, _ = epoch(data)

while True:
    next, occupied = epoch(deepcopy(previous))

    if seatings_are_identical(next, previous):
        print(occupied)
        break

    previous = next