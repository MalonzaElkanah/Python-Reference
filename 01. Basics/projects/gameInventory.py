stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("INVENTORY")
    item_total = 0
    for i, j in inventory.items():
        print(str(j)+" "+i)
        item_total += j
    print("Total NUmber of Items: ", item_total)


def add_to_inventory(inventory, add_item):
    for i in add_item:
        added = False
        for k, j in inventory.items():
            if i == k:
                j += 1
                inventory[k] = int(j)
                added = True
        if not added:
            inventory[i] = int(1)
    return inventory


display_inventory(stuff)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = add_to_inventory(stuff, dragonLoot)
display_inventory(stuff)
