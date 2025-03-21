#Semana 14 Tarea: Componentes y contenedores
#Tarea: Creación de una Aplicación de Agenda Personal
# AGENDA TKINTER
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class AgendaPersonal:
    def __init__(self, root):
        # Configurar la ventana principal
        self.root = root
        self.root.title("AGENDA PERSONAL DE MARÍA VERA")
        self.root.geometry("550x450")
        self.root.configure(bg="#F5DEB3")  # Color de fondo de la ventana

        # Estilos para los botones y tabla
        self.style = ttk.Style()
        self.style.configure("Yellow.TButton", background="#FFD700", foreground="black")

        # Frame para la tabla
        self.frame_tree = ttk.Frame(self.root)
        self.frame_tree.pack(pady=10)

        # Crear la tabla Treeview
        self.tree = ttk.Treeview(self.frame_tree, columns=("FECHA", "HORA", "DESCRIPCIÓN"), show="headings")
        self.tree.heading("FECHA", text="FECHA")
        self.tree.heading("HORA", text="HORA")
        self.tree.heading("DESCRIPCIÓN", text="DESCRIPCIÓN")

        # Aplicar color de fondo a las filas
        self.tree.tag_configure("color_fondo", background="#FFFACD")  # Amarillo claro
        self.tree.pack()

        # Frame para la entrada de datos
        self.frame_input = ttk.Frame(self.root)
        self.frame_input.pack(pady=10)

        # Labels y campos de entrada
        ttk.Label(self.frame_input, text="Fecha :").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_fecha = ttk.Entry(self.frame_input)
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_input, text="Hora :").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_hora = ttk.Entry(self.frame_input)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_desc = ttk.Entry(self.frame_input)
        self.entry_desc.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

        # Frame para los botones
        self.frame_buttons = ttk.Frame(self.root)
        self.frame_buttons.pack(pady=10)

        # Botón "Agregar Evento"
        self.btn_agregar = ttk.Button(self.frame_buttons, text="AGREGAR EVENTO", style="Yellow.TButton",
                                      command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0, padx=5, pady=5)

        # Botón "Eliminar Evento Seleccionado"
        self.btn_eliminar = ttk.Button(self.frame_buttons, text="ELIMINAR EVENTO", style="Yellow.TButton",
                                       command=self.eliminar_evento)
        self.btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

        # Botón "Salir"
        self.btn_salir = ttk.Button(self.frame_buttons, text="SALIR", style="Yellow.TButton",
                                    command=self.root.quit)
        self.btn_salir.grid(row=0, column=2, padx=5, pady=5)

    # Función para agregar eventos a la lista
    def agregar_evento(self):
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_desc.get().strip()

        if not fecha or not hora or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Validar el formato de fecha
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use YYYY-MM-DD.")
            return

        # Validar el formato de hora
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato de hora incorrecto. Use HH:MM (24h).")
            return

        # Insertar el evento con color de fondo
        self.tree.insert("", "end", values=(fecha, hora, descripcion), tags=("color_fondo",))
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    # Función para eliminar eventos
    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            if messagebox.askyesno("Confirmación", "¿Está seguro de eliminar este evento?"):
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")


# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
