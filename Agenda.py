import tkinter as tk

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda")

        self.label = tk.Label(root, text="Agenda Simple", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Guardar", width=10)
        self.button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
