#! python3
"""
Program supposed to delete unneeded files by checking those large sized ones. However, we will just walk through the folder and display those files exceeding (not including) a certain file size
"""

import os
from pathlib import Path

def displayLargeFiles(folder, filesize):

    # check file size is numeric
    if not (type(filesize) is int or type(filesize) is float):
        raise TypeError('Only numbers are allowed')

        # get absolute path
    folder = os.path.abspath(folder)

    largeFiles = {}

    # walk through folder
    for foldername, subfolders, filenames in os.walk(folder):
        if not filenames:
            print('empty')
        else:
            for i in filenames:
                fs = os.path.getsize(Path(foldername / Path(i)))
                if fs > filesize:
                    print(i)
                    largeFiles.setdefault(i, fs)

    print('The following large files are found: ')
    print(largeFiles)



### test
zip_from = Path.cwd() / 'docs/backupToZip'
displayLargeFiles(zip_from, 1000)