#! python3
# simple countdown script

import time, subprocess

# countdown
timeLeft = 20
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

# play sound
subprocess.Popen(['start', './docs/alarm.wav'], shell=True)
