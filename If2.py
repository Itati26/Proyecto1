def evaluar_numero(num):
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

def clasificar_edad(edad):
    if edad < 18:
        print("Eres menor de edad.")
    elif 18 <= edad < 65:
        print("Eres adulto.")
    else:
        print("Eres adulto mayor.")

def calcular_descuento(precio, cliente_frecuente):
    if precio > 100:
        descuento = 20 if cliente_frecuente else 10
    elif precio > 50:
        descuento = 10 if cliente_frecuente else 5
    else:
        descuento = 5 if cliente_frecuente else 0
    print(f"Descuento aplicado: {descuento}%")

numero = int(input("Introduce un número: "))
evaluar_numero(numero)

edad = int(input("Introduce tu edad: "))
clasificar_edad(edad)

precio = float(input("Introduce el precio del producto: "))
cliente_frecuente = input("¿Eres cliente frecuente? (sí/no): ").strip().lower() == "sí"
calcular_descuento(precio, cliente_frecuente)
