"""
alter english words.
if word begins with a vowel, add yay eg. ace = aceyay
if word begins with consonant or cluster, move them to the end followed by ay eg. char = archay

"""

# english to latin
print("Enter english message to translate into pig latin:")
msg = input()

vowels = ('a','e','i','o','u','y')

pigLatin = []

# split words and check for non-letters at start and end of work

for word in msg.split():
    # separate non-letters at start
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]  # remove non-letter
    
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # separate non-letters at end
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # remember if word is uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    # make word to lower
    word = word.lower()

    # separate consonants
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefixConsonants += word[0]
        word = word[1:]

    # then add pig latin
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # set word back to uppercase or title
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # add non-letters back to start and end
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

print(' '.join(pigLatin))