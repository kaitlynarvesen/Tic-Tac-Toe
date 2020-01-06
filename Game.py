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

def win(board, c):
	#rows
	if board[0][0]==c and board[0][1]==c and board[0][2]==c:
		return True
	if board[1][0]==c and board[1][1]==c and board[1][2]==c:
		return True
	if board[2][0]==c and board[2][1]==c and board[2][2]==c:
		return True
	#columns
	if board[0][0]==c and board[1][0]==c and board[2][0]==c:
		return True
	if board[0][1]==c and board[1][1]==c and board[2][1]==c:
		return True
	if board[0][2]==c and board[1][2]==c and board[2][2]==c:
		return True
	#diagonals
	if board[0][0]==c and board[1][1]==c and board[2][2]==c:
		return True
	if board[0][2]==c and board[1][1]==c and board[2][0]==c:
		return True
	return False


def player_move(w, board):
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
	if win(board, 'X'):
		disp(w, board)
		print('Player wins!')
		exit()
	return board

def computer_move(w, board):
	print('--Computer move--')
	turn=0
	while turn==0:
		row=random.randint(1, 3)
		col=random.randint(1, 3)
		if spot_check(board, row, col): #if spot not taken
			board[row-1][col-1]='O'
			turn=1
	if win(board, 'O'):
		disp(w, board)
		print('Computer wins!')
		exit()
	return board


def solve(r, w):
	#initialize board
	board=[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
	#display
	disp(w, board)
	
	while 1==1:
		player_move(w, board)
		disp(w, board)

		computer_move(w, board)
		disp(w, board)


