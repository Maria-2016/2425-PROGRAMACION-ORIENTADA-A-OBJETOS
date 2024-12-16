# EJEMPLO DE ENCAPSULACIÓN

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria con encapsulación.
    Permite realizar operaciones como consultar saldo, depositar y retirar dinero.
    """

    def __init__(self, titular, saldo_inicial):
        # Atributos privados para proteger los datos sensibles
        self.__titular = titular  # Nombre del titular de la cuenta (María Vera en este ejemplo)
        self.__saldo = saldo_inicial  # Saldo inicial de la cuenta

    # Método público para consultar el saldo actual de la cuenta
    def consultar_saldo(self):
        """Devuelve el saldo actual de la cuenta."""
        return f"Saldo de {self.__titular}: ${self.__saldo:.2f}"

    # Método público para depositar dinero en la cuenta
    def depositar(self, monto):
        """Permite depositar una cantidad positiva de dinero en la cuenta."""
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito realizado: ${monto:.2f}. {self.consultar_saldo()}")
        else:
            print("El monto a depositar debe ser positivo.")

    # Método público para retirar dinero de la cuenta
    def retirar(self, monto):
        """Permite retirar dinero si hay suficiente saldo disponible."""
        if monto > 0:
            if monto <= self.__saldo:
                self.__saldo -= monto
                print(f"Retiro realizado: ${monto:.2f}. {self.consultar_saldo()}")
            else:
                print("Fondos insuficientes para realizar este retiro.")
        else:
            print("El monto a retirar debe ser positivo.")

    # Método público para cambiar el titular de la cuenta
    def cambiar_titular(self, nuevo_titular):
        """Permite actualizar el nombre del titular de la cuenta."""
        if nuevo_titular:
            print(f"El titular ha sido cambiado de {self.__titular} a {nuevo_titular}.")
            self.__titular = nuevo_titular
        else:
            print("El nuevo titular no puede estar vacío.")

# Ejemplo de uso de la clase CuentaBancaria

# Creación de una cuenta bancaria para María Vera con saldo inicial
cuenta_maria = CuentaBancaria("María Vera", 1000.00)

# Consultar el saldo inicial
print(cuenta_maria.consultar_saldo())

# Realizar un depósito
cuenta_maria.depositar(500)

# Intentar realizar un retiro mayor al saldo disponible
cuenta_maria.retirar(2000)

# Realizar un retiro válido
cuenta_maria.retirar(300)

# Cambiar el titular de la cuenta
cuenta_maria.cambiar_titular("María Rocío Vera")

# Consultar el saldo tras los cambios
print(cuenta_maria.consultar_saldo())
