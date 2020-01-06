import random

def disp(w, board):
	for row in board:
		for elem in row:
			w.write(elem+' ')
		w.write('\n')
	w.write('\n')

def player_move(board):
	print('--Your move--')
	row=int(input('Row: ')) #add check that it's an int 1-3
	col=int(input('Column: '))
	board[row-1][col-1]='X' #add check that spot isn't already taken
	return board

def computer_move(board):
	print('--Computer move--')
	row=random.randint(1, 3)
	col=random.randint(1, 3)
	board[row-1][col-1]='O'
	return board


def solve(r, w):
	#initialize board
	board=[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
	#display
	disp(w, board)
	win=0

	player_move(board)
	disp(w, board)

	computer_move(board)
	disp(w, board)

	#while win==0:
		#player moves


		#display


		#computer moves


		#display

