## program that asks users for sandwich preferences and display total cost

import pyinputplus as pyip

# bread type
bread_type = pyip.inputMenu(
    ['wheat', 'white', 'sourdough'], 
    prompt = 'Choose your bread type:\n', 
    numbered = True)
print(f'You have selected {bread_type}.')

# protein type
protein_type = pyip.inputMenu(
    ['chicken', 'turkey', 'ham', 'tofu'], 
    prompt = ' Choose your protein type.\n',
    numbered = True)
print(f'You have selected {protein_type}.')

# cheese type
want_cheese = pyip.inputYesNo(prompt = 'Do you want cheese? (y/n)')

if want_cheese == "yes":
    cheese_type = pyip.inputMenu(
        ['cheddar', 'swiss', 'mozzarella'], 
        prompt = 'Choose your cheese type:\n', 
        numbered = True)

    print(f'You have selected {cheese_type}.')
else:
    cheese_type = 'no_cheese'

# sauce type
sauce_type = pyip.inputMenu(
    ['mayo', 'mustard', 'lettuce', 'tomato'], 
    prompt = ' Choose your sauce type.\n',
    numbered = True)
print(f'You have selected {sauce_type}.')

# quantity
qty = pyip.inputInt('How many sandwiches?', min=1)

# display order
sandwich = [bread_type, protein_type, cheese_type, sauce_type]
print(f'Repeat your sandwich order {sandwich} and quantity is {qty}.')


# display total cost
food_cost = {'wheat': 1, 'white': 1, 'chicken': 2, 'ham': 3, 'mozzarella': 1}

total_cost = 0
for i in range(len(sandwich)):
    food_cost.setdefault(sandwich[i], 0)
    total_cost += food_cost[sandwich[i]]

print(f'Total costs for your sandwiches is ${total_cost * qty}.')
