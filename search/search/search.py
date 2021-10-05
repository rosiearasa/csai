from game import Agent
from game import AgentState
from game import Directions


import util
from pacman import GameState



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
class Node:
    def __init__(self, curr_state,parent_node,action, step_cost,total_path_cost) -> None:

        self.curr_state = curr_state
        self.parent_node =parent_node
        self.action =action
        self.step_cost =step_cost
        self.total_path_cost = total_path_cost




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




"""node class definition"""
class Node:
    def __init__(self, state, parent_node, action,step_cost, path_cost):
        self.state =state
        self.parent = parent_node
        self.action = action
        self.step_cost =step_cost
        self.path_cost= path_cost



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


    #uses the LIFO stack defined
    frontier = util.Stack()

    explored = []

    #first node
    startState = problem.getStartState()

    startNode = (startState, [])




    frontier.push(startNode)


    #check if not empty
    while frontier:

        #a node with actions
        currentState, actions = frontier.pop()


        if currentState not in explored:

            #mark as expored
            explored.append(currentState)

            if problem.isGoalState(currentState):
                #return a list of actios from the start state ti the goal state
                return actions

            else:
                #for each successor of the goal state
                successors = problem.getSuccessors(currentState)

                #if not in explored add node of the successor onto the frontier
                for successorState, successorAction, successorCost in successors:
                    newAction = actions + [successorAction]
                    newNode = (successorState, newAction)
                    frontier.push(newNode)
    return actions

def breadthFirstSearch(problem):
    # initialize the FIFO queue
    frontier =util.Queue()

    #initialize explored
    explored = []

    startState = problem.getStartState()
    startNode = (startState, [], 0) #state action and cost

    frontier.push(startNode)

    while frontier:

        currentState, actions, currentCost = frontier.pop()

        if currentState not in explored:
            #put state into the node
            explored.append(currentState)

            if problem.isGoalState(currentState):
                return actions

            else:
                successors = problem.getSuccessors(currentState)

                for successorState, successorAction, successorCost in successors:
                    newAction = actions + [successorAction]
                    newCost = currentCost+successorCost
                    newNode =(successorState, newAction, newCost)

                    frontier.push(newNode)

    return actions



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
