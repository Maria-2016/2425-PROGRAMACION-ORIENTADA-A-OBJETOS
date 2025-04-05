# (Semana 16) Tarea: Manejadores de eventos
# Tarea: Aplicación GUI para Gestión de Tareas con Atajos de Teclado
# Objetivo: Desarrollar una aplicación GUI que permita a los usuarios
# gestionar una lista de tareas pendientes. La aplicación deberá permitir
# añadir nuevas tareas, marcar tareas como completadas, y eliminar tareas
# utilizando tanto la interfaz gráfica (clics de botón) como atajos de teclado.

import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")
root.configure(bg="#FFDAB9")  # Color piel (peach puff)

# Lista para almacenar las tareas
tareas = []

# Función para añadir una tarea
def agregar_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        tareas.append({"texto": tarea, "completada": False})
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

# Función para marcar una tarea como completada
def completar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        texto = lista_tareas.get(index)
        if not texto.startswith("✔️ "):
            lista_tareas.delete(index)
            lista_tareas.insert(index, "✔️ " + texto)
            lista_tareas.itemconfig(index, fg="gray")

# Función para eliminar una tarea
def eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        lista_tareas.delete(index)

# Función para cerrar la aplicación
def cerrar_aplicacion(event=None):
    root.destroy()

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(root, font=("Arial", 14))
entrada_tarea.pack(pady=10)
entrada_tarea.focus()

# Botón para añadir tarea
btn_agregar = tk.Button(root, text="AÑADIR TAREA", command=agregar_tarea, bg="yellow")
btn_agregar.pack(pady=5)

# Botón para completar tarea
btn_completar = tk.Button(root, text="COMPLETAR TAREA", command=completar_tarea, bg="yellow")
btn_completar.pack(pady=5)

# Botón para eliminar tarea
btn_eliminar = tk.Button(root, text="ELIMINAR TAREA", command=eliminar_tarea, bg="yellow")
btn_eliminar.pack(pady=5)

# Lista para mostrar las tareas
lista_tareas = tk.Listbox(root, font=("Arial", 12), selectbackground="lightblue")
lista_tareas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Atajos de teclado
root.bind("<Return>", agregar_tarea)      # Enter para añadir tarea
root.bind("<c>", completar_tarea)         # 'c' para completar tarea
root.bind("<C>", completar_tarea)         # 'C' mayúscula también
root.bind("<d>", eliminar_tarea)          # 'd' para eliminar tarea
root.bind("<D>", eliminar_tarea)          # 'D' mayúscula también
root.bind("<Delete>", eliminar_tarea)     # Tecla Delete para eliminar
root.bind("<Escape>", cerrar_aplicacion)  # Escape para cerrar

# Iniciar el bucle principal de la aplicación
root.mainloop()
