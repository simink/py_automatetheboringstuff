#! python3
"""
Renames filenames with american date format of MM-DD-YYYY to european DD-MM-YYYY
"""

import shutil, os, re


datePattern = re.compile(r"""^(.*?)  # all text before date
    ((0|1)?\d)-  # month
    ((0|1|2|3)?\d)-  # day
    ((19|20)\d\d)  # year
    (.*?)$  # all text after date
""", re.VERBOSE)

print(os.listdir('.'))

# loop over files in working directory
for usFile in os.listdir('.\\docs\\rename_dates'):
    # print(usFile)
    mo = datePattern.search(usFile)
    # print(mo)

    # no file exist
    if mo == None:
        continue

    # get different parts of filenames
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # form european-style filename
    euFile = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # get absolute path
    absPath = os.path.abspath('.\\docs\\rename_dates')
    usFile_abs = os.path.join(absPath, usFile)
    euFile_abs = os.path.join(absPath, euFile)

    # rename files
    print(f"rename {usFile_abs} to {euFile_abs}\n")
    shutil.move(usFile_abs, euFile_abs)





