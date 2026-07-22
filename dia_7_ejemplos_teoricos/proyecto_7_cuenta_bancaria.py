
class Persona: 

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__ (self, nombre, apellido, numero_cuenta, saldo_cuenta):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo_cuenta = saldo_cuenta

    def __str__(self):

        return f"Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Saldo: {self.saldo_cuenta:.2f} €"

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo_cuenta += cantidad
            print(f"Depósito de {cantidad:.2f} € realizado. Nuevo saldo: {self.saldo_cuenta:.2f} €")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo_cuenta:
                self.saldo_cuenta -= cantidad
                print(f"Retiro de {cantidad:.2f} € realizado. Nuevo saldo: {self.saldo_cuenta:.2f} €")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    saldo_cuenta = float(input("Ingrese el saldo inicial de la cuenta: "))
    return Cliente(nombre, apellido, numero_cuenta, saldo_cuenta)

def inicio():
    cliente = crear_cliente()
    print(cliente)
    while True:
    
        print("\nOpciones:")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar información del cliente")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == "3":
            print(cliente)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


inicio()