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
	
