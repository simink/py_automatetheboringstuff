#! python3
"""
Program searches all txt files and searches for any lines containing a particular keyword and display them
"""
from pathlib import Path
import re

# open all txt files based on folder provided
folder_name = input("Enter folder name (eg. folder/folder): ")
p = Path(Path.cwd() / folder_name)
file_list = list(p.glob('*.txt'))
print(file_list)

# user input keyword
kw = input("Enter keyword to be searched: ")

# for each file, read in as lines
kw_list = []

for i in range(len(file_list)):
    f = open(file_list[i])
    txt = f.readlines()
    # for each line, search keyword
    for j in range(len(txt)):
        if kw in txt[j].lower().split():
            kw_list.append(f'{txt[j].strip()} - {file_list[i].name}')

    f.close()

if not kw_list:
    print('keyword not found')
else:
    print(kw_list)
    out_file_name = input("Enter relative path of new file (eg. folder/file.txt): ")
    new_file = open(f"{Path.cwd() / out_file_name}", 'w')
    
    for k in kw_list:
        new_file.write(f'{k}\n')
    
    print(f'Results saved to {out_file_name}')


