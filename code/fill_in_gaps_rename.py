#! python3

"""
Program checks file sequence and renames the later files to fit the sequence.

Assumes that the number sequence starts from the smallest digit and not from 1.
"""

import os, re, copy, shutil
from pathlib import Path

### inputs
folder = Path.cwd() / 'docs/fill_in_gap_rename'
prefixname = 'spam'
fileext = 'txt'

# regex of numbers
rx = re.compile('(^\D+)(\d+)(.*)(\.{})$'.format(fileext))

### initialise filelist
fileList = []
numList = []
minNum = 0
maxNum = 0
digitLen = 0

### identify files with prefix
for foldername, subfolders, filenames in os.walk(folder):
    # extract files to list
    for f in filenames:
        if re.search(r"^({})".format(prefixname), f) and re.search(r"(\.{})$".format(fileext), f):
            fileList.append(f)

            # get string
            tmp = (rx.search(f)).group(2)

            # append
            numList.append(int(tmp))

            # get longest digit length
            if len(tmp) > digitLen:
                digitLen = len(tmp)

    minNum = min(numList)
    maxNum = max(numList)

if not fileList:
    print('No such files found')
else:
    # created ordered list
    ordered = sorted(numList)
    print(ordered)

    # rename files
    for i in range(len(fileList)):
        print(ordered[i])
        txt = fileList[numList.index(ordered[i])]
        txtrx = rx.search(txt)
        renamed_file = txtrx.group(1) + (str(minNum + i).rjust(digitLen, '0')) + txtrx.group(3) + txtrx.group(4)
        shutil.move(folder / Path(txt), folder / Path(renamed_file))
        print(f'renamed {txt} to {renamed_file}')

    print('Done renaming afiles to fill gaps')

