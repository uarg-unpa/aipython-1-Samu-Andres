# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora. Después debe mostrar por pantalla el sueldo que le corresponde.

# Solicitar el número de horas trabajadas al usuario
horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))

# Solicitar el costo por hora al usuario
costo_por_hora = float(input("Ingresa el costo por hora: "))

# Calcular el sueldo
sueldo = horas_trabajadas * costo_por_hora

# Mostrar el sueldo por pantalla
print(f"El sueldo correspondiente es: ${sueldo:.2f}")