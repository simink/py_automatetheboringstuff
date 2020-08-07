## chapter 17 - date time

import time
time.time()

### start end time difference
import time
def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

### string description of current time
thisMoment = time.time()
time.ctime(thisMoment)

### time sleep - pause program
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

### rounding numbers
round(time.time(),2)


### datetime module
import datetime
datetime.datetime.now()
dt = datetime.datetime.now()
dt.year, dt.month, dt.day

### convert unix epoch timestamp to datetime object
datetime.datetime.fromtimestamp(1)  ## time shown in GMT (+8hrs)
datetime.datetime.fromtimestamp(time.time())

# comparing time
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
newyears2020 > halloween2019

### time delta - duration
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
delta.total_seconds()
str(delta)


## arithmetic calculations
dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays


oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st
oct21st - aboutThirtyYears
oct21st - (2 * aboutThirtyYears)

### pausing till a specific date
import datetime, time
halloween2020 = datetime.datetime(2020, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2020:
    time.sleep(1)

### converting datetime objects into strings
oct21st.strftime('%Y/%m/%d %H:%M:%S')
oct21st.strftime('%I:%M %p')
oct21st.strftime("%B of '%y")

### converting strings to datetime
datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
datetime.datetime.strptime("October of '19", "%B of '%y")
datetime.datetime.strptime("November of '63", "%B of '%y")


### Multithreading

# passing arguments to thread target
import threading
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()


## launching other programs from python
import subprocess
paintProc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
paintProc.poll() == None
paintProc.wait()
paintProc.poll()

## opening notepad and file
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\Users\Al\\hello.txt'])