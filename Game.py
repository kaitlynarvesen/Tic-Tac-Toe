import random

#print a board with correct format
def disp(w, board):
	for row in board:
		for elem in row:
			w.write(elem+' ')
		w.write('\n')
	w.write('\n')

#check if user input for row is valid (int 1-3)
def input_check_row(i):
	try:
		n=int(i)
	except:
		n=0 #invalid
	if n==1 or n==2 or n==3:
		return n
	else:
		print('Invalid input.')
		return input_check_row(input('Row: '))

#check if user input for column is valid (int 1-3)
def input_check_col(i):
	try:
		n=int(i)
	except:
		n=0 #invalid
	if n==1 or n==2 or n==3:
		return n
	else:
		print('Invalid input.')
		return input_check_col(input('Column: '))

#check if user input for column is valid (int 1-3)
def input_check_skill(i):
	try:
		n=int(i)
	except:
		n=0 #invalid
	if n==1 or n==2 or n==3:
		return n
	else:
		print('Invalid input.')
		return input_check_skill(input('Choose computer skill level (1-3): '))

#check if a spot is taken or not
def spot_check(board, row, col):
	if board[row-1][col-1]=='_':
		return True #not taken
	else:
		return False

#check if the board is in a winning configuration
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

#option to play again or exit
def end(w):
	again=input('\nPlay again? (Y/N): ')
	if again=='Y' or again=='y' or again=='Yes' or again=='yes':
		solve(w)
	else:
		exit()

#returns a list of tuples (row, col) of all the free spots on the board
def free_spaces(board):
	ans=[]
	for r in range(1, 4):
		for c in range(1, 4):
			if spot_check(board, r, c):
				ans.append((r-1, c-1))
	return ans

#executes minimax algorithm to find the best move
def minimax(board, computer_turn):
	free=free_spaces(board)

	#if game over
	if win(board, 'O'):
		return 1
	if win(board, 'X'):
		return -1
	if len(free)<1:
		return 0

	if computer_turn:
		best=-1000
		for f in free:
			board2=[row.copy() for row in board]
			board2[f[0]][f[1]]='O'
			val=minimax(board2, False)
			best=max(best, val)
		return best

	else:
		best=1000
		for f in free:
			board2=[row.copy() for row in board]
			board2[f[0]][f[1]]='X'
			val=minimax(board2, True)
			best=min(best, val)
		return best

#finds the computer the best move using the minimax function
def findBestMove(board):
	best=-1000
	free=free_spaces(board)
	move=None

	for f in free:
		board2=[row.copy() for row in board]
		board2[f[0]][f[1]]='O'
		if minimax(board2, False)>best:
			best=minimax(board2, False)
			move=f
	return move

#player turn
def player_move(w, board):
	print('--Your move--')
	turn=0
	while turn==0:
		row=input_check_row(input('Row: '))
		col=input_check_col(input('Column: '))
		if spot_check(board, row, col): #if spot not taken
			board[row-1][col-1]='X'
			turn=1
		else:
			print("Spot taken.")
	#check for win
	if win(board, 'X'):
		disp(w, board)
		print('You win!')
		end(w)
	return board

#computer turn: skill level 1 (random)
def computer_move_1(w, board):
	print('--Computer move--')
	turn=0
	while turn==0:
		row=random.randint(1, 3)
		col=random.randint(1, 3)
		if spot_check(board, row, col): #if spot not taken
			board[row-1][col-1]='O'
			turn=1
	#check for win
	if win(board, 'O'):
		disp(w, board)
		print('Computer wins.')
		end(w)
	return board

#computer turn: skill level 2
#if computer can win on next turn: go there
#if player can win on next turn: block them
#otherwise: random
def computer_move_2(w, board):
	free=free_spaces(board)

	#if computer can win on this turn
	for f in free:
		board2=[row.copy() for row in board]
		board2[f[0]][f[1]]='O'
		if win(board2, 'O'):
			print('--Computer move--')
			disp(w, board2)
			print('Computer wins.')
			end(w)
	#if player can win on next turn
	for f in free:
		board2=[row.copy() for row in board]
		board2[f[0]][f[1]]='X'
		if win(board2, 'X'):
			print('--Computer move--')
			board[f[0]][f[1]]='O'
			return board
	#otherwise: random
	computer_move_1(w, board)

#computer turn: skill level 3
#uses minimax algorithm to find best possible move
#calculates all remaining possibilities and assumes player uses best moves
def computer_move_3(w, board):
	print('--Computer move--')

	board2=[row.copy() for row in board]
	move=findBestMove(board2)
	print(move)

	row=move[0]
	col=move[1]
	board[row][col]='O'
	#check for win
	if win(board, 'O'):
		disp(w, board)
		print('Computer wins.')
		end(w)
	return board

#check if the input for the first move guess is valid (int 1-100)
def first_check(i):
	try:
		n=int(i)
	except:
		n=-1 #invalid
	if n>0 and n<101:
		return n
	else:
		print('Invalid input.')
		return first_check(input('Choose a number from 1-100 (inclusive): '))

#plays the game
def solve(w):
	#initialize board
	board=[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

	#set computer skill level
	skill=input_check_skill(input('Choose computer skill level (1-3): '))

	#determine if player or computer goes first by guessing a number from 1-100
	#whoever is closer to a random number from 1-100 goes first
	ans=random.randint(1, 100)
	player=first_check(input('\nChoose a number from 1-100 (inclusive): '))
	computer=random.randint(1, 100)
	print('\nAnswer: '+str(ans)+', Player Guess: '+str(player)+', Computer Guess: '+str(computer))
	if abs(ans-player)==abs(ans-computer):
		print('Tie!')
		solve()
	if abs(ans-player)<abs(ans-computer):
		print('You go first!\n')
		solve_player(w, board, skill)
	else:
		print('Computer goes first.\n')
		solve_computer(w, board, skill)

#used if player goes first
def solve_player(w, board, skill):
	disp(w, board)

	player_move(w, board)
	disp(w, board)

	#play until someone wins or the board is full
	count=0
	while count<4:
		if skill==1:
			computer_move_1(w, board)
		if skill==2:
			computer_move_2(w, board)
		if skill==3:
			computer_move_3(w, board)
		disp(w, board)

		player_move(w, board)
		disp(w, board)

		count+=1
	print('Tie!')
	end(w)

#used if computer goes first
def solve_computer(w, board, skill):
	if skill==1:
		computer_move_1(w, board)
	if skill==2:
		computer_move_2(w, board)
	if skill==3:
		computer_move_3(w, board)
	disp(w, board)

	#play until someone wins or the board is full
	count=0
	while count<4:
		player_move(w, board)
		disp(w, board)

		if skill==1:
			computer_move_1(w, board)
		if skill==2:
			computer_move_2(w, board)
		if skill ==3:
			computer_move_3(w, board)
		disp(w, board)

		count+=1
	print('Tie!')
	end(w)
