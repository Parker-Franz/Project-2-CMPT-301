# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()

    fringe.push((None, problem.getStartState(), None, 0))
    visited = dict()

    def addSuccesorsToFringe(start, cost):
        for next, action, added_cost in problem.getSuccessors(start):
            if hash(next) not in visited:
                fringe.push((start, next, action, cost + added_cost))

    def pathTo(end):
        state, action = visited[hash(end)]
        actions = []

        while action is not None:
            actions.append(action)
            state, action = visited[hash(state)]

        return actions[::-1]

    while not fringe.isEmpty():
        start, next, action, cost = fringe.pop()

        if hash(next) in visited:
            continue

        visited[hash(next)] = (start, action)

        if problem.isGoalState(next):
            return pathTo(next)

        addSuccesorsToFringe(next, cost)

    return []

def breadthFirstSearch(problem):
    fringe = [] 
    visited = []
    fringe.append([problem.getStartState(), []])
    print(problem.getStartState())
    while len(fringe) >0:  
        current,direction = fringe.pop()
        if current not in visited:
            visited.append(current)
            if (problem.isGoalState(current)):   
                return direction
            for coordinates,  directions,  cost in problem.getSuccessors(current): 
        
                fringe.insert(0, (coordinates,direction+[directions]))
    return visited

def lowestCostFirst(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    def fringeFn(item):
        state_s, state_e, action, cost = item
        return cost
    fringe = util.PriorityQueueWithFunction(fringeFn)

    fringe.push((None, problem.getStartState(), None, 0))
    visited = dict()

    def addSuccesorsToFringe(start, cost):
        for next, action, added_cost in problem.getSuccessors(start):
            if hash(next) not in visited:
                fringe.push((start, next, action, cost + added_cost))

    def pathTo(end):
        state, action = visited[hash(end)]
        actions = []

        while action is not None:
            actions.append(action)
            state, action = visited[hash(state)]

        return actions[::-1]

    while not fringe.isEmpty():
        start, next, action, cost = fringe.pop()

        if hash(next) in visited:
            continue

        visited[hash(next)] = (start, action)

        if problem.isGoalState(next):
            return pathTo(next)

        addSuccesorsToFringe(next, cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    def fringeFn(item):
        state_s, state_e, action, cost = item
        return cost + heuristic(state_e, problem=problem)
    fringe = util.PriorityQueueWithFunction(fringeFn)
    fringe.push((None, problem.getStartState(), None, 0))
    visited = dict()

    def addSuccesorsToFringe(start, cost):
        for next, action, added_cost in problem.getSuccessors(start):
            if hash(next) not in visited:
                fringe.push((start, next, action, cost + added_cost))

    def pathTo(end):
        state, action = visited[hash(end)]
        actions = []

        while action is not None:
            actions.append(action)
            state, action = visited[hash(state)]

        return actions[::-1]

    while not fringe.isEmpty():
        start, next, action, cost = fringe.pop()

        if hash(next) in visited:
            continue

        visited[hash(next)] = (start, action)

        if problem.isGoalState(next):
            return pathTo(next)

        addSuccesorsToFringe(next, cost)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
lcf = lowestCostFirst
astar = aStarSearch
