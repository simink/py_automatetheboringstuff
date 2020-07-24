## prints the words from a table right justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


# create list of colWidths to identify the longest string in each column
colWidths = [0] * len(tableData)

# identify the longest string in each column
for i in range(len(tableData)):
    for item in tableData[i]:
        if len(item) > colWidths[i]:
            colWidths[i] = len(item)

# print right justified table
for x in range(len(tableData[0])):
    for y in range(len(tableData)):
        print(tableData[y][x].rjust(colWidths[y]+2, ' '), end = '')
    print('\n')

        