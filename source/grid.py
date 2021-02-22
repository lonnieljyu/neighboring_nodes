"""grid.py

Public:
    NeighbordingNodes
        build_grid()
        get_node_coordinates()
        find_neighbors()
"""

from typing import List, Tuple


class NeighbordingNodes:
    def __init__(self, size: int, debug: bool = False) -> None:
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
            If i is an invalid index then an empty tuple is returned.
        """
        return self.grid[i] if 0 <= i < self.size * self.size else tuple()

    def __is_valid_node(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size

    def __get_cross(self, i: int, m: int) -> List[Tuple[int, int]]:
        x, y = self.grid[i]
        nodes = list()
        for i in range(1, m + 1):
            if not self.__is_valid_node(x - i, y):
                break
            nodes.append((x - i, y))

        for i in range(1, m + 1):
            if not self.__is_valid_node(x + i, y):
                break
            nodes.append((x + i, y))

        for i in range(1, m + 1):
            if not self.__is_valid_node(x, y - i):
                break
            nodes.append((x, y - i))

        for i in range(1, m + 1):
            if not self.__is_valid_node(x, y + i):
                break
            nodes.append((x, y + i))
        return nodes

    def __get_diagonals(self, i: int, m: int) -> List[Tuple[int, int]]:
        x, y = self.grid[i]
        nodes = list()
        for i in range(1, m + 1):
            if not self.__is_valid_node(x - i, y - i):
                break
            nodes.append((x - i, y - i))

        for i in range(1, m + 1):
            if not self.__is_valid_node(x - i, y + i):
                break
            nodes.append((x - i, y + i))

        for i in range(1, m + 1):
            if not self.__is_valid_node(x + i, y - i):
                break
            nodes.append((x + i, y - i))

        for i in range(1, m + 1):
            if not self.__is_valid_node(x + i, y + i):
                break
            nodes.append((x + i, y + i))
        return nodes

    def find_neighbors(self, **kwargs) -> List:
        """Gets a list of neighbors given the origin node, neighborhood radius, m, and neighborhood type.

        Args:
            **kwargs: dictionary of parameters

        Returns:
            List of tuples of x,y coordinates.
        """
        neighbors = list()
        if (not (('x' in kwargs and 'y' in kwargs) != ('i' in kwargs))
                or 'm' not in kwargs or kwargs['m'] <= 0 or kwargs['m'] > self.size/2
                or 'type' not in kwargs or kwargs['type'] not in ('SQUARE', 'CROSS', 'DIAMOND')):
            return neighbors

        if 'i' in kwargs:
            if kwargs['i'] < 0 or kwargs['i'] >= self.size*self.size:
                return neighbors
            i = kwargs['i']
        else:
            if (kwargs['x'] < 0 or kwargs['x'] >= self.size
                    or kwargs['y'] < 0 or kwargs['y'] >= self.size):
                return neighbors
            i = kwargs['x'] * self.size + kwargs['y']

        neighbors = self.__get_cross(i, kwargs['m'])
        if kwargs['type'] == 'SQUARE':
            neighbors.extend(self.__get_diagonals(i, kwargs['m']))
        elif kwargs['type'] == 'DIAMOND':
            neighbors.extend(self.__get_diagonals(i, kwargs['m'] - 1))
        return neighbors


if __name__ == '__main__':
    pass
