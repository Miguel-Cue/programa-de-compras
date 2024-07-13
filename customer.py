from user import User
from cart import Cart

class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)  # Inicializar el carrito para el cliente
        self.items = []  # Inicializar la lista de artículos del cliente

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"{item.name}: {item.price}")

    # Otros métodos de la clase Customer si los hay
