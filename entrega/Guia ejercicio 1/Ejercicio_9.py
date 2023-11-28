# Solicitar al usuario su peso en kilogramos y estatura en metros
peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
estatura = float(input("Por favor, ingresa tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el resultado
print("Tu índice de masa corporal es:", imc)
