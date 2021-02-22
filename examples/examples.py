from source.grid import NeighbordingNodes

# initialize 5x5 grid and print grid
grid = NeighbordingNodes(5, debug=True)
print()

# find coordinates of node in grid
print(grid.get_node_coordinates(-1))
print(grid.get_node_coordinates(3))
print(grid.get_node_coordinates(10))
print(grid.get_node_coordinates(25))
print()

# find cross neighbors
print(sorted(grid.find_neighbors(x=2, y=2, i=2, m=1, type='CROSS')))  # invalid
print(sorted(grid.find_neighbors(x=2, y=2, m=1, type='CROSS')))  # valid
print(sorted(grid.find_neighbors(x=0, y=2, m=1, type='CROSS')))  # valid
print(sorted(grid.find_neighbors(i=2, m=1, type='CROSS')))  # valid
print()

# find square neighbors
print(sorted(grid.find_neighbors(x=2, y=2, m=0, type='SQUARE')))  # invalid
print(sorted(grid.find_neighbors(x=2, y=2, m=1, type='SQUARE')))  # valid
print(sorted(grid.find_neighbors(x=2, y=0, m=1, type='SQUARE')))  # valid
print()

# find square neighbors
print(sorted(grid.find_neighbors(x=2, y=2, m=1, type='DIAMOND')))  # valid
print(sorted(grid.find_neighbors(x=2, y=2, m=2, type='DIAMOND')))  # valid
print(sorted(grid.find_neighbors(x=4, y=2, m=2, type='DIAMOND')))  # valid
print()
