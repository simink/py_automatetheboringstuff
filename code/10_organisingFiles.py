## copying files using shell utilities

import shutil, os, zipfile
from pathlib import Path

# go to docs folder
p = (Path.cwd()).parents[0] / 'docs'

# create directory 'shutil'
Path(p / 'shutil').mkdir()

# identify txt files in folder
file_list = list(Path(p / 'mad_libs').glob('*.txt'))

# copy from mad_libs folder to shutil folder
for i in file_list:
    source = f'mad_libs/{i.name}'
    dest = f'shutil/{i.name}'
    shutil.copy(p / source, p / dest)

# create zip file
newZip = zipfile.ZipFile(Path(p / 'shutil/test.zip'), 'w')
dest_list = list(Path(p / 'shutil').glob('*.txt'))
for j in dest_list:
    newZip.write(j, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


