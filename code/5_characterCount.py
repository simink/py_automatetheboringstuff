# count number of characters
import pprint
message = 'this is A really long message but it is necessary'

count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1

print(count)
print('pretty print below')
pprint.pprint(count)