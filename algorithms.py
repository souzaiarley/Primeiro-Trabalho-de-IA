from problem import Problem
from node import Node
from queue import Queue
from queue import PriorityQueue
from typing import Callable
from random import shuffle
from pathCost import getPathCost

# Breadth First Search
def BFS(problem: Problem, costFunction: Callable):
    # Start from the start node
    currentNode = Node(problem.initial[0], problem.initial[1])
    
    # If the start node is the goal node, return the start node
    if problem.isGoal(currentNode.state):
        return (currentNode, 1, 1)
    
    # Create a queue to store the nodes to be visited and add the start node to the queue
    frontier = Queue()
    frontier.put(currentNode)

    # Create a set to store the states that have been reached and add the start node's state to the set
    reached = set()
    reached.add(currentNode.state)

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
            s = child.state

            if problem.isGoal(s):
                return (child, generated, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if s not in reached:
                reached.add(s)
                frontier.put(child)
    
    # If the goal is not found, return None
    return None

# Random Breadth First Search
def RandomBFS(problem: Problem, costFunction: Callable):
    # Start from the start node
    currentNode = Node(problem.initial[0], problem.initial[1])
    
    # If the start node is the goal node, return the start node
    if problem.isGoal(currentNode.state):
        return (currentNode, 1, 1)
    
    # Create a queue to store the nodes to be visited and add the start node to the queue
    frontier = Queue()
    frontier.put(currentNode)

    # Create a set to store the states that have been reached and add the start node's state to the set
    reached = set()
    reached.add(currentNode.state)

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
            s = child.state

            if problem.isGoal(s):
                return (child, generated, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if s not in reached:
                reached.add(s)
                frontier.put(child)
    
    # If the goal is not found, return None
    return None

# Depth First Search
def DFS(problem: Problem, costFunction: Callable):
    # Start from the start node
    currentNode = Node(problem.initial[0], problem.initial[1])
    
    # If the start node is the goal node, return the start node
    if problem.isGoal(currentNode.state):
        return (currentNode, 1, 1)
    
    # Create a stack to store the nodes to be visited and add the start node to the stack
    frontier = []
    frontier.append(currentNode)

    # Create a set to store the states that have been reached and add the start node's state to the set
    reached = set()
    reached.add(currentNode.state)

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
            s = child.state

            if problem.isGoal(s):
                return (child, generated, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if s not in reached:
                reached.add(s)
                frontier.append(child)
    
    # If the goal is not found, return None
    return None

# Random Depth First Search
def RandomDFS(problem: Problem, costFunction: Callable):
    # Start from the start node
    currentNode = Node(problem.initial[0], problem.initial[1])
    
    # If the start node is the goal node, return the start node
    if problem.isGoal(currentNode.state):
        return (currentNode, 1, 1)
    
    # Create a stack to store the nodes to be visited and add the start node to the stack
    frontier = []
    frontier.append(currentNode)

    # Create a set to store the states that have been reached and add the start node's state to the set
    reached = set()
    reached.add(currentNode.state)

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
            s = child.state

            if problem.isGoal(s):
                return (child, generated, len(visited)) # Return the goal node, the number of nodes reached (generated), and the number of nodes visited
            if s not in reached:
                reached.add(s)
                frontier.append(child)
    
    # If the goal is not found, return None
    return None

# Uniform Cost Search
def Dijkstra(problem: Problem, costFunction: Callable):
    # Start from the start node
    currentNode = Node(problem.initial[0], problem.initial[1])
    
    # Create a priority queue to store the nodes to be visited and add the start node to the queue
    frontier = PriorityQueue()
    frontier.put((0, id(currentNode), currentNode))

    # Create a dictionary to store the states that have been reached and it's nodes. It also adds the start state to the dictionary
    reached = {}
    reached[currentNode.state] = currentNode

    # Create a list to store the nodes that have been visited
    visited = []

    # Number of nodes generated
    generated = 1

    # While the queue is not empty
    while not frontier.empty():
        # Get the first node in the queue, remove it from the queue, and add it to the visited list
        currentNode = frontier.get()[2]
        visited.append(currentNode)
        
        # If the current node's state is the goal, return the current node, the number of nodes reached (generated), and the number of nodes visited
        if problem.isGoal(currentNode.state):
            return (currentNode, generated, len(visited))
        
        # Expand the current node
        children = currentNode.expand(costFunction)

        # Update the number of nodes generated
        generated += len(children)

        # For each child node, if the child node's state is not in the reached dictionary or the cost of the child node is less than the cost of the node in the reached dictionary, add the child node to the reached dictionary and to the queue (Relaxation)
        for child in children:
            s = child.state

            if s not in reached or child.cost < reached[s].cost:
                reached[s] = child
                frontier.put((child.cost, id(child), child))
    
    # If the goal node is not found, return None
    return None

def GBFS(problem: Problem, costFunction: Callable, heuristic: Callable):
    # Start from the start node
    currentNode = Node(problem.initial[0], problem.initial[1])

    # Create a priority queue to store the nodes to be visited and add the start node to the queue
    frontier = PriorityQueue()
    frontier.put((0, id(currentNode), currentNode))  # Priority = f(n) = h(n)

    # Create a dictionary to store the states that have been reached and it's nodes. It also adds the start state to the dictionary
    reached = {}
    reached[currentNode.state] = currentNode

    # List of visited nodes
    visited = []

    # Number of nodes generated
    generated = 1

    # While the queue is not empty
    while not frontier.empty():
        # Remove the node with the lowest f(n) cost
        currentNode = frontier.get()[2]
        visited.append(currentNode)

        # If the current node's state is the goal, return the current node, the number of nodes reached (generated), and the number of nodes visited
        if problem.isGoal(currentNode.state):
            currentNode.cost = getPathCost(currentNode.path(), costFunction)
            return (currentNode, generated, len(visited))

        # Expand the current node
        children = currentNode.expand()

        # Update the number of nodes generated
        generated += len(children)

        for child in children:
            s = child.state

            # Calculate the costs
            f_cost = heuristic(s, problem.goal)  # f(n) = h(n)

            # Check if the node should be updated
            if s not in reached:
                reached[s] = child  # Update the node in the reached dictionary
                frontier.put((f_cost, id(child), child))  # Add to the priority queue

    # If the goal is not found, return None
    return None


def AStar(problem: Problem, costFunction: Callable, heuristic: Callable, nodeClass=Node, pharmacies=[]):
    # Start from the start node
    currentNode = nodeClass(problem.initial[0], problem.initial[1], pharmacies=pharmacies)

    # Create the priority queue and add the start node
    frontier = PriorityQueue()
    frontier.put((0, id(currentNode), currentNode))  # Priority = f(n) = g(n) + h(n)

    # Create a dictionary to store the states that have been reached and it's nodes. It also adds the start state to the dictionary
    reached = {}
    reached[currentNode.state] = currentNode

    # List of visited nodes
    visited = []

    # Number of nodes generated
    generated = 1

    # While the queue is not empty
    while not frontier.empty():
        # Remove the node with the lowest f(n) cost
        currentNode = frontier.get()[2]
        visited.append(currentNode)

        # If the current node's state is the goal, return the current node, the number of nodes reached (generated), and the number of nodes visited
        if problem.isGoal(currentNode.state):
            return (currentNode, generated, len(visited))

        # Expand the current node
        children = currentNode.expand(costFunction)

        # Update the number of nodes generated
        generated += len(children)

        # Expand the child nodes
        for child in children:
            s = child.state

            # Calculate the costs
            g_cost = child.cost  # g(n) is already included in the child's cost (updated in expand)
            f_cost = g_cost + heuristic(s, problem.goal)  # f(n) = g(n) + h(n)

            # Check if the node should be updated
            if s not in reached or g_cost < reached[s].cost:
                reached[s] = child  # Update the node in the reached dictionary
                frontier.put((f_cost, id(child), child))  # Add to the priority queue

    # If the goal is not found, return None
    return None
