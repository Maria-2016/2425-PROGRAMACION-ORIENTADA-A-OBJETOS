# Programa para determinar el promedio semanal del clima usando Programación Tradicional

# Definir una función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas diarias de la semana.
    Retorna una lista con 7 temperaturas.
    """
    print("Ingrese las temperaturas diarias (7 días):")
    temperaturas = []  # Lista vacía para almacenar las temperaturas
    for i in range(7):  # Iterar por cada día de la semana
        while True:
            try:
                temp = float(input(f"Día {i + 1}: "))  # Solicitar la temperatura del día i
                temperaturas.append(temp)  # Agregar la temperatura a la lista
                break  # Salir del bucle si el ingreso es correcto
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

# Definir una función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Recibe:
        temperaturas (list): Lista con temperaturas.
    Retorna:
        float: El promedio de las temperaturas.
    """
    suma = sum(temperaturas)  # Sumar todas las temperaturas
    promedio = suma / len(temperaturas)  # Dividir por el número de temperaturas
    return promedio

# Definir la función principal que organiza la ejecución del programa
def main():
    """
    Función principal del programa que coordina el flujo de ejecución.
    """
    # Paso 1: Ingresar las temperaturas diarias
    temperaturas = ingresar_temperaturas()

    # Paso 2: Calcular el promedio semanal
    promedio_semanal = calcular_promedio(temperaturas)

    # Paso 3: Mostrar el resultado
    print("\nRESULTADO:")
    print(f"Las temperaturas ingresadas son: {temperaturas}")
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f} grados.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
