## regex version of strip

import re

def regexStrip(txt, char=None):

    print(char)
  
    if char == None:
        # remove start and ending spaces
        remove_spaces = re.compile(r'(^\s*)(.*)(\s*$)')
        trimmed = remove_spaces.search(txt).group(2)
        print(trimmed)
    else:
        # remove start, end based on characters input
        remove_start = re.compile(r'^({})*'.format(char))
        remove_end = re.compile(r'({})*$'.format(char))
        trimmed = remove_start.sub(r'', txt)
        trimmed = remove_end.sub(r'', trimmed)
        print(trimmed)


regexStrip('tttthis a long 9s text .   4t', 'tt')