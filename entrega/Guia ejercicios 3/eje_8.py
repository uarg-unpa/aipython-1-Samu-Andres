# ejer8

while True:
    numero = int(input("Ingrese un número entero positivo mayor a 3: "))
    if numero > 3:
        break
    else:
        print("El número debe ser mayor a 3. Inténtelo nuevamente.")
for i in range(1, numero + 1, 2):
    print(i)