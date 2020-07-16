## conway's game of life
# If a living square has two or three living neighbors, it continues to live on the next step. If a dead square has exactly three living neighbors, it comes alive on the next step. Every other square dies or remains dead on the next step.


# setup ----------------------------------------------------------------------
import random, time, copy
WIDTH = 6
HEIGHT = 6


# create a list of list for the cells -----------------------------------------
nextCells = []

# start with width (determines number of columns)
for x in range(WIDTH):
    # create column
    column = []

    # add living/dead cells to each row in a particular column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')  # add living cell
        else:
            column.append('_')  # add dead cell
    
    # append columns
    nextCells.append(column)

# main program loop -----------------------------------------------------------

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    # print currentCells on screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')  # print row wise
        print()  # print newline at end of row


    # calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighbouring coordinates
            # % mod operator to ensure values between 0 and width-1 or height-1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            # count number of living neighbours row wise starting from top left
            numNeighbours = 0

            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours += 1

            # set conway's rules
            if (currentCells[x][y] == '#') and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = '#'
            elif (currentCells[x][y] == '_') and (numNeighbours == 3):
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = '_'

    time.sleep(1)  # add pause to reduce flickering

            



        

        





