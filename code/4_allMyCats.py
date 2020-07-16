## using list to store names of cats

catNames = []

while True:
    print('enter the name of cat ' + str(len(catNames) + 1) + ' (press enter to stop)')
    name = input('> ')

    if name == '':
        break

    # add to list
    catNames = catNames + [name]

print('The cat names entered are: ')
for name in catNames:
    print(name + ' ')