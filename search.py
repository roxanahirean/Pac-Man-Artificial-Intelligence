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
import random

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

def randomSearch(problem):
    state = problem.getStartState()
    actions = []
    while not problem.isGoalState(state):
        successors = problem.getSuccessors(state)
        successor = successors[random.randint(0, len(successors)-1)]
        state = successor[0]
        actions.append(successor[1])
    return actions


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    """print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"

    stack = util.Stack()
    visited = []
    start = problem.getStartState()
    stack.push((start, []))
    visited.append(start)
    while not stack.isEmpty():
        currentState, currentAction = stack.pop()
        if problem.isGoalState(currentState):
            return currentAction
        successor = problem.getSuccessors(currentState)
        visited.append(currentState)
        for s in successor:
            coordinates = s[0]
            if coordinates not in visited:
                currentDirection = s[1]
                stack.push((coordinates, currentAction + [currentDirection]))
    return currentAction
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    explored = []
    explored.append(start)
    states = util.Queue()
    stateTuple = (start, [])
    states.push(stateTuple)
    while not states.isEmpty():
        currentN = states.pop()
        currentS = currentN[0]
        path = currentN[1]
        if problem.isGoalState(currentS):
            return path
        successor = problem.getSuccessors(currentS)
        for i in successor:
            coordinates = i[0]
            if not coordinates in explored:
                direction = i[1]
                explored.append(coordinates)
                states.push((coordinates, path + [direction]))

    return []


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"


    start = problem.getStartState()
    exploredState = []
    states = util.PriorityQueue()
    states.push((start, []), 0)
    while not states.isEmpty():
        state, actions = states.pop()
        if problem.isGoalState(state):
            return actions
        if state not in exploredState:
            successors = problem.getSuccessors(state)
            for succ in successors:
                coordinates = succ[0]
                if coordinates not in exploredState:
                    directions = succ[1]
                    newCost = actions + [directions]
                    states.push((coordinates, actions + [directions]), problem.getCostOfActions(newCost))
        exploredState.append(state)
    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue

    list = PriorityQueue()
    visited_list = []
    path = []
    priority = 0

    """start position"""
    state = problem.getStartState()

    list.push((state, path), priority)

    while not list.isEmpty():
        current_node = list.pop()
        position = current_node[0]
        path = current_node[1]

        if problem.isGoalState(position):
            return path

        if position not in visited_list:
            visited_list.append(position)

            successors = problem.getSuccessors(position)

            for item in successors:
                if item[0] not in visited_list:
                    new_pos = item[0]
                    new_path = path + [item[1]]

                    g = problem.getCostOfActions(new_path)
                    h = heuristic(new_pos, problem)
                    i = g + h
                    new_priority = i
                    list.push((new_pos, new_path), new_priority)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
