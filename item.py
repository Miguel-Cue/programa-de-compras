# item.py
class Item:
    instances = []

    def __init__(self, name, price, owner=None, quantity=1):
        self.name = name
        self.price = price
        self.owner = owner
        self.quantity = quantity
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

    @staticmethod
    def item_all():
        return Item.instances
