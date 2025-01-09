from node import Node
from algorithms import BFS
from algorithms import DFS
from algorithms import Dijkstra
import costFunctions as c


def main():
    start = Node(0, 0)
    objective = Node(1, 8)
    result = Dijkstra(start, objective, c.C_3)
    path = result[0].path()

    if result is None:
        print("No solution")
    else:
        print(f"Solution found:")
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
    main()