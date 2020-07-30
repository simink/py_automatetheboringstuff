#! python3
"""
Program selectively walks through a folder tree and searches for files of a certain file extension and copies them to another new location

# take note that this doesn't take into account if the filenames from different folders are the same and may result in overwrite
"""

from pathlib import Path
import os, re, shutil

def selectiveCopy(source, dest, file_ext):

    # get absolute paths
    source = os.path.abspath(source)
    dest = Path(dest)

    # get pattern
    extRegex = re.compile('^.*\.(.*)$')

    # walk through entire folder tree
    for foldername, subfolders, filenames in os.walk(source):
        
        if not filenames:
            print('empty')
        else:
            for i in filenames:
                # check for file ext
                if (extRegex.search(i)).group(1) == file_ext:
                    print(f'copy {Path(foldername / Path(i))} \nto {Path(dest / Path(i))}\n')
                    shutil.copy(Path(foldername / Path(i)), Path(dest / Path(i)))

        print(f'Done copying files with extension .{file_ext}')


# test
zip_from = Path.cwd() / 'docs/backupToZip'
zip_to = Path.cwd() / 'docs/backupFolder'
selectiveCopy(zip_from, zip_to, 'pdf')
