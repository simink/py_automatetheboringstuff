#! python 3
# myclip.py - a multi-clip program

TEXT = {
    'agree': """Yes, I agree.\nThat sounds fine to me""",
    'busy': """Sorry can we do this later""",
    'upsell': """Would you consider making a donation"""
    }

import sys, pyperclip

if len(sys.argv) < 2:  # checks for first commandline argument
    print('Usage: python myclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There is no such {keyphrase}')

