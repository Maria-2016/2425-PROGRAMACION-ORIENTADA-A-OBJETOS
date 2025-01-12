# Programa para calcular el área de un círculo
# Este programa solicita el radio de un círculo y calcula su área utilizando la fórmula A = π * r^2

import math


def calcular_area_circulo(radio):
    """
    Función que calcula el área de un círculo dado su radio.
    Parámetros:
    radio (float): El radio del círculo

    Retorna:
    float: El área del círculo
    """
    area = math.pi * (radio ** 2)  # Fórmula del área de un círculo
    return area


# Solicitar el radio del círculo al usuario
radio_usuario = float(input("Introduce el radio del círculo en metros: "))

# Calcular el área
area_circulo = calcular_area_circulo(radio_usuario)

# Mostrar el resultado
print(f"El área del círculo con radio {radio_usuario} metros es {area_circulo:.2f} metros cuadrados.")
