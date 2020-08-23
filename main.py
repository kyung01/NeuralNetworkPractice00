#PYTHON MAIN FUNCTION is a starting point of any program. When the program is run, the python interpreter runs the code sequentially. Main function is executed only when it is run as a Python program. It will not run the main function if it imported as a module.

def main():
	gameBegin()


def printBoard(b):
	data = [
		[str(b[0]),str(b[1]),str(b[2])],
		[str(b[3]),str(b[4]),str(b[5])],
		[str(b[6]),str(b[7]),str(b[8])]
	]
	for row in data:
		print("{:>20} {: >20} {:>20}".format(*row))

def switchPlayer():
	global currentPlayer
	if currentPlayer == X:
		currentPlayer = O
	elif currentPlayer == O:
		currentPlayer = X
	else :
		currentPlayer = " "

def checkIfPlayerWon(board, player):
	if ((player == board[0] == board[1] == board[2]) or
		(player == board[3] == board[4] == board[5]) or
		(player == board[6] == board[7] == board[8]) or

		(player == board[0] == board[3] == board[6]) or
		(player == board[1] == board[4] == board[7]) or
		(player == board[2] == board[5] == board[8]) or

		(player == board[0] == board[4] == board[8]) or 
		(player == board[2] == board[4] == board[6])):
		return True
	return False		

def isLegalMove(board, player, input):
	if input < 0 or input >= 9:
		return False
	if(board[input-1] != None):
		return False
	return True

def getMove():
	return int(input())

def printGameOver():
	global board
	global wonPlayer

	print("Player " + wonPlayer + " has won")
	printBoard(board)

def gameBegin():
	global board
	global wonPlayer

	for turn in range(0,9):
		print("Current Player is " + currentPlayer)
		print("Type 1~9 (starting from top left to bottom right)")
		printBoard(board)
		move = getMove()
		if not isLegalMove(board,currentPlayer, move):
			#Current player made a mistake
			#The other player wins automatically 
			print("Current player made a mistake")
			switchPlayer()
			wonPlayer = currentPlayer
			printGameOver()
			return

		board[int(move)-1] = currentPlayer

		#check if there is a winner
		if checkIfPlayerWon(board,currentPlayer):
			wonPlayer = currentPlayer
			printGameOver()
			return
		#if there is no winnter then switch the player
		switchPlayer()
		print("...")




board = [None] * 9
X = 'X'
O = 'O'
currentPlayer = X;
wonPlayer = None

if __name__ == "__main__":
	main()

print("Program end")