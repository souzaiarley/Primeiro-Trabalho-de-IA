from node import Node
from queue import Queue
from queue import PriorityQueue
from typing import Callable
from random import shuffle

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

    # Create a set to store the states that have been reached and add the start node's state to the set
    reached = set()
    reached.add((currentNode.x, currentNode.y))

    # Create a list to store the nodes that have been visited
    visited = []

    # Number of nodes generated
    generated = 1

    # While the queue is not empty
    while not frontier.empty():
        # Get the first node in the queue, remove it from the queue, and add it to the visited list
        currentNode = frontier.get()
        visited.append(currentNode)
        
        # Expand the current node
        children = currentNode.expand(costFunction)
        
        # Update the number of nodes generated
        generated += len(children)

        # For each child node, if it's state is the goal, return the child node. Otherwise, if the state of the child node has not been reached, add the child node to the queue and it's state to the reached set
        for child in children:
            if child.x == goal.x and child.y == goal.y:
                return (child, generated, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if (child.x, child.y) not in reached:
                reached.add((child.x, child.y))
                frontier.put(child)
    
    # If the goal is not found, return None
    return None

# Random Breadth First Search
def RandomBFS(start: Node, goal: Node, costFunction: Callable):
    # Start from the start node
    currentNode = start
    
    # If the start node is the goal node, return the start node
    if currentNode == goal:
        return (currentNode, 1, 1)
    
    # Create a queue to store the nodes to be visited and add the start node to the queue
    frontier = Queue()
    frontier.put(currentNode)

    # Create a set to store the states that have been reached and add the start node's state to the set
    reached = set()
    reached.add((currentNode.x, currentNode.y))

    # Create a list to store the nodes that have been visited
    visited = []

    # Number of nodes generated
    generated = 1

    # While the queue is not empty
    while not frontier.empty():
        # Get the first node in the queue, remove it from the queue, and add it to the visited list
        currentNode = frontier.get()
        visited.append(currentNode)
        
        # Expand the current node
        children = currentNode.expand(costFunction)

        # Shuffle the children nodes to make the search random
        shuffle(children)
        
        # Update the number of nodes generated
        generated += len(children)

        # For each child node, if it's state is the goal, return the child node. Otherwise, if the state of the child node has not been reached, add the child node to the queue and it's state to the reached set
        for child in children:
            if child.x == goal.x and child.y == goal.y:
                return (child, generated, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if (child.x, child.y) not in reached:
                reached.add((child.x, child.y))
                frontier.put(child)
    
    # If the goal is not found, return None
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

    # Create a set to store the states that have been reached and add the start node's state to the set
    reached = set()
    reached.add((currentNode.x, currentNode.y))

    # Create a list to store the nodes that have been visited
    visited = []

    # Number of nodes generated
    generated = 1

    # While the stack is not empty
    while not len(frontier) == 0:
        # Get the last node in the stack, remove it from the stack, and add it to the visited list
        currentNode = frontier.pop()
        visited.append(currentNode)

        # Expand the current node
        children = currentNode.expand(costFunction)

        # Update the number of nodes generated
        generated += len(children)

        # For each child node, if it's state is the goal, return the child node. Otherwise, if the state of the child node has not been reached, add the child node to the queue and it's state to the reached set
        for child in children:
            if child.x == goal.x and child.y == goal.y:
                return (child, generated, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if (child.x, child.y) not in reached:
                reached.add((child.x, child.y))
                frontier.append(child)
    
    # If the goal is not found, return None
    return None

# Random Depth First Search
def RandomDFS(start: Node, goal: Node, costFunction: Callable):
    # Start from the start node
    currentNode = start
    
    # If the start node is the goal node, return the start node
    if currentNode == goal:
        return (currentNode, 1, 1)
    
    # Create a stack to store the nodes to be visited and add the start node to the stack
    frontier = []
    frontier.append(currentNode)

    # Create a set to store the states that have been reached and add the start node's state to the set
    reached = set()
    reached.add((currentNode.x, currentNode.y))

    # Create a list to store the nodes that have been visited
    visited = []

    # Number of nodes generated
    generated = 1

    # While the stack is not empty
    while not len(frontier) == 0:
        # Get the last node in the stack, remove it from the stack, and add it to the visited list
        currentNode = frontier.pop()
        visited.append(currentNode)

        # Expand the current node
        children = currentNode.expand(costFunction)

        # Shuffle the children nodes to make the search random
        shuffle(children)

        # Update the number of nodes generated
        generated += len(children)

        # For each child node, if it's state is the goal, return the child node. Otherwise, if the state of the child node has not been reached, add the child node to the queue and it's state to the reached set
        for child in children:
            if child.x == goal.x and child.y == goal.y:
                return (child, generated, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if (child.x, child.y) not in reached:
                reached.add((child.x, child.y))
                frontier.append(child)
    
    # If the goal is not found, return None
    return None

# Uniform Cost Search
def Dijkstra(start: Node, goal: Node, costFunction: Callable):
    # Start from the start node
    current = start
    
    # Create a priority queue to store the nodes to be visited and add the start node to the queue
    frontier = PriorityQueue()
    frontier.put((0, id(current), current))

    # Create a dictionary to store the states that have been reached and it's nodes. It also adds the start state to the dictionary
    reached = {}
    reached[(current.x, current.y)] = current

    # Create a list to store the nodes that have been visited
    visited = []

    # Number of nodes generated
    generated = 1

    # While the queue is not empty
    while not frontier.empty():
        # Get the first node in the queue, remove it from the queue, and add it to the visited list
        current = frontier.get()[2]
        visited.append(current)
        
        # If the current node's state is the goal, return the current node, the number of nodes reached (generated), and the number of nodes visited
        if current.x == goal.x and current.y == goal.y:
            return (current, generated, len(visited))
        
        # Expand the current node
        children = current.expand(costFunction)

        # Update the number of nodes generated
        generated += len(children)

        # For each child node, if the child node's state is not in the reached dictionary or the cost of the child node is less than the cost of the node in the reached dictionary, add the child node to the reached dictionary and to the queue (Relaxation)
        for child in children:
            if (child.x, child.y) not in reached or child.cost < reached[(child.x, child.y)].cost:
                reached[(child.x, child.y)] = child
                frontier.put((child.cost, id(child), child))
    
    # If the goal node is not found, return None
    return None

def GBFS(start: Node, goal: Node, costFunction: Callable, heuristic: Callable):
    # Start from the start node
    current = start

    # Create a priority queue to store the nodes to be visited and add the start node to the queue
    frontier = PriorityQueue()
    frontier.put((0, id(current), current))  # Priority = f(n) = h(n)

    # Create a dictionary to store the states that have been reached and it's nodes. It also adds the start state to the dictionary
    reached = {}
    reached[(current.x, current.y)] = current

    # List of visited nodes
    visited = []

    # Number of nodes generated
    generated = 1

    # While the queue is not empty
    while not frontier.empty():
        # Remove the node with the lowest f(n) cost
        current = frontier.get()[2]
        visited.append(current)

        # If the current node's state is the goal, return the current node, the number of nodes reached (generated), and the number of nodes visited
        if current.x == goal.x and current.y == goal.y:
            return (current, generated, len(visited))

        # Expand the current node
        children = current.expand(costFunction)

        # Update the number of nodes generated
        generated += len(children)

        for child in children:
            # Calculate the costs
            f_cost = heuristic(child, goal)  # f(n) = h(n)

            # Check if the node should be updated
            if (child.x, child.y) not in reached:
                reached[(child.x, child.y)] = child  # Update the node in the reached dictionary
                frontier.put((f_cost, id(child), child))  # Add to the priority queue

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
