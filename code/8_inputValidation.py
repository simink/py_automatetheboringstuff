import pyinputplus as pyip
# response = pyip.inputNum()

## enter a series of digits that add up to ten

def addsUpToTen(num):
    numList = list(num)
    for i, digit in enumerate(numList):
        numList[i] = int(digit)

    if sum(numList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numList)))

    return int(num)

response = pyip.inputCustom(addsUpToTen)