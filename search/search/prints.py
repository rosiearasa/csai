from game import Agent
from game import AgentState
from game import Directions


import util
from pacman import GameState


"""node class definition"""
class Node:
    def __init__(self, state, parent_node, action,step_cost, path_cost):
        self.state =state
        self.parent = parent_node
        self.action = action
        self.step_cost =step_cost
        self.path_cost= path_cost




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
