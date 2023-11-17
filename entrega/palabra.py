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

def buscarSimbolo(palabra,simbolo):
    for i in range(len(palabra)):
        if palabra[i]==simbolo:
            return  True
    return False

def invertirPalabra(palabra):
    invertida=""
    for i in range(len(palabra)-1,-1,-1):
        invertida+=palabra[i]
    return invertida


def main():
    while True:
        palabra = input("Ingrese una palabra: ")
        print("1: Mostrar Caracteres ")
        print("2: Contar Vocales")
        print("3: Contar Consonantes")
        print("4: Buscar Simbolo")
        print("5: Invertir Palabra")
        op=int(input("Ingrese una opcion: "))
        if op==1:
            mostrarCarac(palabra)
        elif op==2:
            print(f"Cantidad de vocales en {palabra} es {contarVocales(palabra)}")
        elif op==3:
            print(f"Cantidad de consonantes en {palabra} es {contarCons(palabra)}")
        elif op==4:
            simbolo=input("Ingrese para buscar: ")
            if buscarSimbolo(palabra,simbolo):
                print(f"El simbolo {simbolo} se encuentra en {palabra}")
            else:
                print(f"El simbolo {simbolo} no se encuentra en {palabra}")
        elif op==5:
            inveritda=invertirPalabra(palabra)
            print(inveritda)
        else:
            print("Parece no haber ingresado una opcion disponible")
        cont=input("Desea continuar? S/N: ")
        if cont=='s' or cont=='S':
            continue
        else:
            break
    print("Finalizado")

main()