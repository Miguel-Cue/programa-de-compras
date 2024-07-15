# shopping_app.py
from customer import Customer
from item import Item
from seller import Seller

def main():
    # Crear instancia de Seller y agregar artículos
    seller = Seller("DICストア")
    seller.add_item(Item("CPU", 40830, seller))
    seller.add_item(Item("Memoria RAM", 13880, seller))
    seller.add_item(Item("Placa madre", 28980, seller))
    seller.add_item(Item("Unidad de alimentación", 8980, seller))
    seller.add_item(Item("Caja de PC", 8727, seller))
    seller.add_item(Item("HDD de 3.5 pulgadas", 10980, seller))
    seller.add_item(Item("SSD de 2.5 pulgadas", 13370, seller))
    seller.add_item(Item("SSD M.2", 12980, seller))
    seller.add_item(Item("Refrigeración CPU", 13400, seller))
    seller.add_item(Item("Tarjeta gráfica", 23800, seller))

    # Solicitar nombre y cargar billetera del cliente
    print("🤖 Por favor, ingresa tu nombre:")
    customer = Customer(input())

    print("🏧 Ingresa la cantidad para cargar en tu billetera:")
    amount_str = input()
    while not amount_str.isdigit():  # Verifica si la cadena contiene solo dígitos
        print("⚠️ Por favor ingresa solo números. Intenta nuevamente:")
        amount_str = input()

    customer.wallet.deposit(int(amount_str))  # Convierte la cantidad válida a entero y la deposita

    print("🛍️ Comenzando compras...")

    # Mostrar la lista de productos disponibles una sola vez al inicio
    print("📜 Lista de productos disponibles:")
    seller.mostrar_productos()

    end_shopping = False
    while not end_shopping:
        print("️️⛏ Ingresa el número del producto que deseas comprar:")
        number_str = input()

        while not number_str.isdigit():  # Verifica si la cadena contiene solo dígitos
            print("⚠️ Por favor, ingresa un número válido. Intenta nuevamente:")
            number_str = input()

        number = int(number_str)  # Convierte la cantidad válida a entero

        print("⛏ Ingresa la cantidad de productos que deseas comprar:")
        quantity_str = input()

        while not quantity_str.isdigit():  # Verifica si la cadena contiene solo dígitos
            print("⚠️ Por favor, ingresa un número válido. Intenta nuevamente:")
            quantity_str = input()

        quantity = int(quantity_str)  # Convierte la cantidad válida a entero

        items = seller.pick_items(number, quantity)
        for item in items:
            customer.cart.add(item)
        
        print("🛒 Contenido del carrito:")
        customer.cart.show_items()
        print(f"🤑 Total a pagar: {customer.cart.total_amount()}")

        print("😭 ¿Deseas finalizar tus compras? (yes/no)")
        end_shopping = input() == "yes"

    print("💸 ¿Deseas confirmar la compra? (yes/no)")
    if input() == "yes":
        customer.cart.check_out()

    # Mostrar resultados finales
    print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultado ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
    print(f"️🛍️ Artículos de {customer.name}:")
    customer.cart.show_items()  # Mostrar los artículos en el carrito
    print(f"😱👛 Saldo actual en la billetera de {customer.name}: {customer.wallet.balance}")

    # Mostrar el saldo del vendedor
    print(f"😻👛 Saldo actual en la billetera de {seller.name}: {seller.wallet.balance}")

    # Mostrar el carrito nuevamente
    print("🛒 Contenido del carrito:")
    customer.cart.show_items()  # Mostrar los artículos en el carrito nuevamente
    print(f"🌚 Total a pagar: {customer.cart.total_amount()}")

    print("🎉 Fin del programa")

if __name__ == "__main__":
    main()
