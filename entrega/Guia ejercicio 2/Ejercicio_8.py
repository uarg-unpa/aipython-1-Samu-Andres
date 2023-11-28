# Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de entrada según la edad
if edad < 4:
    precio_entrada = 0
elif edad >= 4 and edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

# Imprimir el precio de entrada
print(f"El precio de entrada es: ${precio_entrada}")