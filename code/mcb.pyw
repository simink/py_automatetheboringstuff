#! python3
""" this file saves and loads pieces of text to the clipboard
usage:
py.exe mcb.pyw save <keyword> - saves clipboard to keyword
py.exe mcb.pyw <keyword> - loads keyword to clipboard
py.exe mcb.pyw list - loads all keywords to clipboard
py.exe mcb.pyw delete <keyword> - delete keyword
py.exe mcb.pyw delete_all - delete all keywords
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(f"{sys.argv[2]} keyword is saved to clipboard")
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    print(f"{sys.argv[2]} keyword is deleted")
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('All keywords copied to clipboard')
    elif sys.argv[1].lower() == 'delete_all':
        mcbShelf.clear()
        print('All keywords and content are deleted')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print(f"{sys.argv[1]} keyword doesn't exist.")

mcbShelf.close()