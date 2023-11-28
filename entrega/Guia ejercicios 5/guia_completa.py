# 1. Escribir una función que tome dos números y retorne la multiplicación entre ellos.
def multiplicacion(a, b):
    return a * b


resultado = multiplicacion(5, 10)
print("El resultado es:", resultado)


# 2. Modificar el ejercicio uno, en caso de que la invocación sea sin argumentos retorna siempre el producto de 1*1.
def multiplicacion(a=1, b=1):
    return a * b


resultado_con_argumentos = multiplicacion(5, 10)
resultado_sin_argumentos = multiplicacion()  # Retorna 1 * 1 por defecto

print("Con argumentos:", resultado_con_argumentos)
print("Sin argumentos:", resultado_sin_argumentos)


# 3. Crear una función que tome un nombre como parámetro y retorna un mensaje creativo.
def mensaje_creativo(nombre):
    return f"¡Hola, {nombre}! Espero que tengas un día fantástico."


nombre_usuario = "Carlos"
mensaje = mensaje_creativo(nombre_usuario)
print(mensaje)


# 4. Escribir una función que tome un número como entrada e imprima la tabla de multiplicar del 1 al 10, con el siguiente formato. # A- 4 x 1 = 4
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


tabla_multiplicar(4)


# 5. Implementar una función que determine si dado un número este es par o impar.
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return f"{numero} es un número par."
    else:
        return f"{numero} es un número impar."


resultado = es_par_o_impar(7)
print(resultado)


# 6. Crear una función que calcule el factorial de un número.
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


num = 5
factorial_de_num = factorial(num)
print(f"El factorial de {num} es: {factorial_de_num}")


# 7. Escribir una función que tome tres números como entrada y retorna el máximo.
def maximo_de_tres(a, b, c):
    return max(a, b, c)


resultado = maximo_de_tres(15, 8, 21)
print("El máximo es:", resultado)


# 8. Implementar una función que invierta un string. hola aloh
def invertir_string(cadena):
    return cadena[::-1]


texto = "hola"
texto_invertido = invertir_string(texto)
print("Texto invertido:", texto_invertido)


# 9. Escriba una función que multiplique los elementos de una lista de números.
def multiplicar_lista(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado


numeros = [2, 3, 4, 5]
resultado = multiplicar_lista(numeros)
print("El resultado de la multiplicación es:", resultado)


# 10. Crear una función que tome un string como parámetro y verifique si es un palíndromo. Ejemplo: Arenera, Narran. etc.
def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


palabra = "Arenera"
resultado = es_palindromo(palabra)
if resultado:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")


# 11. Implementar una función que convierte temperaturas de fahrenheit a celsius.
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


temp_fahrenheit = 98.6
temp_celsius = fahrenheit_a_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit} grados Fahrenheit son {temp_celsius:.2f} grados Celsius")


# 12. Escribir una función que dada una lista de caracteres cuente la cantidad de vocales y retorne esa información.
def contar_vocales(lista):
    vocales = 'aeiouAEIOU'
    cantidad_vocales = 0
    for caracter in lista:
        if caracter in vocales:
            cantidad_vocales += 1
    return cantidad_vocales


caracteres = ['a', 'b', 'c', 'e', 'i', 'f', 'O']
cantidad = contar_vocales(caracteres)
print(f"La cantidad de vocales en la lista es: {cantidad}")


# 13. Escribir una función que tome dos listas como parámetros y las intercale en una nueva, retornar la nueva lista resultante.
def intercalar_listas(lista1, lista2):
    nueva_lista = []
    for elemento1, elemento2 in zip(lista1, lista2):
        nueva_lista.append(elemento1)
        nueva_lista.append(elemento2)
    return nueva_lista


lista_a = [1, 3, 5]
lista_b = [2, 4, 6]
resultado = intercalar_listas(lista_a, lista_b)
print("La lista intercalada es:", resultado)


# 14. Implementar una función que tome una lista de números y retorna el promedio de sus elementos.
def promedio_lista(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


lista_numeros = [5, 8, 12, 3, 9]
promedio = promedio_lista(lista_numeros)
print("El promedio de la lista es:", promedio)
