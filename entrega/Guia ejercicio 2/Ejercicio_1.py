# Solicitar la edad del usuario
edad = int(input("Ingrese su edad: "))

# Comprobar si el usuario tiene 18 años o más
if edad >= 18:
    print("Tiene edad suficiente para conducir.")
else:
    # Calcular cuántos años faltan para llegar a los 18 años
    años_faltantes = 18 - edad
    print(f"Le faltan {años_faltantes} años para tener la edad suficiente para conducir.")
