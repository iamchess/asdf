import pprint
import random
chessBoard = [[0 for j in range(8)] for i in range(8)]
chessBoard[0][0] = "R"
pprint.pprint(chessBoard)

#rook
def move():
    x = 0
    y = 0
    getPosition = [0,0]
    chessBoard[0][0] = 0
    if random.uniform(0, 2) < 1:
        x = int(random.uniform(0, 7))
    else:
        y = int(random.uniform(0, 7))
    newPosition = (x,y)
    chessBoard[x][y] = "R"
    pprint.pprint(chessBoard)
    
move()
