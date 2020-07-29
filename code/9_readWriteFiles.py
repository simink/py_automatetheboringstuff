## chpt 9 - reading writing files

from pathlib import Path
import os

### using / operator to join paths
Path('spam') / 'bacon' / 'eggs'

homefolder = Path('C:/users/dude')
subfolder = Path('spam')
homefolder / subfolder


### current working directory
Path.cwd()
os.getcwd()  # old way, not preferred

# change directory
# os.chdir('c:\\windows\\system32')  # don't run this

### home directory
Path.home()

### absolute and relative paths
os.path.abspath('.')
os.path.abspath('.\\Scripts')
os.path.isabs('.')












