# Fantasy inventory tracker -- plus  dragon's dropped loot

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        # For grammar's sake
        if k[-1] in ['s', 'x', 'z'] or k[-2:] in ['ch', 'sh']:
            print(f'{k}es: {v}')
        else:
            print(f'{k}s: {v}')
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'torch': 2, 'box': 4}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
