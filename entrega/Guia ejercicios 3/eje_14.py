numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))


menor = min(numero1, numero2)
mayor = max(numero1, numero2)


print("Números pares entre", menor, "y", mayor, ":")

for numero in range(menor, mayor + 1):
    if numero % 2 == 0:
        print(numero)
