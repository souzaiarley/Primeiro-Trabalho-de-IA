from node import Node
from queue import Queue
from queue import PriorityQueue
from typing import Callable

# Breadth First Search
def BFS(start: Node, goal: Node, costFunction: Callable):
    # Start from the start node
    currentNode = start
    
    # If the start node is the goal node, return the start node
    if currentNode == goal:
        return (currentNode, 1, 1)
    
    # Create a queue to store the nodes to be visited and add the start node to the queue
    frontier = Queue()
    frontier.put(currentNode)

    # Create a set to store the nodes that have been reached and add the start node to the set
    reached = set()
    reached.add(currentNode)

    # Create a list to store the nodes that have been visited
    visited = []

    # While the queue is not empty
    while not frontier.empty():
        # Get the first node in the queue, remove it from the queue, and add it to the visited list
        currentNode = frontier.get()
        visited.append(currentNode)
        
        # Expand the current node
        children = currentNode.expand(costFunction)

        # For each child node, if the child node is the goal node, return the child node. Otherwise, add the child node to the queue and to the reached set
        for child in children:
            if child == goal:
                return (child, len(reached)+1, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if child not in reached:
                reached.add(child)
                frontier.put(child)
    
    # If the goal node is not found, return None
    return None


# Depth First Search
def DFS(start: Node, goal: Node, costFunction: Callable):
    # Start from the start node
    currentNode = start
    
    # If the start node is the goal node, return the start node
    if currentNode == goal:
        return (currentNode, 1, 1)
    
    # Create a stack to store the nodes to be visited and add the start node to the stack
    frontier = []
    frontier.append(currentNode)

    # Create a set to store the nodes that have been reached and add the start node to the set
    reached = set()
    reached.add(currentNode)

    # Create a list to store the nodes that have been visited
    visited = []

    # While the stack is not empty
    while not len(frontier) == 0:
        # Get the last node in the stack, remove it from the stack, and add it to the visited list
        currentNode = frontier.pop()
        visited.append(currentNode)

        # Expand the current node
        children = currentNode.expand(costFunction)

        # For each child node, if the child node is the goal node, return the child node. Otherwise, add the child node to the stack and to the reached set
        for child in children:
            if child == goal:
                return (child, len(reached)+1, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if child not in reached:
                reached.add(child)
                frontier.append(child)
    
    # If the goal node is not found, return None
    return None


# Uniform Cost Search
def Dijkstra(start: Node, goal: Node, costFunction: Callable):
    # Start from the start node
    current = start
    
    # Create a priority queue to store the nodes to be visited and add the start node to the queue
    frontier = PriorityQueue()
    frontier.put((0, id(current), current))

    # Create a dictionary to store the nodes that have been reached and add the start node to the dictionary
    reached = {}
    reached[current] = current

    # Create a list to store the nodes that have been visited
    visited = []

    # While the queue is not empty
    while not frontier.empty():
        # Get the first node in the queue, remove it from the queue, and add it to the visited list
        current = frontier.get()[2]
        visited.append(current)
        
        # If the current node is the goal node, return the current node, the number of nodes reached (generated), and the number of nodes visited
        if current == goal:
            return (current, len(reached), len(visited))
        
        # Expand the current node
        children = current.expand(costFunction)

        # For each child node, if the child node is not in the reached dictionary or the cost of the child node is less than the cost of the child node in the reached dictionary, add the child node to the reached dictionary and to the queue (Relaxation)
        for child in children:
            if child not in reached or child.cost < reached[child].cost:
                reached[child] = child
                frontier.put((child.cost, id(child), child))
    
    # If the goal node is not found, return None
    return None

def GBFS(start: Node, goal: Node, heuristic: Callable):
    # Start from the start node
    current = start

    # Create the priority queue and add the start node
    frontier = PriorityQueue()
    frontier.put((0, id(current), current))  # Priority = f(n) = h(n)

    # Create a dictionary to store the nodes that have been reached and add the start node to the dictionary
    reached = {}
    reached[current] = current

    # List of visited nodes
    visited = []

    # While there are nodes to explore
    while not frontier.empty():
        # Remove the node with the lowest f(n) cost (i.e., smallest heuristic)
        current = frontier.get()[2]
        visited.append(current)

        # Check if it is the goal node
        if current == goal:
            return current, len(reached), len(visited)

        # Expand the child nodes
        for child in current.expandGBFS(heuristic, goal):
            # Calculate the heuristic for the child node
            f_est = heuristic(child, goal)  # f(n) = h(n)

            # If the child node hasn't been reached before, or if it's a better path (lower heuristic)
            if child not in reached:
                reached[child] = child
                frontier.put((f_est, id(child), child))  # Insert the child into the priority queue with its heuristic as the priority

    # If the goal is not found, return None
    return None


def AStar(start: Node, goal: Node, costFunction: Callable, heuristic: Callable):
    # Start from the start node
    current = start

    # Create the priority queue and add the start node
    frontier = PriorityQueue()
    frontier.put((0, id(current), current))  # Priority = f(n) = g(n) + h(n)

    # Create a dictionary to store the nodes that have been reached and add the start node to the dictionary
    reached = {}
    reached[current] = current

    # List of visited nodes
    visited = []

    # While there are nodes to explore
    while not frontier.empty():
        # Remove the node with the lowest f(n) cost
        current = frontier.get()[2]
        visited.append(current)

        # Check if it is the goal node
        if current == goal:
            return current, len(reached), len(visited)

        # Expand the child nodes
        for child in current.expand(costFunction):
            # Calculate the costs
            g_cost = child.cost  # g(n) is already included in the child's cost (updated in expand)
            f_cost = g_cost + heuristic(child, goal)  # f(n) = g(n) + h(n)

            # Check if the node should be updated
            if child not in reached or g_cost < reached[child].cost:
                reached[child] = child  # Update the node in the reached dictionary
                frontier.put((f_cost, id(child), child))  # Add to the priority queue

    # If the goal is not found, return None
    return None
