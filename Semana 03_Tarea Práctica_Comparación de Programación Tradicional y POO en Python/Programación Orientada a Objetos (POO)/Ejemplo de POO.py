# Ejemplo del promedio semanal del clima con Programación Orientada a Objetos (POO)
# Encapsulamiento

class Clima:
    # Constructor de la clase
    def __init__(self):
        # Atributos privados para almacenar las temperaturas de los 7 días
        self.__temperaturas = [0] * 7  # Inicializa una lista con 7 valores (un valor para cada día)

    # Método para ingresar la temperatura de un día específico
    def ingresar_temperatura(self, dia, temperatura):
        if 0 <= dia < 7:  # Aseguramos que el día esté entre 0 y 6 (lunes a domingo)
            self.__temperaturas[dia] = temperatura
        else:
            print("Día inválido. Debe ser un valor entre 0 y 6.")  # Verificamos que el día esté en el rango correcto

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        suma_temperaturas = sum(self.__temperaturas)  # Sumar las temperaturas
        promedio = suma_temperaturas / len(self.__temperaturas)  # Dividir por el número de días (7 días)
        return promedio  # Retorna el promedio de las temperaturas

    # Método para mostrar las temperaturas de la semana
    def mostrar_temperaturas(self):
        print("Temperaturas de la semana:", self.__temperaturas)

# Crear un objeto de la clase Clima
mi_clima = Clima()

# Ingresar las temperaturas para cada día de la semana
mi_clima.ingresar_temperatura(0, 23.5)  # Lunes
mi_clima.ingresar_temperatura(1, 24.0)  # Martes
mi_clima.ingresar_temperatura(2, 25.0)  # Miércoles
mi_clima.ingresar_temperatura(3, 22.5)  # Jueves
mi_clima.ingresar_temperatura(4, 21.0)  # Viernes
mi_clima.ingresar_temperatura(5, 20.0)  # Sábado
mi_clima.ingresar_temperatura(6, 23.0)  # Domingo

# Mostrar las temperaturas ingresadas
mi_clima.mostrar_temperaturas()

# Calcular el promedio semanal
promedio_semanal = mi_clima.calcular_promedio()
print(f"El promedio semanal de la temperatura es: {promedio_semanal:.2f}°C")
