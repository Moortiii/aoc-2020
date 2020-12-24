from collections import defaultdict
from copy import deepcopy
from functional import seq

with open("input.txt", "r") as f:
    data = f.readlines()

grid = (seq(data)
    .map(lambda x: x.strip())
    .map(lambda x: list(x))
    .to_list())

layers = defaultdict(lambda: defaultdict(list))
layers[0] = grid

def get_neighbor_coordinates(x, y, z):
    """ Get the coordinates for all neighbors in three dimensions """
    coordinates = []

    for z in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if x == y == z == 0:
                    continue
                
                coordinates.append((x, y, z))

    return coordinates

for i in range(1, 6 + 1):
    lowest_z = min(layers)
    highest_z = max(layers)

    print(f"After {i} cycles: \n")

    for z in range(lowest_z, highest_z + 1):
        print(f"z = {z}")

        data = deepcopy(layers)
    
        for y in range(len(layers[z])):
            for x in range(len(layers[z][0])):
                current_tile = layers[z][y][x]
                print(current_tile, f"({x}, {y}, {z})")

                neighbor_coordinates = get_neighbor_coordinates(x, y, z)
                neighbors = []

                for coordinate in neighbor_coordinates:
                    _x, _y, _z = coordinate
                    neighbor = '.' # default inactive

                    try:
                        neighbor = layers[_z][_y][_x]
                    except IndexError:
                        pass
                
                    neighbors.append((neighbor, coordinate))

                    # TODO: Expand original grid to include layers above, below
                    # and new neighbors
                    data[_z][_y][_x] = neighbor

                active_neighbors = (seq(neighbors)
                    .filter(lambda xy: xy[0] == '#')
                    .reduce(lambda x, y: x + 1, 0))
                
                inactive_neighbors = (seq(neighbors)
                    .filter(lambda xy: xy[0] == '.')
                    .reduce(lambda x, y: x + 1, 0))

                if current_tile == '.':
                    if 2 <= active_neighbors <= 3: # retain current state
                        continue

                    data[z][y][x] = '.' # set inactive

                elif current_tile == '#':
                    if active_neighbors == 3:
                        data[z][y][x] = '#' # set active

        layers = deepcopy(data)
        
        print("")