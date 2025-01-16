from costFunctions import *
from typing import Callable

# This function returns the cost of a path using a cost function
def getPathCost(path: list, costFunction: Callable):
    totalCost = 0
    path.reverse()

    for i in range(len(path) - 1):
        edgeCosts = costFunction(path[i+1].depth)

        if path[i+1].x > path[i].x or path[i+1].x < path[i].x:
            totalCost += edgeCosts[0]
        else:
            totalCost += edgeCosts[1]

    return totalCost