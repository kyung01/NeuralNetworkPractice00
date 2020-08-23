#PYTHON MAIN FUNCTION is a starting point of any program. When the program is run, the python interpreter runs the code sequentially. Main function is executed only when it is run as a Python program. It will not run the main function if it imported as a module.

def main():
	gameBegin()


def printBoard(b):
	data = [
		[b[0],b[1],b[2]],
		[b[3],b[4],b[5]],
		[b[6],b[7],b[8]]
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

def gameBegin():
	global board
	for turn in range(0,9):
		print("Current Player is " + currentPlayer)
		print("Type 1~9 (starting from top left to bottom right)")
		printBoard(board)
		move = input()
		board[int(move)-1] = currentPlayer

		print("Move was "+ move)
		#check if there is a winner
		#if there is no winnter then switch the player
		switchPlayer()
		print("...")




board = [None] * 9
X = 'X'
O = 'O'
currentPlayer = X;

if __name__ == "__main__":
	main()

print("just a print function")