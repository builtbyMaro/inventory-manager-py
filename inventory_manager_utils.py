from inventory import InventoryManager, Inventory

def add_item(inventory: Inventory):
    while True:
        try:
            name = input("Enter Item name: ").lower()
            if any(item.name == name for item in inventory.items):
                print("------------------------")
                print("This item already exists")
                print("------------------------")
                return
            price = float(input("Enter Item price: "))
            quantity = int(input("Enter Item quantity: "))

            inventory.add_item(name, price, quantity)
            print("------------------------")
            print("Item added successfully.")
            print("------------------------")
            return
        except ValueError:
            print("--------------------------------")
            print("Please enter appropriate values:")
            print("1. Prices can only be numbers.")
            print("2. Quantities can only be numbers but cannot contain decimal places.")
            print("-------------------------------")

def update_item(inventory: Inventory):
    while True:
        name = input("Enter the name of the item you want to update: ").lower()
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
                                new_name = input("Enter new item name: ").lower()
                                inventory.update_item(item_name=name, name=new_name)
                            case 2:
                                new_price = float(input("Enter new price: "))
                                inventory.update_item(item_name=name, price=new_price)
                            case 3:
                                new_quantity = int(input("Enter new quantity: "))
                                inventory.update_item(item_name=name, quantity=new_quantity)
                            case _:
                                print("-----------------")
                                print("Please pick 1/2/3")
                                print("-----------------")
                    except ValueError:
                        print("--------------------------------")
                        print("Please enter appropriate values:")
                        print("1. Prices can only be numbers.")
                        print("2. Quantities can only be numbers but cannot contain decimal places.")
                        print("--------------------------------")

                    print("------------------------")
                    print("Item updated successfully.")
                    print("------------------------")
                    break
                except ValueError:
                    print("-----------------")
                    print("Please pick 1/2/3")
                    print("-----------------")
            break
        else:
            print("---------------")
            print("Item not found.")
            print("---------------")
            break

def delete_item(inventory: Inventory):
    while True:
        name = input("Enter name of the item you would like to delete: ").lower()
        item_found = False
        for item in inventory.items:
            if item.name == name:
                item_found = True

        if item_found:
            print("------------------------")
            sure = input("Are you sure ? Y/N ").lower()
            if sure == "y":
                inventory.delete_item(name)
                print("-------------------------")
                print("Item deleted successfully")
                print("-------------------------")
            else:
                print("----------------")
                print("Delete cancelled")
                print("----------------")
                break
        else:
            print("--------------")
            print("Item not found")
            print("--------------")
        break

def view_items(inventory: Inventory):
    items = inventory.view_items()
    if not items:
        print("----------------")
        print("Inventory Empty.")
        print("----------------")
    else:
        print(f"=== {inventory.name.capitalize()} ===")
        for item in inventory.view_items():
            print("------------------------")
            print(item)
            print("------------------------")

def add_inventory(manager: InventoryManager):
    name = input("Enter Inventory name: ").lower()
            
    if manager.create_inventory(name):
        print("------------------------")
        print("Inventory added successfully")
        print("------------------------")
    else:
        print("------------------------")
        print("This inventory already exists")
        print("------------------------")

def delete_inventory(manager: InventoryManager):
    name = input("Enter Inventory name: ").lower()

    if name in manager.storage_data:
        sure = input("Are you sure ? Y/N ").lower()
        if sure == "y":
            manager.remove_inventory(name)
            print("------------------------------")
            print("Inventory deleted successfully")
            print("------------------------------")
        else:
            print("----------------")
            print("Delete cancelled")
            print("----------------")
    else:
        print("------------------------")
        print(f"{name} doesn't exists")
        print("------------------------")

def view_inventories(manager: InventoryManager):
    if not manager.storage_data:
        print("----------------")
        print("Inventory Empty.")
        print("----------------")
    else:
        print("----------------")
        for inventory in manager.storage_data.keys():
            print(inventory)
        print("----------------")