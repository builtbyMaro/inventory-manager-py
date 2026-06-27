from inventory import InventoryManager, Inventory, Item
from inventory_manager_utils import add_inventory, delete_inventory, view_inventories, add_item, update_item, delete_item, view_items

is_running = True
current_inventory = None
manager = InventoryManager()

def inventory_opened(current_inventory):
    while isinstance(current_inventory, Inventory):

        print(f"=== {current_inventory.name.capitalize()} Inventory ===")
        print("1. Add new Item")
        print("2. Update existing item")
        print("3. Delete an item")
        print("4. View all items")
        print("5. Go back to inventory manager")
        try:
            choice = int(input("What would you like to do ? "))
            match choice:
                case 1:
                    add_item(current_inventory)
                case 2:
                    update_item(current_inventory)
                case 3:
                    delete_item(current_inventory)
                case 4:
                    view_items(current_inventory)
                case 5:
                    current_inventory = None
                    break
                case _:
                    print("----------------------")
                    print("Please enter 1/2/3/4/5")
                    print("----------------------")
        except ValueError:
            print("----------------------")
            print("Please enter 1/2/3/4/5")
            print("----------------------")



while is_running:
    print("=== Inventory Manager ===")
    print("1. Open Inventory")
    print("2. Add Inventory")
    print("3. Delete Inventory")
    print("4. View Inventories")
    print("5. Exit")
    try:
        choice = int(input("What would you like to do ? "))
        match choice:
            case 1:
                user_input = input("Inventory name: ").lower()
                inventory = manager.open_inventory(user_input)
                if isinstance(inventory, Inventory):
                    current_inventory = inventory
                    inventory_opened(current_inventory)
                else:
                    print("----------------------")
                    print(f"{user_input} doesn't exist")
                    print("----------------------")
            case 2:
                add_inventory(manager)
            case 3:
                delete_inventory(manager)
            case 4:
                view_inventories(manager)
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

