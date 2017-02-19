__author__ = 'igor'

from abc import ABCMeta, abstractmethod
from util import *


class SearchProblem(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, goal=None):
        pass

    @abstractmethod
    def setGoal(self, goal):
        pass

    @abstractmethod
    def getGoal(self):
        pass

    @abstractmethod
    def isGoal(self, state):
        pass

    @abstractmethod
    def getPossibleActions(self, state):
        pass

    @abstractmethod
    def getActionCost(self, action):
        return 1

    @abstractmethod
    def getSuccessor(self, state, action):
        pass

    @abstractmethod
    def heuristic(self, state):
        pass

        # # in case you need list with overridden functions(for example contains) otherwise use default list
        # @abstractmethod
        # def getNewList(self):
        #     return []


class DFS(object):
    def __init__(self, problem=None):
        self.problem = None
        if problem:
            self.problem = problem

    def setProblem(self, problem):
        self.problem = problem

    def getPlan(self, initState):
        if not self.problem:
            raise ValueError("problem undefined")

        states = Stack()
        expanded = []
        states.append(initState)

        while len(states) > 0:
            print("states len", len(states))

            (state, actions, cost) = states.pop()
            print state
            if state not in expanded:
                expanded.append(state)

                if self.problem.isGoal(state):
                    return actions

                for action in self.problem.getPossibleActions(state):
                    newState = self.problem.getSuccessor(state, action)
                    newActions = actions + [action]
                    newCost = 0 #cost is irrelevant for DFS
                    states.append((newState, newActions, newCost))

        raise ValueError("failure")
        return []


class BFS(object):
    def __init__(self, problem=None):
        self.problem = None
        if problem:
            self.problem = problem

    def setProblem(self, problem):
        self.problem = problem

    def getPlan(self, initState):
        if not self.problem:
            raise ValueError("problem undefined")

        states = Queue()
        expanded = []
        states.append(initState)

        while len(states) > 0:
            print("states len", len(states))

            (state, actions, cost) = states.pop()
            print state
            if state not in expanded:
                expanded.append(state)

                if self.problem.isGoal(state):
                    print "goal:"
                    print state
                    return actions

                for action in self.problem.getPossibleActions(state):
                    newState = self.problem.getSuccessor(state, action)
                    newActions = actions + [action]
                    newCost = self.problem.heuristic(newState) + self.problem.getActionCost(action)
                    states.append((newState, newActions, newCost))
        
        raise ValueError("failure")
        return []


class UCS(object):
    def __init__(self, problem=None):
        self.problem = None
        if problem:
            self.problem = problem

    def setProblem(self, problem):
        self.problem = problem

    def getPlan(self, initState):
        if not self.problem:
            raise ValueError("problem undefined")

        states = PriorityQueue()
        expanded = []
        states.append(initState)

        while len(states) > 0:
            print("states len", len(states))
            (state, actions, cost) = states.pop()
            if state not in expanded:
                expanded.append(state)
                print state
                if self.problem.isGoal(state):
                    print "goal:"
                    print state
                    return actions

                for action in self.problem.getPossibleActions(state):
                    newState = self.problem.getSuccessor(state, action)
                    newActions = actions + [action]
                    newCost = self.problem.getActionCost(action) + cost
                    states.append((newState, newActions, newCost))
        raise ValueError("failure")
        return []


class AStar(object):
    def __init__(self, problem=None):
        self.problem = None
        if problem:
            self.problem = problem

    def setProblem(self, problem):
        self.problem = problem

    def getPlan(self, initState):
        if not self.problem:
            raise ValueError("problem undefined")

        states = PriorityQueue()
        expanded = []
        states.append(initState)

        while len(states) > 0:
            print("states len", len(states))
            (state, actions, cost) = states.pop()
            if state not in expanded:
                expanded.append(state)
                if self.problem.isGoal(state):
                    print "goal:"
                    print state
                    return actions

                for action in self.problem.getPossibleActions(state):
                    newState = self.problem.getSuccessor(state, action)
                    newActions = actions + [action]
                    newCost = self.problem.heuristic(newState) + self.problem.getActionCost(action)
                    states.append((newState, newActions, newCost))
        raise ValueError("failure")
        return []
