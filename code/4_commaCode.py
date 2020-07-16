## returns string with each item separated by a comma except for the last one

def comma_code(x):
    # check for empty list
    if not x:
        print("list is empty")
    elif len(x) == 1:
        print(x[0])
    else:
        print(', '.join(x[:-1]), end='')
        print(' and '+ spam[-1])


spam = ['apples', 'bananas', 'orange']
comma_code(spam)
spam = ['apples', 'bananas']
comma_code(spam)
spam = ['apples']
comma_code(spam)
spam = []
comma_code(spam)