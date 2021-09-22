import random

from pacman import GameState
from game import Actions, Agent
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
        legalmoves = [i for i in state.getLegalPacmanActions() if i != 'Stop']

        print(legalmoves)
        return random.choice(legalmoves)


class ReflexAgent(Agent):

    def getAction(self, state):
        validmoves = [i for i in state.getLegalActions()if i != 'Stop']


        actions= random.choice(validmoves)

         # Choose one of actions
        nextgameState = state.generatePacmanSuccessor(actions)
        currfood = nextgameState.getFood()

        foodrem =currfood.count()

        # print("count of food ", foodrem)

        # print("current food state ", state.getPacmanState())
        nextmove = nextgameState.getPacmanState()

        # print("next ferr  ", nextmove)

        if nextgameState is nextmove and currfood[nextmove]=='T':
            # print("current food ", currfood)
            return nextgameState


        else:
            return random.choice(validmoves)
