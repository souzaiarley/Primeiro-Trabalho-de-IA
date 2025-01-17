from abc import ABC, abstractmethod

class Problem:
    # initial and goal are tuples in (x, y) format
    def __init__(self, initial: tuple, goal: tuple):
        self.initial = initial
        self.goal = goal
    
    def isGoal(self, state):
        return state == self.goal