import pickle
from random import randrange

#PYTHON MAIN FUNCTION is a starting point of any program. When the program is run, the python interpreter runs the code sequentially. Main function is executed only when it is run as a Python program. It will not run the main function if it imported as a module.
from TicTacToeGame import TicTacToeGame

#3 cell state x 9 cells  x 2 starting cases
MAX_QTABLE_COUNT = pow(3,9)*2

isPrint = False
validGameCount = 0
invalidGameCount = 0
WonCount = 0
TieCount = 0


class Human:
	def __init__(self):
		self.table = [None] * MAX_QTABLE_COUNT
		self.history = []

		for i in range(0,MAX_QTABLE_COUNT):
			self.table[i] = self.newQTableNode()


	def newQTableNode(self):
		node = [0.0] * 9
		return node

	def getBestQTableNodeChoice(self,qtableNode):
		currentBestChoice = -1.0
		currentBestChoiceValue = 0.0
		for i in range(0,9):
			if qtableNode[i] > currentBestChoiceValue:
				if(isPrint):("found an option" + str(qtableNode[i]))

				currentBestChoice = i
				currentBestChoiceValue = qtableNode[i]
			else:
				if(isPrint):("QTable was ineaduqate " + str(qtableNode[i]))
		if(isPrint):
			print("QTable of value " + str(currentBestChoiceValue) + " choice " + str(currentBestChoice))
		return currentBestChoice

	def print(self):
		data = [None] * MAX_QTABLE_COUNT

		for i in range(0,MAX_QTABLE_COUNT):
			row = self.table[i]
			data[i] = [None]*10
			data[i][0] = str(1+i)
			for j in range(0,9):
				data[i][1+j] =str( row[j])

		for row in data:
			print("{:>3} {: >5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format(*row))
		#	return

			

	def getMove(self, game : TicTacToeGame):
		#self.print()
		tableID = game.getBoardID(game.board,game.currentPlayer)
		#print("Table ID " + str(tableID))
		currentTable = self.table[tableID]
		bestChoice = int(input())
		if bestChoice == -1:
			if(isPrint):print("Agent facing dead end choice")
			bestChoice = randrange(9)

		moveMade = [ game.getBoardID(game.board,game.currentPlayer), bestChoice-1]
		self.history.append(moveMade)
		return bestChoice  #because move of the game has to be 1~9

	def updateQTable(self,history, agentScore): 
		if(isPrint):print('History Length '+str(len(history)))

		for i in range(len(history)-1,-1,-1):
			self.table[history[i][0]][history[i][1]] += agentScore
			agentScore *= 0.9
			#print(i)
		self.refreshQtable()



	def updateQTableLight(self,history, agentScore): 
		if(isPrint):print('History Length '+str(len(history)))
		self.table[history[len(history)-1][0]][history[len(history)-1][1]] += agentScore

		self.refreshQtable()

	def refreshQTable(self):
		print("REFRESH")
		maxTableValue = 1

		for i in range(0, MAX_QTABLE_COUNT):
			for j in range(0,9):
				if abs(self.table[i][j]) > maxTableValue:
					maxTableValue = abs(self.table[i][j])

		for i in range(0, MAX_QTABLE_COUNT):
			for j in range(0,9):
				self.table[i][j] /= maxTableValue


	def save(self,fileName,score):
		if(isPrint):print("save")
		outfile = open(fileName,'wb')
		self.history = []
		pickle.dump(self,outfile)
		outfile.close()


class Agent:
	def __init__(self):
		self.table = [None] * MAX_QTABLE_COUNT
		self.history = []

		for i in range(0,MAX_QTABLE_COUNT):
			self.table[i] = self.newQTableNode()


	def newQTableNode(self):
		node = [0.0] * 9
		return node

	def getBestQTableNodeChoice(self,game,qtableNode):
		currentBestChoice = -1.0
		currentBestChoiceValue = -10
		for i in range(0,9):
			if(not game.isValidMove(i)):
				continue
			if qtableNode[i] > currentBestChoiceValue:
				currentBestChoice = i
				currentBestChoiceValue = qtableNode[i]
			else:
				if(isPrint):("QTable was ineaduqate " + str(qtableNode[i]))
		if(isPrint):
			print("QTable of value " + str(currentBestChoiceValue) + " choice " + str(currentBestChoice))
		return currentBestChoice

	def print(self):
		data = [None] * MAX_QTABLE_COUNT

		for i in range(0,MAX_QTABLE_COUNT):
			row = self.table[i]
			data[i] = [None]*10
			data[i][0] = str(1+i)
			for j in range(0,9):
				data[i][1+j] =str( row[j])

		for row in data:
			print("{:>3} {: >5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format(*row))
		#	return

			

	def getMove(self, game : TicTacToeGame):
		#self.print()
		tableID = game.getBoardID(game.board,game.currentPlayer)
		#print("Table ID " + str(tableID))
		currentTable = self.table[tableID]
		bestChoice = self.getBestQTableNodeChoice(game, currentTable)
		if bestChoice == -1:
			if(isPrint):print("Agent facing dead end choice")
			bestChoice = game.getRandomMove() -1

		moveMade = [ game.getBoardID(game.board,game.currentPlayer), bestChoice]
		self.history.append(moveMade)
		return bestChoice + 1 #because move of the game has to be 1~9

	def updateQTable(self,history, agentScore): 
		if(isPrint):print('History Length '+str(len(history)))

		influence = 0.5
		agnetScoreBefore = agentScore

		self.table[history[len(history)-1][0]][history[len(history)-1][1]] = agentScore
		for i in range(len(history)-2,-1,-1):
			self.table[history[i][0]][history[i][1]] = agnetScoreBefore * influence + self.table[history[i][0]][history[i][1]] * (1-influence)
			agnetScoreBefore = self.table[history[i][0]][history[i][1]]
			#agentScore *= 0.5
			#print(i)
		#self.refreshQTable()

	def updateQTableLight(self,history, agentScore): 
		if(isPrint):print('History Length '+str(len(history)))
		self.table[history[len(history)-1][0]][history[len(history)-1][1]] = agentScore
		#self.refreshQTable()

	def refreshQTable(self):
		if(isPrint):print("REFRESH")
		maxTableValue = 1

		for i in range(0, MAX_QTABLE_COUNT):
			for j in range(0,9):
				if abs(self.table[i][j]) > maxTableValue:
					maxTableValue = abs(self.table[i][j])

		for i in range(0, MAX_QTABLE_COUNT):
			for j in range(0,9):
				self.table[i][j] /= maxTableValue

	def save(self,fileName,score):
		if(isPrint):print("save")
		outfile = open(fileName,'wb')
		self.history = []
		pickle.dump(self,outfile)
		outfile.close()


		

def main1():
	loadFile = open(filename,'rb')
	agent = pickle.load(loadFile)
	loadFile.close()
	
	agent.print()
	return

def mainClear():
	agent = Agent()
	agent.save(filename,0)


filename = 'agent.txt'
def main0():
	global validGameCount
	global invalidGameCount
	global WonCount
	global TieCount
	loadFile = open(filename,'rb')
	agent = pickle.load(loadFile)
	loadFile.close()
	

	if True:
		#loadFile = open('agent','rb')
		#agentB = pickle.load(loadFile)
		#loadFile.close()
		agentB = None
	else:
		agentB = Human()

	#agent = Agent()
	
	#agent.print()
	#return

	agentIndex = None

	tttGame = TicTacToeGame()

	#tttGame.begin(None,None)
	#return
	if randrange(2) == 0:
		agentIndex = 'X'
	else:
		agentIndex = 'O'

	if(isPrint):print('Agent is ' + agentIndex)
	if agentIndex == 'X':
		tttGame.begin(agent,agentB)
	else:
		tttGame.begin(agentB,agent)
	agentScoreBase = 1
	agentScore = -agentScoreBase
	if(tttGame.wonPlayer == None):
		TieCount += 1
		validGameCount += 1
		Agent.updateQTableLight(agent,agent.history, agentScoreBase*0.5)
		agent.save(filename,agentScore)

		return
	if(tttGame.wonPlayer == agentIndex):
		if(isPrint):print("Agent won")
		agentScore = agentScoreBase

	else:
		if(isPrint):print("Agent lost")

	if(tttGame.isLegitGame ):
		validGameCount += 1
		#print("Legit game detected at " + str(validGameCount + invalidGameCount))

		if(agentScore>0):
			WonCount += 1
		Agent.updateQTable(agent,agent.history, agentScore)
		if(agentB != None):Agent.updateQTable(agent,agentB.history, -agentScore)

	elif(not tttGame.isLegitGame):
		invalidGameCount += 1

	agent.save(filename,agentScore)
	#agent.print()

if __name__ == "__main__":
	#mainClear()

	totalCount = 0

	gameCount = 100
	repeat = 70

	for r in range(0,repeat):
	#while True:
		invalidGameCount = 0
		validGameCount = 0 
		WonCount = 0
		TieCount = 0
		for i in range(0,gameCount):
			main0()
			totalCount+=1
		print()
		print("Total " + str(totalCount))
		print("Invalid Game Count " + str(invalidGameCount))
		print("Valid Game Count " + str(validGameCount))
		print("Won Game Count " + str(WonCount))
		print("Tie Game Count " + str(TieCount))
		#if(invalidGameCount == 0 or (WonCount + TieCount) == validGameCount): break

