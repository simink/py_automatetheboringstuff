## make zigzag patterns

import time, sys
indent = 0  # number of spaces to indent
indentIncreasing = True  # whether identation is increasing or not

try:
    while True:  # main program
        print(' '*indent, end='')
        print('*******')
        time.sleep(0.1)  # pause for 1/10th second

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False  # change direction
            
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()