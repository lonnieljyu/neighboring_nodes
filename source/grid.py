"""grid.py

Public:
    NeighbordingNodes
        build_grid()
        get_node_coordinates()
"""

from typing import Tuple


class NeighbordingNodes:
    def __init__(self, size: int, debug: bool=False) -> None:
        self.size = size
        self.debug = debug
        self.grid = list()
        self.build_grid()

    def __pretty_print_grid(self) -> str:
        """Returns a visual representation of the grid in a str."""
        string = [
            f'({self.grid[i][0]}, {self.grid[i][1]}, {i})'
            for i in range(self.size*self.size)
        ]

        string = [
            '\t'.join(string[i:i+self.size])
            for i in range(0, self.size*self.size, self.size)
        ]

        return '\n'.join(string)

    def build_grid(self) -> None:
        """Builds a 2D, square (size x size) graph of nodes.
        Each node is represented with the zero-based index number as the key and x,y coordinates as the value.
        The nodes are stored in an array and are created in row-major order.
        If debug is True then this function will print a visual representation of the grid.
        """
        self.grid = [(x, y) for x in range(self.size) for y in range(self.size)]
        if self.debug:
            print(self.__pretty_print_grid())

    def get_node_coordinates(self, i: int) -> Tuple[int, int]:
        """Gets a node's x and y-axis coordinates given the node's index number.

        Args:
            i: zero-based index of the node

        Returns:
            x and y-axis coordinates of the nodes as a tuple.
            If i is an invalid index then None is returned.
        """
        return self.grid[i] if 0 <= i < self.size * self.size else None
