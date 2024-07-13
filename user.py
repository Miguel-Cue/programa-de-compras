from wallet import Wallet  # Importar Wallet desde el archivo correcto

class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)   # Inicializar Wallet con el usuario como propietario
