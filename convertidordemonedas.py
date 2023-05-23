ConvDolarA = 536.64
ConvArs = 3.70
ConvYen = 5.95

print("Convertidor a Pesos Chilenos")
print("Eliga la moneda que desea convertir")
print("1. Dolar Australiano")
print("2. Peso Argentino")
print("3. Yen Japones")
opcion = int(input("Ingrese la opcion: \n"))
if opcion == 1:
    DolarA = float(input("Ingrese la cantidad de dolares australianos: \n"))
    print("El valor en pesos chilenos es:", DolarA * ConvDolarA)
elif opcion == 2:
    Ars = float(input("Ingrese la cantidad de pesos argentinos: \n"))
    print("El valor en pesos chilenos es:", Ars * ConvArs)
elif opcion == 3:
    Yen = float(input("Ingrese la cantidad de yenes japoneses: \n"))
    print("El valor en pesos chilenos es:", Yen * ConvYen)