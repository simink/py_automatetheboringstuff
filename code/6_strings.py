## chpt 6 - strings


name = 'dp'
age = 40

"My name is %s. I'm %s years old." % (name, age)
f"My name is {name}. Next year I will be {age+1}."

# useful string methods
spam = "Hello, world!"

spam.isupper()
'12345'.isupper()
spam.upper().lower()

## join, split methods

','.join(['cats', 'dogs','rabbits'])
' animals '.join(['cats', 'dogs','rabbits']).split()

## partition
spam.partition('w')
spam.partition('zy')
before, sep, after = spam.partition('w')
print(before)

# rjust, ljust, center
'hi'.ljust(20, "-")

## strip whitespaces
dude = 'asdfPigfdsa'
dude.strip('asfd')

## ord and chr
ord('A')
chr(65)

# pyperclip - copy paste




















