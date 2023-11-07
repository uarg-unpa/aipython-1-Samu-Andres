numero = int(input("Ingrese un número entero: "))
es_primo = True
if numero <= 1:
    es_primo = False
elif numero <= 3:
    es_primo = True
elif numero % 2 == 0 or numero % 3 == 0:
    es_primo = False
else:
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            es_primo = False
            break
        i += 6

if es_primo:
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
