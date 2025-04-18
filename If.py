edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Eres un niño.")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente.")
elif edad >= 18 and edad < 30:
    print("Eres un joven adulto.")
elif edad >= 30 and edad < 65:
    print("Eres un adulto.")
elif edad >= 65 and edad < 80:
    print("Eres un adulto mayor.")
else:
    print("Eres una persona de edad avanzada.")

print("¡Gracias por compartir tu edad!")
