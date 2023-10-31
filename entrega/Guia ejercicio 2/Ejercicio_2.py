# Solicitar la edad del usuario
edad_usuario = int(input("Ingrese su edad: "))

# Definir mi edad
mi_edad = 30  # Cambia esto a la edad que desees

# Comparar edades
if edad_usuario < mi_edad:
    diferencia = mi_edad - edad_usuario
    if diferencia == 1:
        print("Soy mayor que tú por 1 año.")
    else:
        print(f"Soy mayor que tú por {diferencia} años.")
elif edad_usuario > mi_edad:
    diferencia = edad_usuario - mi_edad
    if diferencia == 1:
        print("Eres mayor que yo por 1 año.")
    else:
        print(f"Eres mayor que yo por {diferencia} años.")
else:
    print("Tenemos la misma edad. ¡Somos compañeros en la juventud!")
