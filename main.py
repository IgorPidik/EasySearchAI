__author__ = 'igor'

from SearchAI import *
import numpy as np

class HelloProlem(SearchProblem):
    def __init__(self, goal=None):

        if goal:
            self.goal = goal
        else:
            self.goal = None

    def isGoal(self, state):
        if state == self.goal:
            return True
        return False

    def heuristic(self, state):
        counter = 0
        goal = self.getGoal()
        for i in range(0, len(state)):
            if state[i] == goal[i]:
                counter += 1
        return len(goal) - counter

    def setGoal(self, goal):
        self.goal = goal

    def getGoal(self):
        return self.goal

    def getSuccessor(self, state, action):
        return state + [action]

    def getPossibleActions(self, state):
        if len(state) < len(self.goal):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    # def getNewList(self):
    #     return PriorityQueue()

    def getActionCost(self, action):
        return 1


def main():
    problem = HelloProlem(list("HELLO"))
    astar = DFS(problem)
    astar.getPlan(([], [], 0))



main()
