import costFunctions as c
from heuristics import *
from algorithms import *
from typing import Callable
from node import Node

def test(algorithm: Callable, costFunction: Callable, *heuristic: Callable):
    start = Node(0, 0)
    objective = Node(2, 2)

    if not heuristic:
        result = algorithm(start, objective, costFunction)
    else:
        result = algorithm(start, objective, costFunction, heuristic[0])

    path = result[0].path()

    if result is None:
        print("No solution")
    else:
        print(f"\nSolution found:")
        print("Start:", start)
        print("Objective:", objective)
        print("Path:", end=" ")
        for node in reversed(path):
            print(node, end="")
            if node != objective:
                print(" -> ", end="")
        print(f"\nPath cost: {result[0].cost}")
        print(f"Nodes generated: {result[1]}")
        print(f"Nodes visited: {result[2]}")

if __name__ == "__main__":
    print("Choose a cost function:")
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

    print("Choose an algorithm to run:")
    print("[0] Breadth-First Search")
    print("[1] Depth-First Search")
    print("[2] Dijkstra")
    print("[3] Greedy Search")
    print("[4] A*")
    choice = input("Choice: ")

    if choice == "0":
        print("Running Breadth-First Search with cost function", choice_str)
        test(BFS, costFunction)
    elif choice == "1":
        print("Running Depth-First Search with cost function", choice_str)
        test(DFS, costFunction)
    elif choice == "2":
        print("Running Dijkstra with cost function", choice_str)
        test(Dijkstra, costFunction)
    elif choice == "3" or "4":
        print("Choose a heuristic function:")
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
            # test(Greedy, costFunction, heuristic)
        elif choice == "4":
            print("Running A* with cost function", choice_str, " and", heuristic_str, "heuristic")
            test(AStar, costFunction, heuristic)
    else:
        print("Invalid choice.")
