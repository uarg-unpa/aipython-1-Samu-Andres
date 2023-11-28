# 1-declarar una lista vacia
lista_vacia = []

# 2-Declarar una lista con más de 7 elementos.
lista_mas_siete = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3-Mostrar la longitud de una lista creada
lista = [5, 10, 15, 20, 25, 30, 35]
longitud = len(lista)
print("La longitud de la lista es:", longitud)

# 4-Crear una lista de tus frutas favoritas
# A-Imprimir la longitud de la lista
# B-Eliminar el primer elemento de la lista
# C-Agregar un elemento al final de la lista
# D-Imprimir los resultados anteriores

frutas_favoritas = ["manzana", "Banana", "Naranja", "Mandarina"]

print("La longitud de la lista de frutas es:", len(frutas_favoritas))

primer_elemento_eliminado = frutas_favoritas.pop(0)

frutas_favoritas.append("Pera")

print("Primer elemento eliminado:", primer_elemento_eliminado)
print("Lista de frutas actualizada:", frutas_favoritas)

# 5-Dada una lista mostrar el primer elemento, el del medio y el último
mi_lista = [3, 6, 9, 12, 15, 18]

primer_elemento = mi_lista[0]
ultimo_elemento = mi_lista[-1]

longitud = len(mi_lista)
elemento_medio = mi_lista[longitud // 2] if longitud % 2 != 0 else (
    mi_lista[longitud // 2 - 1] + mi_lista[longitud // 2]) / 2

print("Primer elemento:", primer_elemento)
print("Elemento del medio:", elemento_medio)
print("Último elemento:", ultimo_elemento)

# 6-Declarar una lista llamada datos_personales, insertar tu nombre, edad, altura,estado civil y dirección.
datos_personales = ["Samuel", 24, 1.73, "soltero", "Velez Sarfield 1120"]

# 7-Almacenar los nombres de tus compañías favoritas en una lista dándole esos datos como inicial.
companias_favoritas = ["G", "A", "L"]  # Compañias: Google, Apple, Logitech

# 8-Recorrer la lista del ejercicio 6 y mostrar los datos con print.
datos_personales = ["Samuel", 24, 1.73, "soltero", "Velez Sarfield 1120"]

print("Datos personales:")
for dato in datos_personales:
    print(dato)

# 9-Recorrer la lista del ejercicio 6 y mostrar el índice más el nombre de la compañía.
for indice, dato in enumerate(datos_personales):
    if indice == 0:  # Nombre
        print(f"Nombre: {dato}")
    elif indice == 1:  # Edad
        print(f"Edad: {dato}")
    elif indice == 2:  # Altura
        print(f"Altura: {dato}")
    elif indice == 3:  # Estado civil
        print(f"Estado Civil: {dato}")
    elif indice == 4:  # Dirección
        print(f"Dirección: {dato}")
    elif indice < len(companias_favoritas) + 5:  # Compañías
        print(f"Compañía: {companias_favoritas[indice - 5]} - {dato}")


# 10-Modificar alguna/as de las compañía/s de la lista del ejercicio 7 y luego mostrar la lista.
companias_favoritas = ["G", "A", "M"]


companias_favoritas[1] = "F"

print("Lista de compañías actualizada:")
print(companias_favoritas)


# 11-Crear una lista de números del 1 al 10. a. Imprimir los tres primeros números utilizando rebanadas.
numeros = list(range(1, 11))
tres_primeros = numeros[:3]

print("Los tres primeros números son:", tres_primeros)


# 12-Crear una lista de letras (‘a’ hasta ‘j’) a. Imprima cada segundo elemento usando rebanadas.
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
cada_segundo = letras[::2]

print("Cada segundo elemento es:", cada_segundo)


# 13-Crear una lista a su criterio. a. Imprimir la lista en forma inversa usando rebanadas.
lista_criterio = [4, 7, 2, 9, 1, 5]
inversa = lista_criterio[::-1]

print("Lista en forma inversa:", inversa)


# 14-Crear una lista de tus palabras favoritas a. Extraer una sub lista conteniendo desde la segunda hasta la cuarta palabra.
palabras_favoritas = ['Juegos', 'Basquet',
                      'Mates', 'Viernes', 'Sabado', 'Domingo']
sublista = palabras_favoritas[1:4]

print("Sublista de la segunda a la cuarta palabra:", sublista)


# 15-Crear la siguiente lista
# flores= [rosas, orquídea,lirio,tulipan, margarita, dalia, hortensia]
# a-Mostrar tres elementos desde el tercer elemento.
# b-Mostrar los elementos en posiciones pares desde la segunda posición
# c-Mostrar todos los elementos desde la primera posición saltando de a tres elementos.

flores = ['rosas', 'orquídea', 'lirio',
          'tulipan', 'margarita', 'dalia', 'hortensia']

# A
tres_desde_tercero = flores[2:5]
print("Tres elementos desde el tercer elemento:", tres_desde_tercero)

# B
pares_desde_segundo = flores[1::2]
print("Elementos en posiciones pares desde la segunda posición:", pares_desde_segundo)

# C
saltando_tres = flores[::3]
print("Elementos desde la primera posición saltando de a tres elementos:", saltando_tres)
