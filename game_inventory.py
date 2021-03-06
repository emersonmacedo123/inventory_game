
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.

#testing inventory
myInventory = {}
myInventory["Key1"] = 2
myInventory["Key2"] = 3
myInventory["Key3"] = 75




def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for key, value in inventory.items():
        print(f"{key}: {value}")



def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory



def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if item in inventory.keys():
            inventory[item] -= 1
            if inventory[item] <= 0:
                inventory.pop(item)
    return inventory


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    print("-----------------")
    print("item name | count")
    print("-----------------")
    for item in inventory.keys():
        print(f"     {item} |  {inventory[item]}")
    print("-----------------")

print_table(myInventory,1)

def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
