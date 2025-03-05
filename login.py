import tkinter as tk
from tkinter import messagebox

# Diccionario de usuarios y contraseñas
usuarios = {
    "user1": "contraseña1",
    "user2": "contra2",
    "user3": "contra3"
}

def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    # Verificar si el usuario y la contraseña son correctos
    if usuario in usuarios and usuarios[usuario] == contraseña:
        messagebox.showinfo("Acceso concedido", "¡Bienvenido al sistema!")
    else:
        messagebox.showerror("Acceso denegado", "Nombre de usuario o contraseña incorrectos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Login")

# Etiquetas y campos de texto
label_usuario = tk.Label(ventana, text="Nombre de usuario:")
label_usuario.pack(pady=5)

entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack(pady=5)

entry_contraseña = tk.Entry(ventana, show="*")  # `show="*"` oculta la contraseña
entry_contraseña.pack(pady=5)

# Botón de login
boton_login = tk.Button(ventana, text="Iniciar sesión", command=verificar_login)
boton_login.pack(pady=10)

# Ejecutar la interfaz gráfica
ventana.mainloop()

