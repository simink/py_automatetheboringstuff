## dict of friend's bdays

# bday database
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# main
while True:
    name = input('Key a name: (enter to quit)')
    if name == '':
        break

    if name in birthdays:
        print(name + '\'s bday on ' + birthdays[name])
    else:
        print('No information about ' + name)
        bday = input('Key in their bday')
        birthdays[name] = bday
        print('update birthday database')
