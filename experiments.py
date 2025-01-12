from node import Node
from algorithms import *
from costFunctions import *
from heuristics import *
from random import randint

# This function returns a string with the result of the search using it's information
def printResult(start: Node, goal: Node, result):
    if result is None:
        return "No solution"

    return f"""\n
            Solution found:
            Start: {start}
            goal: {goal}
            Path: {" -> ".join([str(node) for node in reversed(result[0].path())])}
            Path cost: {result[0].cost}
            Nodes generated: {result[1]}
            Nodes visited: {result[2]}
    """

def Experiment_0():
    with open("experiments/experiment_0.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 0 |\n")
        f.write("|==============|\n")

        startX = int(input("\nEnter the x value for the start node: "))
        startY = int(input("Enter the y value for the start node: "))
        goalX = int(input("Enter the x value for the goal node: "))
        goalY = int(input("Enter the y value for the goal node: "))

        start = Node(startX, startY)
        goal = Node(goalX, goalY)

        f.write(f"\nNodes: Start {start} - Goal {goal}\n")
            
        # Breadth-First Search
        f.write("\n    Breadth-First Search\n")

        # Calling the BFS function with the cost functions
        f.write("\n        Cost function: C_1")
        result = BFS(start, goal, C_1)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_2")
        result = BFS(start, goal, C_2)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_3")
        result = BFS(start, goal, C_3)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_4")
        result = BFS(start, goal, C_4)
        f.write(printResult(start, goal, result))

        # Depth-First Search
        f.write("\n    Depth-First Search\n")

        # Calling the DFS function with the cost functions
        f.write("\n        Cost function: C_1")
        result = DFS(start, goal, C_1)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_2")
        result = DFS(start, goal, C_2)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_3")
        result = DFS(start, goal, C_3)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_4")
        result = DFS(start, goal, C_4)
        f.write(printResult(start, goal, result))

        # Uniform-Cost Search
        f.write("\n    Uniform-Cost Search (Dijkstra)\n")

        # Calling the Dijkstra function with the cost functions
        f.write("\n        Cost function: C_1")
        result = Dijkstra(start, goal, C_1)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_2")
        result = Dijkstra(start, goal, C_2)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_3")
        result = Dijkstra(start, goal, C_3)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_4")
        result = Dijkstra(start, goal, C_4)
        f.write(printResult(start, goal, result))
        
        # Greedy Best-First Search
        f.write("\n    Greedy Best-First Search\n")

        # Calling the Greedy function with the cost functions
        f.write("\n        Cost function: C_1 (euclidean)")
        result = GBFS(start, goal, C_1, euclidean)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_1 (manhattan)")
        result = GBFS(start, goal, C_1, manhattan)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_2 (euclidean)")
        result = GBFS(start, goal, C_2, euclidean)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_2 (manhattan)")
        result = GBFS(start, goal, C_2, manhattan)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_3 (euclidean)")
        result = GBFS(start, goal, C_3, euclidean)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_3 (manhattan)")
        result = GBFS(start, goal, C_3, manhattan)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_4 (euclidean)")
        result = GBFS(start, goal, C_4, euclidean)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_4 (manhattan)")
        result = GBFS(start, goal, C_4, manhattan)
        f.write(printResult(start, goal, result))

        # A* Search
        f.write("\n    A* Search\n")

        # Calling the AStar function with the cost functions
        f.write("\n        Cost function: C_1 (euclidean)")
        result = AStar(start, goal, C_1, euclidean)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_1 (manhattan)")
        result = AStar(start, goal, C_1, manhattan)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_2 (euclidean)")
        result = AStar(start, goal, C_2, euclidean)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_2 (manhattan)")
        result = AStar(start, goal, C_2, manhattan)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_3 (euclidean)")
        result = AStar(start, goal, C_3, euclidean)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_3 (manhattan)")
        result = AStar(start, goal, C_3, manhattan)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_4 (euclidean)")
        result = AStar(start, goal, C_4, euclidean)
        f.write(printResult(start, goal, result))

        f.write("\n        Cost function: C_4 (manhattan)")
        result = AStar(start, goal, C_4, manhattan)
        f.write(printResult(start, goal, result))


# This function runs the experiment 1, saving the results in a file
def Experiment_1():
    with open("experiments/experiment_1.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 1 |\n")
        f.write("|==============|\n")
        
        for i in range(50):
            # Generate random start and goal nodes
            startX = randint(0, 30)
            startY = randint(0, 30)
            goalX = randint(0, 30)
            goalY = randint(0, 30)

            start = Node(startX, startY)
            goal = Node(goalX, goalY)

            f.write(f"\nNodes: Start {start} - Goal {goal}\n")
            
            # Breadth-First Search
            f.write("\n    Breadth-First Search\n")

            # Calling the BFS function with the cost functions
            f.write("\n        Cost function: C_1")
            result = BFS(start, goal, C_1)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_2")
            result = BFS(start, goal, C_2)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_3")
            result = BFS(start, goal, C_3)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_4")
            result = BFS(start, goal, C_4)
            f.write(printResult(start, goal, result))

            # Depth-First Search
            f.write("\n    Depth-First Search\n")

            # Calling the DFS function with the cost functions
            f.write("\n        Cost function: C_1")
            result = DFS(start, goal, C_1)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_2")
            result = DFS(start, goal, C_2)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_3")
            result = DFS(start, goal, C_3)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_4")
            result = DFS(start, goal, C_4)
            f.write(printResult(start, goal, result))

            # Uniform-Cost Search
            f.write("\n    Uniform-Cost Search (Dijkstra)\n")

            # Calling the Dijkstra function with the cost functions
            f.write("\n        Cost function: C_1")
            result = Dijkstra(start, goal, C_1)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_2")
            result = Dijkstra(start, goal, C_2)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_3")
            result = Dijkstra(start, goal, C_3)
            f.write(printResult(start, goal, result))

            f.write("\n        Cost function: C_4")
            result = Dijkstra(start, goal, C_4)
            f.write(printResult(start, goal, result))