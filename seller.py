# seller.py
from user import User
from tabulate import tabulate
from itertools import groupby
from ownable import Ownable

class Seller(User, Ownable):
    def __init__(self, name):
        User.__init__(self, name)
        Ownable.__init__(self, name)
        self.items_list = []  # Lista para almacenar los artículos del vendedor

    def mostrar_productos(self):
        datos_tabla = []
        for stock in self._stock():
            datos_tabla.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
        print(tabulate(datos_tabla, headers=["Número", "Nombre del Producto", "Precio", "Cantidad"], tablefmt="grid"))

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
