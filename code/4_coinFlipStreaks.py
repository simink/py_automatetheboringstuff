## find out percentage of coin flip streaks of six in a row

import random
numStreaks = []
for numExp in range(10):
    # code that creates a list of 100 coin flips
    coin_flips = []
    for i in range(100):
        coin_flips.append(random.randint(0,1))

    # code that checks if there's a streak
    streak_sequence = []

    streak = 0
    for i in range(100):
        if i == 0:
            pass
        if coin_flips[i-1] == coin_flips[i]:
            streak += 1
        else:
            streak_sequence.append(streak)
            streak = 0

    # count number of exactly 6 in a row and add to the numStreaks list
    numStreaks.append(streak_sequence.count(6))

# print('Chance of streak: %s%%'% (numStreaks / 100))

print('number of exactly a streak of six happening in a 100 coin flips: %s%%' % (sum(numStreaks) / len(numStreaks)))