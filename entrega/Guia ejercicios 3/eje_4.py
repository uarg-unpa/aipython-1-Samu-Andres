# ejer4

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

numero_min = min(numero1, numero2)
numero_max = max(numero1, numero2)

for numero in range(numero_min, numero_max + 1):
    print(numero)
