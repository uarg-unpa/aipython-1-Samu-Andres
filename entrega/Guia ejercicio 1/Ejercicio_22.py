# Cortar las dos primeras palabras de la frase ‘’El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio”.

frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio."

palabras = frase.split()

nuevas_palabras = palabras[2:]

nueva_frase = ' '.join(nuevas_palabras)

print(nueva_frase)
