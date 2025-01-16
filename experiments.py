from node import Node
from algorithms import *
from costFunctions import *
from heuristics import *
from random import randint
from pathCost import getPathCost

# This function returns the cost of a path using a cost function
def getPathCost(path: list, costFunction: Callable):
    totalCost = 0
    path = path[::-1]

    for i in range(len(path) - 1):
        edgeCosts = costFunction(path[i+1].depth)

        if path[i+1].x > path[i].x or path[i+1].x < path[i].x:
            totalCost += edgeCosts[0]
        else:
            totalCost += edgeCosts[1]

    return totalCost

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


# This function runs the experiment 2, saving the results in a file
def Experiment_2():
    with open("experiments/experiment_2.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 2 |\n")
        f.write("|==============|\n")

        for i in range(50):
            # Generate random coordinates for the start and goal nodes
            startX = randint(0, 30)
            startY = randint(0, 30)
            goalX = randint(0, 30)
            goalY = randint(0, 30)

            # Create Node objects for the start and goal points
            start = Node(startX, startY)
            goal = Node(goalX, goalY)

            # Log the start and goal nodes to the file
            f.write(f"\nIteration {i + 1}:\n")
            f.write(f"Nodes: Start {start} - Goal {goal}\n")

            # Perform Uniform-Cost Search (Dijkstra) for each cost function
            f.write("\n    Uniform-Cost Search (Dijkstra)\n")
            for cost_function, label in [(C_1, "C_1"), (C_2, "C_2"), (C_3, "C_3"), (C_4, "C_4")]:
                f.write(f"\n        Cost function: {label}")
                result = Dijkstra(start, goal, cost_function)
                f.write(printResult(start, goal, result))

            # Perform A* Search for each combination of cost function and heuristic
            f.write("\n    A* Search\n")
            for cost_function, cost_label in [(C_1, "C_1"), (C_2, "C_2"), (C_3, "C_3"), (C_4, "C_4")]:
                for heuristic, heuristic_label in [(euclidean, "Euclidean (H1)"), (manhattan, "Manhattan (H2)")]:
                    f.write(f"\n        Cost function: {cost_label}, Heuristic: {heuristic_label}")
                    result = AStar(start, goal, cost_function, heuristic)
                    f.write(printResult(start, goal, result))

def Experiment_3():
    with open("experiments/experiment_3.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 3 |\n")
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

            # Breadth-First Search (random)
            f.write("\n    Greedy Best-First Search(euclidean)\n")

            # Calling the BFS function
            result = GBFS(start, goal, C_1, euclidean)

            # Getting the goal node
            goalNode = result[0]
            
            # Getting the path from the goal node to the start node
            path = goalNode.path()

            f.write(f"\n            Solution Found:\n")
            f.write(f"            Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
            f.write(f"            Path cost: {goalNode.cost} (C1)\n")
            f.write(f"            Path cost: {getPathCost(path, C_2)} (C2)\n")
            f.write(f"            Path cost: {getPathCost(path, C_3)} (C3)\n")
            f.write(f"            Path cost: {getPathCost(path, C_4)} (C4)\n")
            f.write(f"            Nodes generated: {result[1]}\n")
            f.write(f"            Nodes visited: {result[2]}\n")

            f.write("\n    Greedy Best-First Search(manhattan)\n")

            # Calling the BFS function
            result = GBFS(start, goal, C_1, manhattan)

            # Getting the goal node
            goalNode = result[0]
            
            # Getting the path from the goal node to the start node
            path = goalNode.path()

            f.write(f"\n            Solution Found:\n")
            f.write(f"            Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
            f.write(f"            Path cost: {goalNode.cost} (C1)\n")
            f.write(f"            Path cost: {getPathCost(path, C_2)} (C2)\n")
            f.write(f"            Path cost: {getPathCost(path, C_3)} (C3)\n")
            f.write(f"            Path cost: {getPathCost(path, C_4)} (C4)\n")
            f.write(f"            Nodes generated: {result[1]}\n")
            f.write(f"            Nodes visited: {result[2]}\n")

            # Perform A* Search for each combination of cost function and heuristic
            f.write("\n    A* Search\n")
            for cost_function, cost_label in [(C_1, "C_1"), (C_2, "C_2"), (C_3, "C_3"), (C_4, "C_4")]:
                for heuristic, heuristic_label in [(euclidean, "Euclidean (H1)"), (manhattan, "Manhattan (H2)")]:
                    f.write(f"\n        Cost function: {cost_label}, Heuristic: {heuristic_label}")
                    result = AStar(start, goal, cost_function, heuristic)
                    f.write(printResult(start, goal, result))


            
# This function runs the experiment 4, saving the results in a file
def Experiment_4():
    with open("experiments/experiment_4.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 4 |\n")
        f.write("|==============|\n")

        for i in range(20):
            # Generate random start and goal nodes
            startX = randint(0, 30)
            startY = randint(0, 30)
            goalX = randint(0, 30)
            goalY = randint(0, 30)

            start = Node(startX, startY)
            goal = Node(goalX, goalY)

            f.write(f"\nNodes: Start {start} - Goal {goal}\n")

            # Breadth-First Search (random)
            f.write("\n    Random Breadth-First Search\n")

            for i in range(10):
                # Calling the BFS function
                result = RandomBFS(start, goal, C_1)

                # Getting the goal node
                goalNode = result[0]
                
                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Iteration: {i+1}\n")
                f.write(f"\n            Solution Found:\n")
                f.write(f"            Start: {start}\n")
                f.write(f"            Goal: {goal}\n")
                f.write(f"            Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"            Path cost: {goalNode.cost} (C1)\n")
                f.write(f"            Path cost: {getPathCost(path, C_2)} (C2)\n")
                f.write(f"            Path cost: {getPathCost(path, C_3)} (C3)\n")
                f.write(f"            Path cost: {getPathCost(path, C_4)} (C4)\n")
                f.write(f"            Nodes generated: {result[1]}\n")
                f.write(f"            Nodes visited: {result[2]}\n")

            # Depth-First Search (random)
            f.write("\n    Random Depth-First Search\n")

            for i in range(10):
                # Calling the DFS function
                result = RandomDFS(start, goal, C_1)

                # Getting the goal node
                goalNode = result[0]
                
                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Iteration: {i+1}\n")
                f.write(f"\n            Solution Found:\n")
                f.write(f"            Start: {start}\n")
                f.write(f"            Goal: {goal}\n")
                f.write(f"            Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"            Path cost: {goalNode.cost} (C1)\n")
                f.write(f"            Path cost: {getPathCost(path, C_2)} (C2)\n")
                f.write(f"            Path cost: {getPathCost(path, C_3)} (C3)\n")
                f.write(f"            Path cost: {getPathCost(path, C_4)} (C4)\n")
                f.write(f"            Nodes generated: {result[1]}\n")
                f.write(f"            Nodes visited: {result[2]}\n")
