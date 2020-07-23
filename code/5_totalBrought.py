# count number of items brought in total

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

# create definition
def totalBrought(guests, product):
    numBrought = 0

    for k, v in guests.items():
        numBrought = numBrought + v.get(product, 0)
    
    return numBrought

print('number of things brought:')
print('Apples: ' + str(totalBrought(allGuests, 'apples')))
print('Cakes: ' + str(totalBrought(allGuests, 'cakes')))