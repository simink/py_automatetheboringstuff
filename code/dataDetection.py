## detect valid dates

import re, copy

dt = 'there are a few dates here 31/12/2020, 29/02/2020, 31/06/2020 and finally 01/01/0999'

# detect dates in this format DD/MM/YYYY
dateFormat = re.compile(r'([012]\d|3[01])/(0\d|1[012])/([12]\d{3})')

dts = dateFormat.findall(dt)

# check validity of dates

# check if leap year
def isLeapYear(x):
    if (x % 400 == 0):
        return True
    elif ((x % 4 == 0) and (x % 100 != 0)):
        return True
    else:
        return False

# initialise list of dates
validList = [True] * len(dts)

for i in range(len(dts)):

    # unpack values
    (d, m, y) = dts[i]
    print(dts)
    d = int(d)
    m = int(m)
    y = int(y)

    if m in [4,6,9,11] and d > 30:
        validList[i] = False
    elif m == 2 and isLeapYear(y) == True and d > 29:
        validList[i] = False
    elif m == 2 and isLeapYear(y) != True and d > 28:
        validList[i] = False


result = ['/'.join(x) for x, y in zip(dts, validList) if y == True]
print(result)
