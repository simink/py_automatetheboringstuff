#! python 3
"""
Program that reads in text files and lets users replace some keywords. Lastly, save as new file
"""

from pathlib import Path
import re

### read in text file
file_name = input("Enter relative path of file (eg. folder/file.txt): ")
p = Path(Path.cwd() / file_name)
input_file = open(p)
txt = input_file.read()
print(txt)

### find following keywords
kwRegex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
kwList = kwRegex.findall(txt)

### get user to input string to replace
for i in kwList:
    replaceWord = input(f'Enter a {i}:')
    txt = txt.replace(i, replaceWord, 1)

### save updated text to new file
print(txt)

# consider identifying how many different parents levels are there
out_file_name = input("Enter relative path of new file (eg. folder/file.txt): ")
new_file = open(f"{Path.cwd() / out_file_name}", 'w')
new_file.write(txt)

input_file.close()
new_file.close()