## create a function to add a player's new items to his existing inventory
from inventory import displayInventory

def addToInventory(inventory, addedItems):

    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1

    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)