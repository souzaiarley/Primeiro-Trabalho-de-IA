from typing import Callable

class Node:
    # Constructor
    def __init__(self, x, y, depth=0, parent=None, cost=0):
        if x < 0 or y < 0 or x > 30 or y > 30:
            raise ValueError("Invalid position. Values for x and y must be between 0 and 30")
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent
        self.cost = cost

    # Methods for comparison, hashing (used in set) and string representation
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Returns a list of all possible children nodes
    def expand(self, costFunction: Callable = lambda depth: (1,1)):
        children = []
        costs = costFunction(self.depth + 1)
        if self.x - 1 >= 0:
            children.append(Node(self.x - 1, self.y, self.depth + 1, self, self.cost + costs[0]))
        if self.x + 1 <= 30:
            children.append(Node(self.x + 1, self.y, self.depth + 1, self, self.cost + costs[0]))
        if self.y - 1 >= 0:
            children.append(Node(self.x, self.y - 1, self.depth + 1, self, self.cost + costs[1]))
        if self.y + 1 <= 30:
            children.append(Node(self.x, self.y + 1, self.depth + 1, self, self.cost + costs[1]))
        return children
    
    # Returns the path from the current node to the root node
    def path(self):
        path = []
        current = self
        while current is not None:
            path.append(current)
            current = current.parent
        return path