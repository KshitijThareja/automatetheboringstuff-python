#List to Dictionary Function for Fantasy Game Inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(v,k)
        item_total+=v
    print("Total number of items: " + str(item_total))



def addToInventory(inventory, addedItems):
    # your code goes here
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i]+=1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)