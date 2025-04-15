def calcular_division():
    try:
        numerador = int(input("Ingresa el numerador: "))
        denominador = int(input("Ingresa el denominador: "))
        
        resultado = numerador / denominador
        print(f"El resultado de la división es: {resultado}")
    
    except ZeroDivisionError:
        print("Error: No puedes dividir entre cero.")
    
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    finally:
        print("Fin del cálculo.")

calcular_division()
