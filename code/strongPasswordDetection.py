## detect strong password
# at least 8 characters long, upper/lower case and on digit

import re

def detectStrongPassword(x):
    isStrong = 'Password is strong'

    lowerChar = re.compile('[a-z]')
    upperChar = re.compile('[A-Z]')
    hasDigit = re.compile('\d')


    if len(x) < 8:
        isStrong = "password needs to be at least 8 characters in length"
    elif lowerChar.search(x) == None:
        isStrong = "password needs to have at least one lowercase character"
    elif upperChar.search(x) == None:
        isStrong = "password needs to have at least one uppercase character"
    elif hasDigit.search(x) == None:
        isStrong = "password needs to have at least one digit"
    else:
        isStrong

    print(isStrong)

detectStrongPassword('AdAAAhd9')
