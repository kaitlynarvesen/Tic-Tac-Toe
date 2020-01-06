import random

def disp(w, board):
	for row in board:
		for elem in row:
			w.write(elem+' ')
		w.write('\n')
	w.write('\n')

def input_check(i):
	flag=0 #okay
	n=0
	try:
		n=int(i)
	except:
		flag=1 #can't convert to int
	if n<1 or n>3:
		flag=1 #out of range
	if flag==0:
		return n
	else:
		print('Invalid input.')
		return input_check(input('Row: '))

def spot_check(board, row, col):
	if board[row-1][col-1]=='_':
		return True #not taken
	else:
		return False


def player_move(board):
	print('--Your move--')
	turn=0
	while turn==0:
		row=input_check(input('Row: '))
		col=input_check(input('Column: '))
		if spot_check(board, row, col): #if spot not taken
			board[row-1][col-1]='X'
			turn=1
		else:
			print("Spot taken.")
	return board

def computer_move(board):
	print('--Computer move--')
	turn=0
	while turn==0:
		row=random.randint(1, 3)
		col=random.randint(1, 3)
		if spot_check(board, row, col): #if spot not taken
			board[row-1][col-1]='O'
			turn=1
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

	player_move(board)
	disp(w, board)

	#while win==0:
		#player moves


		#display


		#computer moves


		#display

