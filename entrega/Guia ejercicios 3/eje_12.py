n = int(input("Ingrese un numero natural N: "))
suma = 0
for i in range(1, n + 1):
    suma += i
print("La suma de los numeros naturales desde 1 hasta", n, "es:")
for i in range(1, n):
    print(i, "+", end=" ")
print(n, "=", suma)