# Escribir un programa que calcule el promedio de precios de 10 productos.

# Inicializar una lista para almacenar los precios de los productos
precios = []

# Solicitar al usuario ingresar los precios de los 10 productos
for i in range(1, 11):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    precios.append(precio)

# Calcular el promedio de precios
total = sum(precios)
promedio = total / 10  # Dividir entre 10, el número de productos

# Mostrar el promedio de precios por pantalla
print(f"El promedio de precios de los 10 productos es: ${promedio:.2f}")