# Obtener dos números del usuario
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

# Comparar los números y mostrar el resultado
if a > b:
    print(f"{a} es mayor que {b}.")
elif a < b:
    print(f"{a} es menor que {b}.")
else:
    print(f"{a} es igual a {b}.")
