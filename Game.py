

def disp(w, board):
	for row in board:
		w.write(str(row)+'\n')

def solve(r, w):
	#initialize board
	board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	disp(w, board)