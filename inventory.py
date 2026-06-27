from inventory_utils import write_file, read_file

file_path = "inventory.json"

class InventoryManager:

    def __init__(self):
        self.storage_data = read_file(file_path)

    def create_inventory(self, name):
        if name in self.storage_data:
            return False
        
        new_inventory = Inventory(name, self)
        self.save_inventory(new_inventory)
        return new_inventory

    def remove_inventory(self, name):
        self.storage_data.pop(name)
        write_file(file_path, self.storage_data)
        
    def open_inventory(self, name):
        if name not in self.storage_data:
            return None
        
        inventory = Inventory(name, self)
        inventory.items = [Item.from_dict(item) for item in self.storage_data[name]]
        return inventory

    def save_inventory(self, inventory):
        items = [item.to_dict() for item in inventory.items]
        self.storage_data[inventory.name] = items
        write_file(file_path, self.storage_data)

    def view_inventories(self):
        return self.storage_data

class Inventory:

    def __init__(self, name, manager: InventoryManager):
        self.name = name
        self.manager = manager
        self.items = []

    def add_item(self, name, price, quantity):
        item = Item(name, price, quantity)
        self.items.append(item)
        self.manager.save_inventory(self)

    def update_item(self, item_name, **kwargs):
        for item in self.items:
            if item.name == item_name:
                item.update(**kwargs)
                self.manager.save_inventory(self)

    def delete_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                self.manager.save_inventory(self)
        
    def view_items(self):
        return self.items



class Item:
    def __init__(self, name, price, quantity):
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )

    def update(self, **kwargs):
        if "name" in kwargs:
            self.name = kwargs["name"]
            return True

        if "price" in kwargs:
            self.price = kwargs["price"]
            return True

        if "quantity" in kwargs:
            self.quantity = kwargs["quantity"]
            return True

    def to_dict(self):
        return{
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["price"],
            data["quantity"]
        )


