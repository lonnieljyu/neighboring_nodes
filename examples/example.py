from source.grid import NeighbordingNodes

# initialize 5x5 grid and print grid
grid = NeighbordingNodes(5, debug=True)

# find coordinates of node in grid
print(grid.get_node_coordinates(-1))
print(grid.get_node_coordinates(3))
print(grid.get_node_coordinates(10))
print(grid.get_node_coordinates(25))
