## guess the number game

import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# ask the player to guess 6 times
for guessesTaken in range(1,7):
    print("Make a guess")
    guess = int(input('>  '))

    if guess < secretNumber:
        print('too low')
    elif guess > secretNumber:
        print('too high')
    else:
        break  # correct guess

if guess == secretNumber:
    print(f'Good job. You guessed it in {guessesTaken} tries.')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}')