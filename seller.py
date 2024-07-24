# seller.py
from user import User
from tabulate import tabulate
from itertools import groupby
from item import Item

class Seller(User):
    def __init__(self, name):
        super().__init__(name)
        self.items_list = []

    def mostrar_productos(self):
        headers = ["Número", "Nombre", "Precio", "Cantidad"]
        table = []
        for index, item in enumerate(self.items_list):
            table.append([index, item.name, item.price, item.quantity])
        print(tabulate(table, headers=headers, tablefmt="grid"))

    def _stock(self):
        lista_de_items = self.items_list
        lista_de_items.sort(key=lambda m: m.name)
        grupos = []
        for clave, grupo in groupby(lista_de_items, key=lambda m: m.name):
            grupos.append(list(grupo))
        stock = []
        for index, item in enumerate(grupos):
            stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})
        return stock

    def add_item(self, item):
        self.items_list.append(item)

    def pick_items(self, number, quantity):
        selected_items = []
        if 0 <= number < len(self.items_list):
            item = self.items_list[number]
            if item.quantity >= quantity:
                item.quantity -= quantity
                for _ in range(quantity):
                    selected_items.append(Item(item.name, item.price, item.owner, 1))
            else:
                print("Cantidad insuficiente disponible.")
        else:
            print("Número de producto inválido.")
        return selected_items
