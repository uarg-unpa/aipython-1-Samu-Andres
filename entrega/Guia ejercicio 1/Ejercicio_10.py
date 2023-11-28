# Escribir un programa que pida una temperatura en grados Celsius al usuario, realice la transformación de grados Celsius a Fahrenheit e imprima el resultado por pantalla.

# Solicitar la temperatura en grados Celsius al usuario
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Realizar la conversión de grados Celsius a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Imprimir el resultado por pantalla
print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")