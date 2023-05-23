menu = True
while menu == True:
        print("------------------------")
        print("Elige una opción")
        print("1) Test")
        print("2) Test")
        print("3) Test")
        print("4) Salir")
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
                    print("Salio")
                    menu = False
            else:
                print("Ingrese un numero valido entre las opciones mostrada")
        except ValueError:
            print("!!!!!!!!!!!!!!!!")
            print("Ingrese numeros")
            print("!!!!!!!!!!!!!!!!")