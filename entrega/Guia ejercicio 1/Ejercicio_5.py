# Utilizando la función input
# a.
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Ahora, ingresa tu apellido: ")
edad = input("Finalmente, ingresa tu edad: ")

mensaje_creativo = f"Hola {nombre} {apellido}, ¡ser creativo a los {edad} años es genial!"
print(mensaje_creativo)

# b. 

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Ahora, ingresa tu apellido: ")
edad = input("Finalmente, ingresa tu edad: ")


mensaje_creativo = "Hola {}, ¡ser creativo a los {} años es genial!".format(nombre, edad)


print(mensaje_creativo)