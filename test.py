from inventory import InventoryManager, Item

manager = InventoryManager()

phones = manager.create_inventory("phones")
laptops = manager.create_inventory("laptops")

item1 = Item("iphone 12 pro", 350000, 26)
item2 = Item("Samsung S24 ultra", 500000, 18)
item3 = Item("Dell latitude", 400000, 17)
item4 = Item("Macbook M4", 700000, 28)

phones.add_item(item1)
phones.add_item(item2)
laptops.add_item(item3)
laptops.add_item(item4)

for item in phones.view_items():
    print(item)