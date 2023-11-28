
puntuacion = int(input("Ingrese la puntuación del estudiante: "))

if puntuacion >= 80 and puntuacion <= 100:
    clasificacion = "A"
elif puntuacion >= 70 and puntuacion < 80:
    clasificacion = "B"
elif puntuacion >= 60 and puntuacion < 70:
    clasificacion = "C"
elif puntuacion >= 50 and puntuacion < 60:
    clasificacion = "D"
elif puntuacion >= 0 and puntuacion < 50:
    clasificacion = "F"
else:
    clasificacion = "Puntuación no válida"

print(f"La clasificación del estudiante es: {clasificacion}")
