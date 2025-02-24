from problem import Problem
from node import *
from algorithms import *
from costFunctions import *
from heuristics import *
from random import randint
from pathCost import getPathCost

# This function returns a string with the result of the search using it's information
def printResult(problem: Problem, result):
    if result is None:
        return "No solution"

    return f"""\n
            Solution found:
            Start: {problem.initial}
            goal: {problem.goal}
            Path: {" -> ".join([str(node) for node in reversed(result[0].path())])}
            Path cost: {result[0].cost}
            Nodes generated: {result[1]}
            Nodes visited: {result[2]}
    """


def Experiment_0():
    with open("experiments_output/experiment_0.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 0 |\n")
        f.write("|==============|\n")

        startX = int(input("\nEnter the x value for the start node: "))
        startY = int(input("Enter the y value for the start node: "))
        goalX = int(input("Enter the x value for the goal node: "))
        goalY = int(input("Enter the y value for the goal node: "))

        problem = Problem((startX, startY), (goalX, goalY))
        
        f.write(f"\nNodes: Start {problem.initial} - Goal {problem.goal}\n")
            
        # Breadth-First Search
        f.write("\n    Breadth-First Search\n")

        # Calling the BFS function with the cost functions
        f.write("\n        Cost function: C_1")
        result = BFS(problem, C_1)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_2")
        result = BFS(problem, C_2)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_3")
        result = BFS(problem, C_3)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_4")
        result = BFS(problem, C_4)
        f.write(printResult(problem, result))

        # Depth-First Search
        f.write("\n    Depth-First Search\n")

        # Calling the DFS function with the cost functions
        f.write("\n        Cost function: C_1")
        result = DFS(problem, C_1)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_2")
        result = DFS(problem, C_2)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_3")
        result = DFS(problem, C_3)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_4")
        result = DFS(problem, C_4)
        f.write(printResult(problem, result))

        # Uniform-Cost Search
        f.write("\n    Uniform-Cost Search (Dijkstra)\n")

        # Calling the Dijkstra function with the cost functions
        f.write("\n        Cost function: C_1")
        result = Dijkstra(problem, C_1)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_2")
        result = Dijkstra(problem, C_2)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_3")
        result = Dijkstra(problem, C_3)
        f.write(printResult(problem, result))

        f.write("\n        Cost function: C_4")
        result = Dijkstra(problem, C_4)
        f.write(printResult(problem, result))
        
        f.write("\n    Greedy Best-First Search (euclidean)\n")

        # Calling the BFS function
        result = GBFS(problem, C_1, euclidean)

        # Getting the goal node
        goalNode = result[0]
        
        # Getting the path from the goal node to the start node
        path = goalNode.path()

        f.write(f"\n            Solution Found:\n")
        f.write(f"            Start: {problem.initial}\n")
        f.write(f"            Goal: {problem.goal}\n")
        f.write(f"            Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
        f.write(f"            Path cost: {goalNode.cost} (C1)\n")
        f.write(f"            Path cost: {getPathCost(path, C_2)} (C2)\n")
        f.write(f"            Path cost: {getPathCost(path, C_3)} (C3)\n")
        f.write(f"            Path cost: {getPathCost(path, C_4)} (C4)\n")
        f.write(f"            Nodes generated: {result[1]}\n")
        f.write(f"            Nodes visited: {result[2]}\n")

        f.write("\n    Greedy Best-First Search (manhattan)\n")

        # Calling the BFS function
        result = GBFS(problem, C_1, manhattan)

        # Getting the goal node
        goalNode = result[0]
        
        # Getting the path from the goal node to the start node
        path = goalNode.path()

        f.write(f"\n            Solution Found:\n")
        f.write(f"            Start: {problem.initial}\n")
        f.write(f"            Goal: {problem.goal}\n")
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
                result = AStar(problem, cost_function, heuristic)
                f.write(printResult(problem, result))

# This function runs the experiment 1, saving the results in a file
def Experiment_1():
    with open("experiments_output/experiment_1.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 1 |\n")
        f.write("|==============|\n")
        
        for i in range(50):
            # Generate random start and goal nodes
            startX = randint(0, 30)
            startY = randint(0, 30)
            goalX = randint(0, 30)
            goalY = randint(0, 30)

            problem = Problem((startX, startY), (goalX, goalY))

            f.write(f"\nNodes: Start {problem.initial} - Goal {problem.goal}\n")
            
            # Breadth-First Search
            f.write("\n    Breadth-First Search\n")

            # Calling the BFS function with the cost functions
            f.write("\n        Cost function: C_1")
            result = BFS(problem, C_1)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_2")
            result = BFS(problem, C_2)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_3")
            result = BFS(problem, C_3)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_4")
            result = BFS(problem, C_4)
            f.write(printResult(problem, result))

            # Depth-First Search
            f.write("\n    Depth-First Search\n")

            # Calling the DFS function with the cost functions
            f.write("\n        Cost function: C_1")
            result = DFS(problem, C_1)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_2")
            result = DFS(problem, C_2)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_3")
            result = DFS(problem, C_3)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_4")
            result = DFS(problem, C_4)
            f.write(printResult(problem, result))

            # Uniform-Cost Search
            f.write("\n    Uniform-Cost Search (Dijkstra)\n")

            # Calling the Dijkstra function with the cost functions
            f.write("\n        Cost function: C_1")
            result = Dijkstra(problem, C_1)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_2")
            result = Dijkstra(problem, C_2)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_3")
            result = Dijkstra(problem, C_3)
            f.write(printResult(problem, result))

            f.write("\n        Cost function: C_4")
            result = Dijkstra(problem, C_4)
            f.write(printResult(problem, result))


# This function runs the experiment 2, saving the results in a file
def Experiment_2():
    with open("experiments_output/experiment_2.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 2 |\n")
        f.write("|==============|\n")

        for i in range(50):
            # Generate random coordinates for the start and goal nodes
            startX = randint(0, 30)
            startY = randint(0, 30)
            goalX = randint(0, 30)
            goalY = randint(0, 30)

            problem = Problem((startX, startY), (goalX, goalY))

            # Log the start and goal nodes to the file
            f.write(f"\nIteration {i + 1}:\n")
            f.write(f"Nodes: Start {problem.initial} - Goal {problem.goal}\n")

            # Perform Uniform-Cost Search (Dijkstra) for each cost function
            f.write("\n    Uniform-Cost Search (Dijkstra)\n")
            for cost_function, label in [(C_1, "C_1"), (C_2, "C_2"), (C_3, "C_3"), (C_4, "C_4")]:
                f.write(f"\n        Cost function: {label}")
                result = Dijkstra(problem, cost_function)
                f.write(printResult(problem, result))

            # Perform A* Search for each combination of cost function and heuristic
            f.write("\n    A* Search\n")
            for cost_function, cost_label in [(C_1, "C_1"), (C_2, "C_2"), (C_3, "C_3"), (C_4, "C_4")]:
                for heuristic, heuristic_label in [(euclidean, "Euclidean (H1)"), (manhattan, "Manhattan (H2)")]:
                    f.write(f"\n        Cost function: {cost_label}, Heuristic: {heuristic_label}")
                    result = AStar(problem, cost_function, heuristic)
                    f.write(printResult(problem, result))

#This function runs the experiment 3, saving the results in a file
def Experiment_3():
    with open("experiments_output/experiment_3.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 3 |\n")
        f.write("|==============|\n")

        for i in range(50):
            # Generate random start and goal nodes
            startX = randint(0, 30)
            startY = randint(0, 30)
            goalX = randint(0, 30)
            goalY = randint(0, 30)

            problem = Problem((startX, startY), (goalX, goalY))

            f.write(f"\nNodes: Start {problem.initial} - Goal {problem.goal}\n")

            # Greedy Best-First Search (euclidean)
            f.write("\n    Greedy Best-First Search (euclidean)\n")

            # Calling the GBFS function with euclidean
            result = GBFS(problem, C_1, euclidean)

            # Getting the goal node
            goalNode = result[0]
            
            # Getting the path from the goal node to the start node
            path = goalNode.path()

            f.write(f"\n            Solution Found:\n")
            f.write(f"            Start: {problem.initial}\n")
            f.write(f"            Goal: {problem.goal}\n")
            f.write(f"            Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
            f.write(f"            Path cost: {goalNode.cost} (C1)\n")
            f.write(f"            Path cost: {getPathCost(path, C_2)} (C2)\n")
            f.write(f"            Path cost: {getPathCost(path, C_3)} (C3)\n")
            f.write(f"            Path cost: {getPathCost(path, C_4)} (C4)\n")
            f.write(f"            Nodes generated: {result[1]}\n")
            f.write(f"            Nodes visited: {result[2]}\n")

            #Greedy Best-First Search(manhattan)
            f.write("\n    Greedy Best-First Search (manhattan)\n")

            # Calling the GBFS function with manhattan
            result = GBFS(problem, C_1, manhattan)

            # Getting the goal node
            goalNode = result[0]
            
            # Getting the path from the goal node to the start node
            path = goalNode.path()

            f.write(f"\n        Iteration: {i+1}\n")
            f.write(f"\n            Solution Found:\n")
            f.write(f"            Start: {problem.initial}\n")
            f.write(f"            Goal: {problem.goal}\n")
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
                    result = AStar(problem, cost_function, heuristic)
                    f.write(printResult(problem, result))


# This function runs the experiment 4, saving the results in a file
def Experiment_4():
    with open("experiments_output/experiment_4.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 4 |\n")
        f.write("|==============|\n")

        for i in range(20):
            # Generate random start and goal nodes
            startX = randint(0, 30)
            startY = randint(0, 30)
            goalX = randint(0, 30)
            goalY = randint(0, 30)

            problem = Problem((startX, startY), (goalX, goalY))

            f.write(f"\nNodes: Start {problem.initial} - Goal {problem.goal}\n")

            # Breadth-First Search (random)
            f.write("\n    Random Breadth-First Search\n")

            for j in range(10):
                # Calling the BFS function
                result = RandomBFS(problem, C_1)

                # Getting the goal node
                goalNode = result[0]
                
                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Iteration: {j+1}\n")
                f.write(f"\n            Solution Found:\n")
                f.write(f"            Start: {problem.initial}\n")
                f.write(f"            Goal: {problem.goal}\n")
                f.write(f"            Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"            Path cost: {goalNode.cost} (C1)\n")
                f.write(f"            Path cost: {getPathCost(path, C_2)} (C2)\n")
                f.write(f"            Path cost: {getPathCost(path, C_3)} (C3)\n")
                f.write(f"            Path cost: {getPathCost(path, C_4)} (C4)\n")
                f.write(f"            Nodes generated: {result[1]}\n")
                f.write(f"            Nodes visited: {result[2]}\n")

            # Depth-First Search (random)
            f.write("\n    Random Depth-First Search\n")

            for j in range(10):
                # Calling the DFS function
                result = RandomDFS(problem, C_1)

                # Getting the goal node
                goalNode = result[0]
                
                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Iteration: {j+1}\n")
                f.write(f"\n            Solution Found:\n")
                f.write(f"            Start: {problem.initial}\n")
                f.write(f"            Goal: {problem.goal}\n")
                f.write(f"            Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"            Path cost: {goalNode.cost} (C1)\n")
                f.write(f"            Path cost: {getPathCost(path, C_2)} (C2)\n")
                f.write(f"            Path cost: {getPathCost(path, C_3)} (C3)\n")
                f.write(f"            Path cost: {getPathCost(path, C_4)} (C4)\n")
                f.write(f"            Nodes generated: {result[1]}\n")
                f.write(f"            Nodes visited: {result[2]}\n")

# This function runs the experiment 5, saving the results in a file
def Experiment_5():
    with open("experiments_output/experiment_5.txt", "w") as f:
        f.write("|==============|\n")
        f.write("| Experiment 5 |\n")
        f.write("|==============|\n")
        for i in range(25):
                # Generate random start and goal nodes
                startX = randint(0, 30)
                startY = randint(0, 30)
                goalX = randint(0, 30)
                goalY = randint(0, 30)

                problem = Problem((startX, startY, False), (goalX, goalY, True))

                # Generate random coordinates for the pharmacies
                pharmacies = []

                while len(pharmacies) != 4:
                    x = randint(0, 30)
                    y = randint(0, 30)
                    if (x, y) not in pharmacies:
                        pharmacies.append((x, y))

                f.write(f"\nNodes: Start {(startX, startY)} - Goal {(goalX, goalY)}\n")

                f.write("Pharmacies: " + " - ".join([f"({x}, {y})" for x, y in pharmacies]) + "\n")

                
                f.write(f"\n    A* Search using C1 and H1\n")

                result = AStar(problem, C_1, euclidean, ExperimentFiveNode, pharmacies)

                # Getting the goal node
                goalNode = result[0]

                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Solution Found:\n")
                f.write(f"        Start: {problem.initial}\n")
                f.write(f"        Goal: {problem.goal}\n")
                f.write(f"        Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"        Path cost: {goalNode.cost}\n")
                f.write(f"        Nodes generated: {result[1]}\n")
                f.write(f"        Nodes visited: {result[2]}\n")

                


                f.write(f"\n    A* Search using C1 and H2\n")

                result = AStar(problem, C_1, manhattan, ExperimentFiveNode, pharmacies)

                # Getting the goal node
                goalNode = result[0]

                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Solution Found:\n")
                f.write(f"        Start: {problem.initial}\n")
                f.write(f"        Goal: {problem.goal}\n")
                f.write(f"        Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"        Path cost: {goalNode.cost}\n")
                f.write(f"        Nodes generated: {result[1]}\n")
                f.write(f"        Nodes visited: {result[2]}\n")


                

                f.write(f"\n    A* Search using C2 and H1\n")

                result = AStar(problem, C_2, euclidean, ExperimentFiveNode, pharmacies)

                # Getting the goal node
                goalNode = result[0]

                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Solution Found:\n")
                f.write(f"        Start: {problem.initial}\n")
                f.write(f"        Goal: {problem.goal}\n")
                f.write(f"        Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"        Path cost: {goalNode.cost}\n")
                f.write(f"        Nodes generated: {result[1]}\n")
                f.write(f"        Nodes visited: {result[2]}\n")
                
                


                f.write(f"\n    A* Search using C2 and H2\n")

                result = AStar(problem, C_2, manhattan, ExperimentFiveNode, pharmacies)

                # Getting the goal node
                goalNode = result[0]

                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Solution Found:\n")
                f.write(f"        Start: {problem.initial}\n")
                f.write(f"        Goal: {problem.goal}\n")
                f.write(f"        Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"        Path cost: {goalNode.cost}\n")
                f.write(f"        Nodes generated: {result[1]}\n")
                f.write(f"        Nodes visited: {result[2]}\n")




                f.write(f"\n    A* Search using C3 and H1\n")

                result = AStar(problem, C_3, euclidean, ExperimentFiveNode, pharmacies)

                # Getting the goal node
                goalNode = result[0]

                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Solution Found:\n")
                f.write(f"        Start: {problem.initial}\n")
                f.write(f"        Goal: {problem.goal}\n")
                f.write(f"        Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"        Path cost: {goalNode.cost}\n")
                f.write(f"        Nodes generated: {result[1]}\n")
                f.write(f"        Nodes visited: {result[2]}\n")




                f.write(f"\n    A* Search using C3 and H2\n")

                result = AStar(problem, C_3, manhattan, ExperimentFiveNode, pharmacies)

                # Getting the goal node
                goalNode = result[0]

                # Getting the path from the goal node to the start node
                path = goalNode.path()

                f.write(f"\n        Solution Found:\n")
                f.write(f"        Start: {problem.initial}\n")
                f.write(f"        Goal: {problem.goal}\n")
                f.write(f"        Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"        Path cost: {goalNode.cost}\n")
                f.write(f"        Nodes generated: {result[1]}\n")
                f.write(f"        Nodes visited: {result[2]}\n")




                f.write(f"\n    A* Search using C4 and H1\n")

                result = AStar(problem, C_4, euclidean, ExperimentFiveNode, pharmacies)

                # Getting the goal node
                goalNode = result[0]

                # Getting the path from the goal node to the start node
                path = goalNode.path()
                f.write(f"\n        Solution Found:\n")
                f.write(f"        Start: {problem.initial}\n")
                f.write(f"        Goal: {problem.goal}\n")
                f.write(f"        Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"        Path cost: {goalNode.cost}\n")
                f.write(f"        Nodes generated: {result[1]}\n")
                f.write(f"        Nodes visited: {result[2]}\n")




                f.write(f"\n    A* Search using C4 and H2\n")

                result = AStar(problem, C_4, manhattan, ExperimentFiveNode, pharmacies)

                # Getting the goal node
                goalNode = result[0]

                # Getting the path from the goal node to the start node
                path = goalNode.path()
                f.write(f"\n        Solution Found:\n")
                f.write(f"        Start: {problem.initial}\n")
                f.write(f"        Goal: {problem.goal}\n")
                f.write(f"        Path: {' -> '.join([str(node) for node in reversed(path)])}\n")
                f.write(f"        Path cost: {goalNode.cost}\n")
                f.write(f"        Nodes generated: {result[1]}\n")
                f.write(f"        Nodes visited: {result[2]}\n")