dolar_peso  = 794.43 
peso_dolar = 0.0013
clp_ars = 3.64

print("Convertidor de monedas")
print("Elija la moneda que desea convertir")
print("1. Dolar a Pesos chilenos")
print("2. Pesos chilenos a Dolar")
print("3. Peso Argentino a Peso Chileno")
opcion = int(input("Ingrese la opcion: \n"))
if opcion == 1:
    Dolar = float(input("Ingrese la cantidad de dolares a cambiar a pesos chilenos: \n"))
    print("El valor en pesos chilenos es:", round(Dolar * dolar_peso))
elif opcion == 2:
    clp = int(input("Ingrese la cantidad de pesos chilenos a cambiar a dolar: \n"))
    print("El valor en dolar es:", clp * peso_dolar)
elif opcion == 3:
    ars = float(input("Ingrese la cantidad de pesos argentinos a cambiar por pesos chilenos: \n"))
    print("El valor en pesos chilenos es:", round(ars * clp_ars))
else:
    print("Opcion valida")