from inventory import InventoryManager, Item

def add_item(inventory: InventoryManager):
    while True:
        try:
            name = input("Enter Item name: ")
            price = float(input("Enter Item price: "))
            quantity = int(input("Enter Item quantity: "))

            new_item = Item(name, price, quantity)
            inventory.add_item(new_item)
            print("------------------------")
            print("Item added successfully.")
            print("------------------------")
            break
        except ValueError:
            print("Please enter appropriate values:")
            print("1. Prices can only be numbers.")
            print("2. Quantities can only be numbers but cannot contain decimal places.")

def update_item(inventory: InventoryManager):
    while True:
        name = input("Enter the name of the item you want to update: ")
        item_found = False
        for item in inventory.items:
            if item.name == name:
                item_found = True
        
        if item_found:
            while True:
                try:
                    print("-------------")
                    print("1. Name")
                    print("2. Price")
                    print("3. Quantity")
                    choice = int(input("What would you like to update ?"))

                    try:

                        match choice:
                            case 1:
                                new_name = input("Enter new item name: ")
                                inventory.update_item(item_name=name, name=new_name)
                            case 2:
                                new_price = float(input("Enter new price: "))
                                inventory.update_item(item_name=name, price=new_price)
                            case 3:
                                new_quantity = int(input("Enter new quantity: "))
                                inventory.update_item(item_name=name, quantity=new_quantity)
                            case _:
                                print("Please pick 1/2/3")
                    except ValueError:
                        print("Please enter appropriate values:")
                        print("1. Prices can only be numbers.")
                        print("2. Quantities can only be numbers but cannot contain decimal places.")

                    print("------------------------")
                    print("Item updated successfully.")
                    print("------------------------")
                    break
                except ValueError:
                    print("Please pick 1/2/3")
            break
        else:
            print("Item not found.")
            break

def delete_item(inventory: InventoryManager):
    while True:
        name = input("Enter name of the item you would like to delete: ")
        item_found = False
        for item in inventory.items:
            if item.name == name:
                item_found = True

        if item_found:
            sure = input("Are you sure ? Y/N ").lower()
            if sure == "y":
                inventory.delete_item(name)
                print("Item deleted successfully")
            else:
                print("Delete cancelled")
                break
        else:
            print("Item not found")
        break

def view_items(inventory: InventoryManager):
    items = inventory.view_items()
    if not items:
        print("Inventory Empty.")
    else:
        for item in inventory.view_items():
            print(item)

is_running = True
inventory = InventoryManager()

while is_running:

    print("=== Inventory Manager ===")
    print("1. Add new Item")
    print("2. Update existing item")
    print("3. Delete an item")
    print("4. View all items")
    print("5. Exit")
    try:
        choice = int(input("What would you like to do ? "))
        match choice:
            case 1:
                add_item(inventory)
            case 2:
                update_item(inventory)
            case 3:
                delete_item(inventory)
            case 4:
                view_items(inventory)
            case 5:
                is_running = False
            case _:
                print("----------------------")
                print("Please enter 1/2/3/4/5")
                print("----------------------")
    except ValueError:
        print("----------------------")
        print("Please enter 1/2/3/4/5")
        print("----------------------")


