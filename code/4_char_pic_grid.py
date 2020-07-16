## print the following grid as a picture

grid = [['1', '.', '.', '.', '.', '.'],
        ['2', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['8', 'O', 'O', '.', '.', '.'],
        ['9', '.', '.', '.', '.', '.']]

# reverse the list
grid.reverse()

# print
for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()
