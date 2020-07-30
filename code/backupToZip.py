#! python 3
"""
copies an entire folder and its contents into a zip file which incremental filename
"""
from pathlib import Path
import zipfile, os

def backupToZip(source, dest):

    """
    source - source folder to be zipped
    dest - destination folder to store zipped file
    """

    # get absolute path of folder
    source = os.path.abspath(source)
    dest = os.path.abspath(dest)
    print(source)
    print(dest)

    # figure filename
    num = 1
    while True:
        zipFilename = os.path.basename(source) + '_' + str(num) + '.zip'
        print(dest / Path(zipFilename))

        if not os.path.exists(dest / Path(zipFilename)):
            break

        num = num + 1

    # create zip file
    print(f'Creating {zipFilename}...')
    # print(f)
    backupZip = zipfile.ZipFile(dest / Path(zipFilename), 'w')

    # walk entire folder tree and compress files in each folder
    for foldername, subfolders, filenames in os.walk(source):
        print(f'Adding files in {foldername}...')
        # add current folder to zip file
        backupZip.write(foldername)

        # add all files in this folder to zip
        for filename in filenames:
            newBase = os.path.basename(source) + '_'

            # don't backup the backup zip files
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()

    print('Done zipping!')

# test
zip_from = Path.cwd() / 'docs/backupToZip'
zip_to = Path.cwd() / 'docs'
backupToZip(zip_from, zip_to)