
import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Semana_02_Desarrollo de Ejemplos de Técnicas de Programación POO/Abstracción/Abstracción.py',
        '2': 'Semana_02_Desarrollo de Ejemplos de Técnicas de Programación POO/Encapsulación/Encapsulación.py',
        '3': 'Semana_02_Desarrollo de Ejemplos de Técnicas de Programación POO/Herencia/Herencia.py',
        '4': 'Semana_02_Desarrollo de Ejemplos de Técnicas de Programación POO/Polimorfismo/Polimorfismo.py',
        '5': 'Semana 03_Tarea Práctica_Comparación de Programación Tradicional y POO en Python/Programación Orientada a Objetos (POO)/Ejemplo de POO.py',
        '6': 'Semana 03_Tarea Práctica_Comparación de Programación Tradicional y POO en Python/Programación Tradicional/Ejemplo de PT.py',
        '7': 'Semana_04_EjemplosMundoReal_POO/Ejemplos del Mundo Real y Características de la Programación Orientada a Objetos.py',
        '8': 'SEMANA_05_Tipos de datos, Identificadores/Programa para calcular el área de un círculo.py',
        '9': 'Semana 06_Tarea_Clases_objetos_herencia_ encapsulamiento y polimorfismo/Tarea_Aplicación de Conceptos de POO en Python.py',
        '10': 'Semana 07_Tarea_Constructores y Destructores/Uso de constructor.py',
        '11': 'Semana 07_Tarea_Constructores y Destructores/Uso del destructor.py',

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()