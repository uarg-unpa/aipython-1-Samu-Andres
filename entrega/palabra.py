def mostrarCarac(palabra):
    for i in range(len(palabra)):
        print(palabra[i])

def contarVocales(palabra):
    cant = 0
    for i in range(len(palabra)):
        if palabra[i] == 'a' or palabra[i] == 'e' or palabra[i] == 'i' or palabra[i] == 'o' or palabra[i] == 'u':
            cant = cant+1
    return cant

def contarCons(palabra):
    cant=0
    for letra in palabra:
        if letra !='a' and letra!='e' and letra!='i' and letra!='o' and letra!='u':
            cant+=1
    return cant

def main():
    while True:
        palabra = input("Ingrese una palabra: ")
        print("1: Mostrar Caracteres ")
        print("2: Contar Vocales")
        print("3: Contar Consonantes")
        op=int(input("Ingrese una opcion: "))
        if op==1:
            mostrarCarac(palabra)
        elif op==2:
            print(f"Cantidad de vocales en {palabra} es {contarVocales(palabra)}")
        elif op==3:
            print("Cantidad de consonantes en {palabra} es {contarCons(palabra)}")
        else:
            print("Parece no haber ingresado una opcion disponible")
        cont=input("Desea continuar? S/N: ")
        if cont=='s' or cont=='S':
            continue
        else:
            break
print("Fin del programa")
