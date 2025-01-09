import math
from typing import Tuple

def euclidean_heuristic(node: Tuple[int, int], goal: Tuple[int, int]) -> float:
  x1, y1 = node
  x2, y2 = goal
  return 10 * math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def manhattan_heuristic(node: Tuple[int, int], goal: Tuple[int, int]) -> float:
  x1, y1 = node
  x2, y2 = goal
  return 10 * (abs(x1 - x2) + abs(y1 - y2))
