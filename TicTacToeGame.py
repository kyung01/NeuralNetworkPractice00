
from random import randrange
#Enums
X = 'X'
O = 'O'
class TicTacToeGame:
	def __init__(self):
		self.isPrint = False
		self.board = [None] * 9
		self.currentPlayer = X;
		self.wonPlayer = None
		self.isLegitGame = True

	def print(self):
		self.printBoard(self.board)

	def printBoard(self,b):
		data = [
			[str(b[0]),str(b[1]),str(b[2])],
			[str(b[3]),str(b[4]),str(b[5])],
			[str(b[6]),str(b[7]),str(b[8])]
		]
		for row in data:
			print("{:>20} {: >20} {:>20}".format(*row))

	def switchPlayer(self):
		if self.currentPlayer == X:
			self.currentPlayer = O
		elif self.currentPlayer == O:
			self.currentPlayer = X
		else :
			self.currentPlayer = " "

	def checkIfPlayerWon(self,board, player):
		if ((player == board[0] == board[1] == board[2]) or
			(player == board[3] == board[4] == board[5]) or
			(player == board[6] == board[7] == board[8])):
			if(self.isPrint):print("Horizontal victory")
			return True



		if	((player == board[0] == board[3] == board[6]) or
			(player == board[1] == board[4] == board[7]) or
			(player == board[2] == board[5] == board[8])):
			if(self.isPrint):print("Vertical Victory")
			return True

		if	((player == board[0] == board[4] == board[8]) or 
			(player == board[2] == board[4] == board[6])):
			if(self.isPrint):print("Diagonal Victory")
			return True
		return False		

	def isLegalMove(self,board, player, input):
		if input < 0 or input >= 9:
			return False
		if(board[input] != None):
			return False
		return True

	def getMove(self):
		return int(input())

	def printGameOver(self):
		print("Player " + str(self.wonPlayer) + " has won")
		self.printBoard(self.board)

	def isValidMove(self, move):
		return self.board[move] == None

	def getRandomMove(self):
		unselectedSlots = []
		for i in range(0,9):
			if self.board[i] == None :
				unselectedSlots.append(i)
		return 1+unselectedSlots[randrange(len(unselectedSlots))]

	#move has to be 1~9
	def getMoveFrom(self, player):
		if(player == None):
			#return int(input())
			return self.getRandomMove()
		return player.getMove(self)

	def begin(self,playerX,playerO):

		for turn in range(0,9):
			if(self.isPrint):
				print("Current Player is " + self.currentPlayer)
				print("Type 1~9 (starting from top left to bottom right)")
				self.printBoard(self.board)
			if(self.currentPlayer == X):
				move = self.getMoveFrom(playerX)
			else:
				move = self.getMoveFrom(playerO)
			if(self.isPrint): print("Selected Move : " + str(move) )
			move -= 1
			if not self.isLegalMove(self.board,self.currentPlayer, move):
				#Current player made a mistake
				#The other player wins automatically 
				if(self.isPrint): print("Current player made a mistake")
				self.switchPlayer()
				self.wonPlayer = self.currentPlayer
				self.isLegitGame = False
				if(self.isPrint): self.printGameOver()
				return

			self.board[move] = self.currentPlayer

			#check if there is a winner
			if self.checkIfPlayerWon(self.board,self.currentPlayer):
				self.wonPlayer = self.currentPlayer
				if(self.isPrint): self.printGameOver()
				return
			#if there is no winnter then switch the player
			self.switchPlayer()
			if(self.isPrint): print("...")
		if(self.isPrint):
			self.printBoard(self.board)
			print("Tie")

	#board related functions
	def getBoardID(self,board, currentPlayer):
		boardID = 0
		if currentPlayer == O:
			boardID += 27
		for i in range(0,9):
			cellID = 0
			if board[i] == X: 
				cellID = 1
			elif(board[i] == O): 
				cellID = 2
			boardID += pow(3,i) * cellID;
		return boardID




	

	