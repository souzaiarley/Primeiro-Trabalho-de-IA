import math
from node import Node

def euclidean(state: tuple, goal: tuple) -> float:
    x1, y1 = state[0], state[1]
    x2, y2 = goal[0], goal[1]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def manhattan(state: tuple, goal: tuple) -> float:
    x1, y1 = state[0], state[1]
    x2, y2 = goal[0], goal[1]
    return abs(x1 - x2) + abs(y1 - y2)
