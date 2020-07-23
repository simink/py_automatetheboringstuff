## chapter 5 - dictionaries
# keys, values, items

spam = {'colour': 'red', 'age':40}
for k, v in spam.items():
    print(' Key ' + k + ' Value ' + str(v))


## using get() method
picnicItems = {'apples': 5, 'cups': 2}

print('i am bringing ' + str(picnicItems.get('apples', 0)) + ' apples')
print('i am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs')


## setdefault() method
spam.setdefault('name', 'Pooka')
print(spam)