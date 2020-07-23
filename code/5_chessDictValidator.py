## function to validate the pieces and chess board space
import string

# create list of valid spaces
validSpace = []
for x in range(8):
    for y in range(8):
        validSpace.append(str(x+1)+str(string.ascii_lowercase[y]))

# create list of valid pieces
validPieces = {'pawn': 8, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1, 'king': 1}

# create function to number of pieces
def checkPieces(inputList, validList):
    count = {}
    result = True

    for i in inputList:
        count.setdefault(i, 0)
        count[i] = count[i] + 1
    
    for k,v in count.items():
        if v > validList[k]:
            result = False
            break

    return result

# create function to check validity of chess board
def isValidChessBoard(input):

    # x is a dictionary and should return true or false
    result = True

    # check the number of chess pieces ------------------

    # check black or white and split
    tmp = list(input.values())
    black = []
    white = []
    
    for i in tmp:
        if i[0] == 'b':
            black.append(i[1:])
        elif i[0] == 'w':
            white.append(i[1:])
        else:
            result = False
            break

    # check if count of pieces valid
    if checkPieces(black, validPieces) == False:
        result = False

    if checkPieces(white, validPieces) == False:
        result = False

    # check for valid space --------------------------
    for z in list(input.keys()):
        if (z in validSpace) == False:
            result = False
            break

    return result
    

# test
chessMoves = {'1h': 'bking', '8c': 'bpawn', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(chessMoves))

