n = int(input("Ingrese un número natural N: "))
suma = 0
for i in range(2, 2 * n + 1, 2):
    suma += i
print("La suma de los primeros", n, "números pares es:", suma)