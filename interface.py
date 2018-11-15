## Central Function to communicate between game state and decision making algorithms

import pydemic

# Function to define rewards
#	Could also define this as a class?
def rewards(action,param):
	
	# Go through possible actions and return reward
	if action is example:
		reward = 10
	elif action is example2:
		reward = 3*param
	else:
		reward = 0

	return reward

# Function to initialize Game
def main():
	game = Game(numPlayers,numEpidemics)
	game.game_setup

	# Facilitate decision making algorithm playing the game
	while game != lost:
	
		#Policy should contain a list of 4 actions (a single turn for the current player)
		#gameClass is the Game as defined in pydemic.py
		policy = decisionMakingAlgorithm(gameClass)

		for action in policy:

			#Execute the action
			do(action)

		#End the turn
		turn(end)

