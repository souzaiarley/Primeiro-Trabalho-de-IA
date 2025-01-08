import costs as c
from queue import Queue
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
    def expand(self, costFunction: Callable):
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

def BFS(start: Node, Objective: Node, costFunction: Callable):
    currentNode = start
    
    if currentNode == Objective:
        return currentNode
    
    frontier = Queue()
    frontier.put(currentNode)

    reached = set()
    reached.add(currentNode)

    visited = []

    while not frontier.empty():
        currentNode = frontier.get()
        visited.append(currentNode)
        children = currentNode.expand(costFunction)

        for child in children:
            if child == Objective:
                return (child, len(reached), len(visited))
            if child not in reached:
                reached.add(child)
                frontier.put(child)
    return None

def main():
    start = Node(0, 0)
    objective = Node(2, 1)
    result = BFS(start, objective, c.C_1)
    path = result[0].path()

    if result is None:
        print("No solution")
    else:
        print(f"Solution found:")
        print("Start:", start)
        print("Objective:", objective)
        print("Path:", end=" ")
        for node in reversed(path):
            print(node, end="")
            if node != objective:
                print(" -> ", end="")
        print(f"\nPath cost: {result[0].cost}")
        print(f"Nodes generated: {result[1]}")
        print(f"Nodes visited: {result[2]}")

if __name__ == "__main__":
    main()