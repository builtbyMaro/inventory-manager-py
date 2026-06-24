from inventory_utils import write_file, read_file

file_path = "inventory.json"

class InventoryManager:
    def __init__(self):
        self.items = [Item.from_dict(item) for item in read_file(file_path)]

    def add_item(self, item):
        self.items.append(item)
        write_file(file_path, [item.to_dict() for item in self.items])

    def update_item(self, item_name, **kwargs):
        for item in self.items:
            if item.name == item_name:
                item.update(**kwargs)
        write_file(file_path, [item.to_dict() for item in self.items])
                
    def delete_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
        write_file(file_path, [item.to_dict() for item in self.items])
        
    
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

        if "price" in kwargs:
            self.price = kwargs["price"]

        if "quantity" in kwargs:
            self.quantity = kwargs["quantity"]

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


