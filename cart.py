class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        return sum(item.price for item in self.items)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Fondos insuficientes.")
            return
        
        for item in self.items:
            item.owner.wallet.withdraw(item.price)
            self.owner.wallet.deposit(item.price)
            item.owner = self.owner
        
        self.items = []
        print("Checkout successful.")

    def show_items(self):
        if not self.items:
            print("El carrito está vacío.")
        else:
            print("Contenido del carrito:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. Nombre: {item.name}, Precio: {item.price}")
