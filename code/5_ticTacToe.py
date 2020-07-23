## tictactoe

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
# 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# start with X
turn = 'x'

# 9 turns in all
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move to which space?')
    move = input('> ')
    theBoard[move] = turn

    # change turn
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
        
    printBoard(theBoard)