num = int(input("Ingrese un numero entero: "))
current = 1
for i in range(1, num + 1, 2):
    for j in range(1, 0, -2):
        print(j, end=" ")
    print()