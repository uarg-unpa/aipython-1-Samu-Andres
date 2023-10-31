import math

# Calcular el área y el perímetro de un rectángulo
def calcular_rectangulo(base, altura):
    area_rectangulo = base * altura
    perimetro_rectangulo = 2 * (base + altura)
    return area_rectangulo, perimetro_rectangulo

# Calcular el área y la circunferencia de una circunferencia
def calcular_circunferencia(radio):
    area_circunferencia = math.pi * radio ** 2
    circunferencia = 2 * math.pi * radio
    return area_circunferencia, circunferencia

# Solicitar al usuario qué figura desea calcular
figura = input("¿Qué figura deseas calcular (rectángulo/circunferencia)? ").lower()

if figura == "rectangulo":
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    area, perimetro = calcular_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area}")
    print(f"El perímetro del rectángulo es: {perimetro}")
elif figura == "circunferencia":
    radio = float(input("Ingresa el radio de la circunferencia: "))
    area, circunferencia = calcular_circunferencia(radio)
    print(f"El área de la circunferencia es: {area}")
    print(f"La circunferencia de la circunferencia es: {circunferencia}")
else:
    print("Figura no reconocida. Por favor, ingresa 'rectangulo' o 'circunferencia'.")
