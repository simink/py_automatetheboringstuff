#! python3

"""
Program checks file sequence and create files to fill in that gap

Assumes that the number sequence starts from the smallest digit and not from 1.
"""

import os, re, copy, shutil
from pathlib import Path

### inputs
folder = Path.cwd() / 'docs/fill_in_gap_create'
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

## change formatting of the files
if not fileList:
    print('No such files found')
else:
    for i in range(minNum, maxNum+1):
        if i in numList:
            txt = fileList[numList.index(i)]
            txtrx = rx.search(txt)
            renamed_file = txtrx.group(1) + (str(i).rjust(digitLen, '0')) + txtrx.group(3) + txtrx.group(4)
            shutil.move(folder / Path(txt), folder / Path(renamed_file))
            print(f'renamed {txt} to {renamed_file}')
        else:
            renamed_file = prefixname + (str(i).rjust(digitLen, '0')) + txtrx.group(3) + "." + fileext
            newFile = open(folder / Path(renamed_file), 'w')
            newFile.write('this file did not exist before.')
            newFile.close()
            print(f'created new file {renamed_file}')

    print('Done renaming and creating files to fill gaps')