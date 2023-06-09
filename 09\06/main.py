from funcionessss import *
main = True
while main:
    menu()
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            try:
                compra = int(input("Ingrese el valor de su compra: "))
                IVA19(compra)
            except ValueError:
                print("Ingrese un numero valido")
        elif opc == 2:
            try:
                compra = int(input("Ingrese el valor de su compra: "))
                descuento30(compra)
            except ValueError:
                print("Ingrese un numero valido")   
        elif opc == 3:
            try:
                peso = float(input("Ingrese su Peso en Kilos: "))
                altura = float(input("Ingrese su Altura en Metros: "))
                IMCc(peso, altura)
            except ValueError:
                print("Ingrese un numero valido")
        elif opc == 4:
            print("Saliendo...")
            main = False
        else:
            print("Ingrese un numero valido")
    except ValueError:
        print("Ingrese un numero porfavor")
print("Salio del Programa")
