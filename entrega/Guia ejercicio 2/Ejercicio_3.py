# Solicitar al usuario una contraseña
contrasena_guardada = "pedroELPERRO"  # Cambia esto a tu contraseña guardada
contrasena_usuario = input("Ingrese su contraseña: ")

# Convertir ambas contraseñas a minúsculas y comparar
if contrasena_guardada.lower() == contrasena_usuario.lower():
    print("¡La contraseña coincide!")
else:
    print("La contraseña no coincide.")
