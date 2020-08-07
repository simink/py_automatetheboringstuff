#! python3
# simple stopwatch program

import time

### display program instructions
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

### track laptimes
try:
    while True:
        input()
        lapTime = round(time.time()-lastTime, 2)
        totalTime = round(time.time()-startTime, 2)
        print(f'Lap #{lapNum}: {totalTime} ({lapTime})', end='')
        lapNum += 1
        lastTime = time.time()  # reset laptime
except KeyboardInterrupt:
    # hand ctrl-c exception to keep its error messge from displaying
    print('\nDone.')