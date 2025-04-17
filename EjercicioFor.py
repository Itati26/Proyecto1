matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma_total = 0

for fila in matriz:
    for elemento in fila:
        suma_total += elemento

print(f"La suma de todos los elementos en la matriz es: {suma_total}")
