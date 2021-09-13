import random
from game import Agent
from game import Directions


class DumbAgent(Agent):
    "an agent that goes west until it can't"

    def getAction(self, state):
        "the agent receives a GameState(defined in pacman.py)"
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        print("Agents available: ", state.getNumAgents())
        print("the number of capsules available: ", state.getCapsules())
        print("the walls: ", state.getWalls())

        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST

        else:
            print("Stopping.")
            return Directions.STOP


    "a random agent that moves in a random direction as long as there are no walls"
class RandomAgent(Agent):

     def getAction(self, state):
        #remove stop 
        legalmoves = [i for i in state.getLegalPacmanActions() if i is not 'Stop']
        #legalmoves = state.getLegalPacmanActions()
        print(legalmoves)
        return random.choice(legalmoves)


class ReflexAgent(Agent):

    def getAction(self, state):
        'To Do'
        


