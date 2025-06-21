import tkinter as tk

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda")

        # Título
        self.label = tk.Label(root, text="Agenda Personal", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botón para guardar (sin funcionalidad)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.btn_guardar = tk.Button(self.button_frame, text="Guardar", width=12)
        self.btn_guardar.pack(side="left", padx=5)

        self.btn_borrar = tk.Button(self.button_frame, text="Borrar", width=12)
        self.btn_borrar.pack(side="left", padx=5)

        # Lista para mostrar entradas (aún sin funcionalidades)
        self.lista = tk.Listbox(root, width=50, height=8)
        self.lista.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
