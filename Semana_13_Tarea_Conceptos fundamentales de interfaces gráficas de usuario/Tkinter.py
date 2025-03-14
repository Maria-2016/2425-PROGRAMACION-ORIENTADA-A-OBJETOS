# (Semana 13) Tarea: Conceptos fundamentales de interfaces gráficas de usuario
# Tarea: Creación de una Aplicación GUI Básica
import tkinter as tk
from tkinter import messagebox


class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Tarea: Creación de una Aplicación GUI Básica")
        self.ventana.geometry("400x300")

        # Configuración de la ventana
        self.etiqueta = tk.Label(ventana, text="Ingrese un dato:")
        self.etiqueta.pack(pady=5)

        # Entrada de texto
        self.campo_texto = tk.Entry(ventana, width=40)
        self.campo_texto.pack(pady=5)

        # Agregar botón
        self.boton_agregar = tk.Button(ventana, text="GUARDAR",background="Yellow", command=self.agregar_elemento)
        self.boton_agregar.pack(pady=5)

        # Lista
        self.lista_datos = tk.Listbox(ventana, width=50, height=10)
        self.lista_datos.pack(pady=5)

        # Botón para limpiar
        self.boton_limpiar = tk.Button(ventana, text="LIMPIAR", background="Skyblue", command=self.limpiar_elementos)
        self.boton_limpiar.pack(pady=5)

    def agregar_elemento(self):
        elemento = self.campo_texto.get().strip()
        if elemento:
            self.lista_datos.insert(tk.END, elemento)
            self.campo_texto.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede agregar un valor vacío.")

    def limpiar_elementos(self):
        self.lista_datos.delete(0, tk.END)


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
