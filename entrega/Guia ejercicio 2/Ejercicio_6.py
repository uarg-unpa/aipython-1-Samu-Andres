# Obtener un número entero del usuario
numero = int(input("Introduce un número entero del 1 al 7: "))

# Verificar si el número está en el rango [1, 7]
if 1 <= numero <= 7:
    # Usar una lista para mapear los números a los días de la semana
    dias_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    
    # Mostrar el día correspondiente
    dia_correspondiente = dias_semana[numero]
    print(f"El número {numero} corresponde a {dia_correspondiente}.")
else:
    print("El número debe estar en el rango del 1 al 7.")
