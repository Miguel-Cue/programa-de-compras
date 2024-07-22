from tabulate import tabulate

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
        print("Pago exitoso.")

    def show_items(self):
        if not self.items:
            print("El carrito está vacío.")
        else:
            # Crear un diccionario para agrupar los productos por nombre
            grouped_items = {}
            for item in self.items:
                if item.name in grouped_items:
                    grouped_items[item.name]['quantity'] += 1
                else:
                    grouped_items[item.name] = {'price': item.price, 'quantity': 1}

            # Crear los datos para el formato tabular
            table_data = []
            for index, (name, details) in enumerate(grouped_items.items(), start=1):
                table_data.append([index, name, details['price'], details['quantity']])

            # Mostrar los datos en formato tabular
            print(tabulate(table_data, headers=["N°", "Producto", "Precio", "Cantidad"], tablefmt="grid"))
