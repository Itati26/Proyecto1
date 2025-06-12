import math

def calcular_z(a, b):
    z_cuadrado = a**2 + b**2
    z = math.sqrt(z_cuadrado)
    return z, z_cuadrado
  
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))

z, z_cuadrado = calcular_z(a, b)

print(f"z^2 = {z_cuadrado}")
print(f"z = {z}")
