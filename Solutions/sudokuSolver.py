
board = [
		  [0, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ]



def convertToBoard(string):
	''' 
Give the 9 lines of each containing 9 chars(str) representing the corrosponding values 
e.g 
200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003
'''
	board = []

	lines = string.split('\n')
	for line in lines:
		temp = []
		for char in line:
			temp.append(int(char))
		board.append(temp)

	return board



def emptyPos(board):
	''' The the index of next empty place '''

	for row in range(9):
		for col in range(9):
			if board[row][col] == 0:
				return (row, col)

	return 0 # The board is solved


def print_(board):
	for i in board:
		print(i)



def valid(board, number, pos):

	# Check horizontally 
	row, col = pos
	for index in range(9):
		if board[row][index] == number:
			# print(board[row][index])
			return 0
		
	
		# Check Vertically 
		if board[index][col] == number:
			return 0


		# Check Boxes 
		boxStart = (row//3)*3, (col//3)*3
		boxEnd = boxStart[0] + 2, boxStart[1]+ 2
		
		for i in range(boxStart[0], boxEnd[0]+1):
			for j in range(boxStart[1], boxEnd[1]+1):
				if board[i][j] == number:
					return 0

	return 1



def solve(board : list):
	''' Returns Boards with valid replaced numbers from 0 '''

	if not emptyPos(board):
		print_(board)
		return True
	else:
		e_x, e_y = emptyPos(board)

	for number in range(1, 10):
		if valid(board, number, (e_x, e_y)):
			board[e_x][e_y] = number

			if solve(board):
				return True

			board[e_x][e_y] = 0


if __name__ == '__main__':
	# board = convertToBoard(string)
	ans = solve(board)
	if ans is None:
		print("The board is not valid")
