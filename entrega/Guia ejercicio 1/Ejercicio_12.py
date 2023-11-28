# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

# Solicitar la cantidad a invertir al usuario
cantidad_invertir = float(input("Ingresa la cantidad a invertir: "))

# Solicitar el interés anual al usuario
interes_anual = float(input("Ingresa el interés anual en porcentaje: "))

# Convertir el interés anual a tasa decimal
tasa_interes = interes_anual / 100

# Solicitar el número de años de la inversión
num_anios = int(input("Ingresa el número de años de la inversión: "))

# Calcular el capital obtenido en la inversión
capital_obtenido = cantidad_invertir * (1 + tasa_interes)**num_anios

# Mostrar el capital obtenido por pantalla
print(
    f"El capital obtenido en la inversión después de {num_anios} años es: ${capital_obtenido:.2f}")