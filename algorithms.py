from node import Node
from queue import Queue
from typing import Callable

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
                return (child, len(reached)+1, len(visited))
            if child not in reached:
                reached.add(child)
                frontier.put(child)
    return None

def DFS(start: Node, Objective: Node, costFunction: Callable):
    currentNode = start
    
    if currentNode == Objective:
        return currentNode
    
    frontier = []
    frontier.append(currentNode)

    reached = set()
    reached.add(currentNode)

    visited = []

    while not len(frontier) == 0:
        currentNode = frontier.pop()
        visited.append(currentNode)
        children = currentNode.expand(costFunction)

        for child in children:
            if child == Objective:
                return (child, len(reached)+1, len(visited))
            if child not in reached:
                reached.add(child)
                frontier.append(child)
    return None