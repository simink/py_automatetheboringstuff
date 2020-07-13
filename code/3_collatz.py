### collatz sequence

## define collatz function
def collatz():

    global num

    if num % 2 == 0:
        num = num // 2
        print(num)
    else:
        num = 3 * num + 1
        print(num)


## capture input
num = input('enter number >  ')

## check that input is a number
try:
    num = int(num)
    while True:
        collatz()
        if num == 1:
            break
except:
    print('input must be an integer')











