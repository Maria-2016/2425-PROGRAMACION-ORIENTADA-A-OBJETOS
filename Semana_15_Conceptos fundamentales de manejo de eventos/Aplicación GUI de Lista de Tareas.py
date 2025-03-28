# Tarea: Conceptos fundamentales de manejo de eventos
# Tarea: Aplicación GUI de Lista de Tareas

import tkinter as tk
from tkinter import messagebox


def add_task():
    """Añade una nueva tarea a la lista si el campo de entrada no está vacío."""
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task.upper())  # Agrega la tarea en mayúsculas
        entry_task.delete(0, tk.END)  # Limpia el campo de entrada después de agregar
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")


def mark_completed():
    """Marca una tarea como completada cambiando su estado visualmente."""
    try:
        selected_index = listbox_tasks.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        task = listbox_tasks.get(selected_index)

        if not task.startswith("✔ "):
            listbox_tasks.delete(selected_index)
            listbox_tasks.insert(selected_index, f"✔ {task}")  # Marca la tarea como completada
        else:
            messagebox.showinfo("Información", "Esta tarea ya está completada.")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")


def delete_task():
    """Elimina la tarea seleccionada de la lista."""
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")


def add_task_enter(event):
    """Permite añadir una tarea presionando Enter en el campo de entrada."""
    add_task()


# Configuración de la ventana principal
root = tk.Tk()
root.title("LISTA DE TAREAS DE MARIA VERA")
root.geometry("400x400")

# Campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task_enter)  # Vincula la tecla Enter para agregar tareas

# Botones de acción con color rosado
btn_add = tk.Button(root, text="AÑADIR TAREA", command=add_task, bg="#ff69b4", fg="white")
btn_add.pack(pady=5)

btn_complete = tk.Button(root, text="MARCAR COMO COMPLETADA", command=mark_completed, bg="#ff69b4", fg="white")
btn_complete.pack(pady=5)

btn_delete = tk.Button(root, text="ELIMINAR TAREA", command=delete_task, bg="#ff69b4", fg="white")
btn_delete.pack(pady=5)

# Listbox para mostrar las tareas en mayúsculas
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Iniciar el bucle de eventos de Tkinter
root.mainloop()
