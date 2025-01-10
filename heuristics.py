import math
from node import Node

def euclidean(node: Node, goal: Node) -> float:
    x1, y1 = node.x, node.y
    x2, y2 = goal.x, goal.y
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def manhattan(node: Node, goal: Node) -> float:
    x1, y1 = node.x, node.y
    x2, y2 = goal.x, goal.y
    return abs(x1 - x2) + abs(y1 - y2)
