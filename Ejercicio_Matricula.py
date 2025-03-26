import datetime
i = 1
while i <= 999:
    fecha = datetime.datetime.now()
    año = datetime.datetime.strftime(fecha, "%Y")
    periodo = int(input("Elige 1 si eres de otra escuela o elige 2 si eres de admision tec: "))
    carreras = [
        "Ing.Industrial",
        "TICS",
        "Ing.Sistemas Computacionales",
        "Ing.Química",
        "Ing.Civil",
        "Ing.Mecatrónica",
        "Ing.Electrica",
        "Ing.Logistica",
        "Lic.Administración"]
    print("Selecciona el número de la carrera que deseas elegir:")
    for numero_carrera, nombre_carrera in enumerate(carreras, start=1):
        print(f"{numero_carrera}. {nombre_carrera}")
    seleccion = int(input("Ingresa el número de tu carrera elegida: "))
    if 1 <= seleccion <= 9:
        print(f"Tu matricula es la siguente: {año}{periodo}{seleccion}{i:03}")
    print("***********************************************************************************")
    i += 1