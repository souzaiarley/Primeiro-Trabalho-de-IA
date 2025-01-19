import costFunctions as c
from heuristics import *
from algorithms import *
from typing import Callable
from problem import Problem
from node import *

def test(algorithm: Callable, costFunction: Callable, *heuristic: Callable, problem: Problem):
    if not heuristic:
        result = algorithm(problem, costFunction)
    else:
        result = algorithm(problem, costFunction, heuristic[0])

    path = result[0].path()

    if result is None:
        print("No solution")
    else:
        print(f"\nSolution found:")
        print("Start:", problem.initial)
        print("Objective:", problem.goal)
        print("Path:", end=" ")
        for node in reversed(path):
            print(node, end="")
            if node.state != problem.goal:
                print(" -> ", end="")
        print(f"\nPath cost: {result[0].cost}")
        print(f"Nodes generated: {result[1]}")
        print(f"Nodes visited: {result[2]}")

if __name__ == "__main__":
    startX = int(input("\nEnter the x value for the start node: "))
    startY = int(input("Enter the y value for the start node: "))
    goalX = int(input("Enter the x value for the goal node: "))
    goalY = int(input("Enter the y value for the goal node: "))

    problem = Problem((startX, startY), (goalX, goalY))

    print("\nChoose a cost function:")
    print("[0] C_1")
    print("[1] C_2")
    print("[2] C_3")
    print("[3] C_4")
    costFunction = input("Choice: ")
    if costFunction == "0":
        costFunction = c.C_1
        choice_str = "C_1"
    elif costFunction == "1":
        costFunction = c.C_2
        choice_str = "C_2"
    elif costFunction == "2":
        costFunction = c.C_3
        choice_str = "C_3"
    elif costFunction == "3":
        costFunction = c.C_4
        choice_str = "C_4"
    else:
        print("Invalid choice.")
        exit()

    print("\nChoose an algorithm to run:")
    print("[0] Breadth-First Search")
    print("[1] Depth-First Search")
    print("[2] Dijkstra")
    print("[3] Greedy Search")
    print("[4] A*")
    choice = input("Choice: ")

    if choice == "0":
        print("Running Breadth-First Search with cost function", choice_str)
        test(BFS, costFunction, problem=problem)
    elif choice == "1":
        print("Running Depth-First Search with cost function", choice_str)
        test(DFS, costFunction, problem=problem)
    elif choice == "2":
        print("Running Dijkstra with cost function", choice_str)
        test(Dijkstra, costFunction, problem=problem)
    elif choice == "3" or "4":
        print("\nChoose a heuristic function:")
        print("[0] euclidean")
        print("[1] manhattan")
        heuristic_str = input("Choice: ")
        if heuristic_str == "0":
            heuristic = euclidean
            heuristic_str = "euclidean"
        elif heuristic_str == "1":
            heuristic = manhattan
            heuristic_str = "manhattan"
        else:
            print("Invalid choice.")
            exit()
        if choice == "3":
            print("Running Greedy Search with cost function", choice_str, "and heuristic", heuristic_str)
            test(GBFS, costFunction, heuristic, problem=problem)
        elif choice == "4":
            print("\nDo you want to passa a pharmacy list? [y/n]")
            choice = input("Choice: ")
            choice = choice.lower()
            if choice == "y":
                pharmacies = []
                
                while len(pharmacies) != 4:
                    print(f"\nPharmacies: {len(pharmacies)}/4")
                    x = int(input("Enter the x value for the pharmacy node: "))
                    y = int(input("Enter the y value for the pharmacy node: "))
                    if x < 0 or x > 30 or y < 0 or y > 30:
                        print("Invalid coordinates.")
                    else:
                        if (x, y) not in pharmacies:
                            pharmacies.append((x, y))
                        else:
                            print("This pharmacy is already in the list.")

                problem = Problem((startX, startY, False), (goalX, goalY, True))

                print("\nRunning A* with cost function", choice_str, " and", heuristic_str, "heuristic")

                result = AStar(problem, costFunction, heuristic, ExperimentFiveNode, pharmacies)
                goalNode = result[0]
                path = goalNode.path()

                print(f"\nSolution Found:")
                print(f"Start: {(startX, startY)}")
                print(f"Goal: {(goalX, goalY)}")
                print("Pharmacies: " + " - ".join([f"({x}, {y})" for x, y in pharmacies]))
                print(f"Path: {' -> '.join([str(node) for node in reversed(path)])}")
                print(f"Path cost: {goalNode.cost}")
                print(f"Nodes generated: {result[1]}")
                print(f"Nodes visited: {result[2]}")

            elif choice == "n":
                print("Running A* with cost function", choice_str, " and", heuristic_str, "heuristic")
                test(AStar, costFunction, heuristic, problem=problem)
            else:
                print("Invalid choice.")
    else:
        print("Invalid choice.")
