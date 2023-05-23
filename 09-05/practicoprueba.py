menu = False
Usuario = ["Admin", "Pepito"]
Contraseña = ["admin", "pepe1"]

Sesion = True


while Sesion:
    i = 0
    User = input("Ingrse su nombre de usuario\n")
    password = input("Ingrese su contraseña\n")

    for i in range(len(Usuario)):
        if User == Usuario[i] and password == Contraseña[i]:
            menu = True
            while menu:
                print("------------------------")
                print("Elige una opción")
                print("1) Test")
                print("2) Test")
                print("3) Test")
                print("4) Cerrar sessión")
                print("5) Salir del Programa")
                if User == "Admin":
                      print("6) Crear Usuario y contraseña")
                      print("7) Mostrar Usuario y Contraseña")
                print("------------------------")
                try:
                    opc = int(input("Eliga una opcion\n"))
                    if opc == 1:
                            print("Test 1")
                    elif opc == 2:
                            print("Test 2")
                    elif opc == 3:
                            print("Test 3")
                    elif opc == 4:
                            print("Cerro sessión")
                            menu = False
                    elif opc == 5:
                            print("Salio del Programa")
                            menu = False
                            Sesion = False
                    elif opc == 6 and User == "Admin":
                          usernuevo = input("Ingrese un usuario nuevo: \n")
                          passnueva = input("Ingrese una contraseña nueva: \n")
                          Usuario.append(usernuevo)
                          Contraseña.append(passnueva)
                          print(usernuevo)
                          print(passnueva)
                    elif opc == 6:
                          print("Ingrese un numero valido entre las opciones mostrada")
                    elif opc == 7 and User == "Admin":
                          print(Usuario)
                          print(Contraseña)
                    elif opc == 7:
                          print("Ingrese un numero valido entre las opciones mostrada")
                    else:
                        print("Ingrese un numero valido entre las opciones mostrada")
                except ValueError:
                    print("!!!!!!!!!!!!!!!!")
                    print("Ingrese numeros")
                    print("!!!!!!!!!!!!!!!!")
        else:
             print("Datos no valido")
print("Gracias por usar nuestro programa informatico")