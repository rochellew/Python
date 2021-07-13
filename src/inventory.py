# Fantasy inventory tracker

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'box': 15}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # For grammar's sake
        if  k[-1] in ['s','x','z'] or k[-2:] in ['ch', 'sh']:
            print(f'{k}es: {v}')
        else:
            print(f'{k}s: {v}')
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
