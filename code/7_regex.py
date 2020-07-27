## chpt 7 - regular expressions

import re

# sub method with group
agentNamesRegex = re.compile(r'Agent (\w)\w*(\w)')
agentNamesRegex.sub(r'\1***\2', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

# Q20. match numbers with commas

numList = ['42', '1,234', '6,367,453', '12,34,234', '3215', '1,123,23']
numRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
for i in numList:
    txt = numRegex.search(i)
    if txt != None:
        print(txt.group())
    else:
        print('not found')


# Q21. match names

names = ['Haruto Watanabe', 'RoboCop Watanabe''haru Watanabe', 'Mr. Watanabe', 'Watanabe', 'Haru watanabe']

nameRegex = re.compile(r'[A-Z][a-zA-Z]*\sWatanabe')
for i in names:
    txt = nameRegex.search(i)
    if txt != None:
        print(txt.group())
    else:
        print('Not matched')

# Q22 - phrases

ph = ['Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.', 'Alice throws Apples.', 'BOB EATS CATS.', 'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.']

phRegex = re.compile(r'(alice|bob|carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)
for i in ph:
    txt = phRegex.search(i)
    if txt != None:
        print(txt.group())
    else:
        print('Not matched')






