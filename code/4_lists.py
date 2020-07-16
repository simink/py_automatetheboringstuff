## testing lists

# unpacking
cat = ['fat', 'loud', 'gray']
size, disposition, colour = cat
print(size)
print(colour)
print('-'*40)

# enumerate returns index and item in list
for index, item in enumerate(cat):
    print(f'index {index} gives you item {item}')

## randon choices and shuffle
import random

print('random choice:' + random.choice(cat))
random.shuffle(cat)


# methods are like a function except it is "called on" a value.
# index method
print(cat.index('gray'))

# append and insert are list methods
# (modify in place as the return value of these is None)
cat.append('female')
print(cat)

cat.insert(3, 2)
print(cat)

# other methods - remove, sort
spam = ['a','z','A','Z']
spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)


## Parsing references - need to take note of this
def eggs(x):
    x.append('hello')

spam = [1,2,3]
print(id(spam))
eggs(spam)
print(spam)
print(id(spam)) # refer to the same id



