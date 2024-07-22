# seller.py
from user import User
from tabulate import tabulate
from itertools import groupby

class Seller(User):
    def __init__(self, name):
        super().__init__(name)
        self.items_list = []  # Lista para almacenar los artículos del vendedor

    def mostrar_productos(self):
        headers = ["Número", "Nombre", "Precio"]
        table = []
        for index, item in enumerate(self.items_list):
            table.append([index, item.name, item.price])
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
        index = 0
        for item in self.items_list:
            if index == number:
                selected_items.extend([item] * quantity)
            index += 1
        return selected_items
