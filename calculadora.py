import tkinter as tk

# Función que actualiza la pantalla de la calculadora
def actualizar_pantalla(valor):
    pantalla_var.set(pantalla_var.get() + str(valor))

# Función que realiza el cálculo de la operación
def calcular():
    try:
        resultado = eval(pantalla_var.get())
        pantalla_var.set(resultado)
    except Exception as e:
        pantalla_var.set("Error")

# Función que borra el contenido de la pantalla
def borrar():
    pantalla_var.set("")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variable que almacenará el contenido de la pantalla
pantalla_var = tk.StringVar()

# Crear la pantalla donde se mostrarán los resultados
pantalla = tk.Entry(ventana, textvar=pantalla_var, font=("Arial", 20), bd=10, relief="sunken", width=20, justify="right")
pantalla.grid(row=0, column=0, columnspan=4)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Crear los botones dinámicamente
for texto, fila, columna in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, font=("Arial", 20), bd=5, command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, font=("Arial", 20), bd=5, command=lambda valor=texto: actualizar_pantalla(valor))
    boton.grid(row=fila, column=columna, sticky="nsew")

# Botón de borrar
boton_borrar = tk.Button(ventana, text='C', font=("Arial", 20), bd=5, command=borrar)
boton_borrar.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Hacer que los botones se expandan para llenar el espacio disponible
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for j in range(4):
    ventana.grid_columnconfigure(j, weight=1)

# Ejecutar la ventana
ventana.mainloop()
