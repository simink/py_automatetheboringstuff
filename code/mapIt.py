#! python3
# launches map in browser using address from commandline or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from commandline
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
