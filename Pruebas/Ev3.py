from Ev3Func import *
Lista_Rut = [20626765,12345678]
Lista_Nombre = ["Nico","Calfun"]
Lista_ApPaterno = ["Hernandez","Picaro"]
Lista_Edad = ["21", "69"]
Lista_Fecha = ["12/12/2012", "09/11/2001"]

menun = True
minimenun = True
while menun:
    menu()
    try:
        opc = int(input("Ingrese una opción: "))
        if opc == 1:
            try:
                Rut = int(input("Ingrese su rut sin dv (12345678 si comienza con 9 millones o inferior poner un 0): ")) 
            except ValueError:
                print("Ingrese un rut valido.")
            Nombre = input("Ingrese su nombre: ")  
            Apellido_Paterno = input("Ingrese su Apellido Paterno: ")
            Edad = int(input("Ingrese su edad: "))
            Fecha_Afiliacion = input("Ingrese su fecha de Aficiliacion (DD/MM/AAAA): ")
            grabar(Rut, Nombre, Apellido_Paterno, Edad, Fecha_Afiliacion, Lista_Rut, Lista_Nombre, Lista_ApPaterno, Lista_Edad, Lista_Fecha)
        elif opc == 2:
            Rut = int(input("Ingrese un rut para buscar su informacion: "))
            buscar(Rut,Lista_Rut, Lista_Nombre, Lista_ApPaterno, Lista_Edad, Lista_Fecha)
        elif opc == 3:
            Rut = int(input("Ingrese un rut para su certificado: "))
            minimenu()
            opc2 = int(input("Ingrese una opción: "))
            Imprimir(opc2,Rut,Lista_Rut, Lista_Nombre, Lista_ApPaterno, Lista_Edad, Lista_Fecha)
        elif opc == 4:
            menun = False
        else:
            print("Ingrese un numero valido")
    except ValueError:
        print("Ingrese porfavor un numero")
        
print("Saliste del bucle bro")