import pprint
import random
chessBoard = [[0 for j in range(8)] for i in range(8)]
chessBoard[0][0] = "R"
pprint.pprint(chessBoard)

#rook
def mRook():
    x = 0
    y = 0
    getPos = [][]
    chessBoard[0][0] = 0
    if int(random.uniform(0, 1)) == 1:
        x = int(random.random(0.0, 8.0))
    else:
        y = int(random.random(0.0, 8.0))
    newPosition = (x,y)
    chessBoard[x][y] = "R"
    pprint.pprint(chessBoard)
    
#bishop
def mBishop:
	x = 0
	y = 0
	getPos = [x][y]
	
	
def validMoves(x, y, piece):
	validSpace = []
	if piece == rook:
		for a in range(x):
			validSpace.append(str(a) + str(y))
		for b in range(y):
			validSpace.append(str(x) + str(b))
	
	elif piece == bishop:
		for a in range(7):
			if x + a <= 7 and y + a <= 7:
				validSpace.append(str(x + a) + str(y + a))
			
			if x - a >= 0 and y - a >= 0:
				validSpace.append(str(x - a) + str(y - a))
					
			if x - a >= 0 and y + a <= 7:
				validSpace.append(str(x - a) + str(y + a))
					
			if x + a <= 7 and y - a >= 0:
				validSpace.append(str(x + a) + str(y + a))
	
	elif piece == knight:
		if x + 2 <= 7:
			if y + 1 <= 7:
				validSpace.append(str(x + 2) + str(y + 1))
			if y - 1 >= 0:
				validSpace.append(str(x + 2) + str(y - 1))
		
		if x - 2 >= 0:
			if y + 1 <= 7:
				validSpace.append(str(x - 2) + str(y + 1))
			if y - 1 >= 0:
				validSpace.append(str(x - 2) + str(y - 1))
				
		if y + 2 <= 7:
			if x + 1 <= 7:
				validSpace.append(str(x + 1) + str(y + 2))
			if x - 1 >= 0:
				validSpace.append(str(x - 1) + str(y + 2))
				
		if y - 2 >= 0:
			if x + 1 <= 7:
				validSpace.append(str(x + 1) + str(y - 2))
			if x - 1 >= 0:
				validSpace.append(str(x - 1) + str(y - 2))
	
	elif piece == queen:
		for a in range(x):
			validSpace.append(str(a) + str(y))
			if x + a <= 7 and y + a <= 7:
				validSpace.append(str(x + a) + str(y + a))
			
			if x - a >= 0 and y - a >= 0:
				validSpace.append(str(x - a) + str(y - a))
					
			if x - a >= 0 and y + a <= 7:
				validSpace.append(str(x - a) + str(y + a))
					
			if x + a <= 7 and y - a >= 0:
				validSpace.append(str(x + a) + str(y + a))
		for b in range(y):
			validSpace.append(str(x) + str(b))
	
	elif piece == king:
		asdf
	
	elif piece == pawn:
		asdf
