# Solicitar al usuario que ingrese su edad y sus ingresos mensuales
edad = int(input("Ingrese su edad: "))
ingresos_mensuales = float(
    input("Ingrese sus ingresos mensuales en dólares: "))

# Comprobar si el usuario debe pagar el impuesto
if edad > 18 and ingresos_mensuales >= 100000:
    debe_pagar_impuesto = True
else:
    debe_pagar_impuesto = False

# Imprimir el resultado
if debe_pagar_impuesto:
    print("Usted debe pagar el impuesto.")
else:
    print("Usted no tiene que pagar el impuesto.")
