UserRegistrado1 = "fcalfun" #Usuario Registrado
ContraRegistrada1 = "1234" #Contra Registrada
UserRegistrado2 = "nico" #Usuario Registrado
ContraRegistrada2 = "n" #Contra Registrada
PrecioTradicional = 12000 #Precio Pizza, constantes
PrecioPeperoni = 14000 #Precio Pizza, constantes
PrecioCarnes = 17000 #Precio Pizza, constantes
CantidadTradicional = 0 #Variable que almacena la cantidad
CantidadPeperoni = 0 #Variable que almacena la cantidad
CantidadCarnes = 0 #Variable que almacena la cantidad
TotalTradicional = 0 #Precio Total de la pizza
TotalPeperoni = 0 #Precio Total de la Pizza
TotalCarnes = 0 #Precio Total de la Pizza
SubTotal = 0 #SubTotal 
Total = 0 #Total con descuento

login = True
while login: #Ciclo de Inicio de Session que permite salir al programa si se pone en false
    user = input("Ingrese un usuario: ")
    contra = input("Ingresa su contraseña: ")
    if user == UserRegistrado1 and contra == ContraRegistrada1 or user == UserRegistrado2 and contra == ContraRegistrada2:
        menurapid = True
        while menurapid: #Menu
            print("--------------Rapid--------------")
            print("1) Ingresar una compra")
            print("2) Efectuar Compra y Boleta")
            print("3) Salir del Programa.")
            print("4) Cerrar Sesion")
            print("----------------------------")
            try: 
                opcrapid = int(input("Ingrese una opción: "))
                if opcrapid == 1:
                    menupizza = True
                    while menupizza:
                        print("--------------Rapid--------------")
                        print("1)Añadir Pizza Tradicional $12000 x Unidad")
                        print("2)Añadir Pizza Peperoni $14000 x Unidad")
                        print("3)Añadir Pizza Todo carnes $17000 x Unidad")
                        print("4) Volver al menu anterior.")
                        print("----------------------------")
                        try:
                            opcpizza = int(input("Ingrese una opcion: "))
                            if opcpizza == 1:
                                try: 
                                    CantidadTradicional = int(input("Ingrese la cantidad de Pizzas Tradicionales: "))
                                    TotalTradicional = CantidadTradicional * PrecioTradicional #Almacena el precio total de la pizza Tradicional
                                    print("Pizzas Ingresadas con exito.") #Mensaje que muestra que fueron ingresadas, si muestra otro mensaje no fueron ingresadas.
                                except ValueError:
                                    print("Ingrese un numero")
                            elif opcpizza == 2:
                                try:
                                    CantidadPeperoni = int(input("Ingrese la cantidad de Pizzas Peperoni: "))
                                    TotalPeperoni = CantidadPeperoni * PrecioPeperoni
                                    print("Pizzas Ingresadas con exito.")
                                except ValueError:
                                    print("Ingrese un numero")
                            elif opcpizza == 3:
                                try:
                                    CantidadCarnes = int(input("Ingrese la cantidad de Pizza de Todas carnes: "))
                                    TotalCarnes = CantidadCarnes * PrecioCarnes
                                    print("Pizzas Ingresadas con exito.")
                                except ValueError:
                                    print("Ingrese un numero")
                            elif opcpizza == 4:
                                menupizza = False
                                print("Volviendo al menu anterior...")
                            else:
                                print("Ingrese un numero valido.")
                        except ValueError:
                            print("Error, Ingrese un numero.")
                elif opcrapid == 2:
                    menucompra = True
                    while menucompra: #Ciclo para forzar el menu
                        print("--------------Rapid--------------")
                        print("1)Descuento Diurno")
                        print("2)Descuento Vespertino")
                        print("3)Descuento Administrativo")
                        print("4)Anular Compra")
                        print("----------------------------")
                        try:
                            opcdesc = int(input("Ingrese una opcion:"))
                            if opcdesc == 1:
                                Descuento = 0.12 #Descuento Diurno
                            elif opcdesc == 2:
                                Descuento = 0.10 #Descuento Vespertino
                            elif opcdesc == 3:
                                Descuento = 0 #Descuento Administrativo
                            elif opcdesc == 4: #Al Anular, Reinicia los valores almacenados
                                CantidadCarnes = 0
                                CantidadPeperoni = 0
                                CantidadTradicional = 0
                                TotalCarnes = 0
                                TotalPeperoni = 0
                                TotalTradicional = 0
                                SubTotal = 0
                                Total = 0
                                break
                            else:
                                continue
                            print("PizzasDuoc")
                            print("-----------------------------")
                            if CantidadTradicional > 0: #Condición para solo mostrar la pizza si su cantidad es mayor a 0 para no saturar la boleta de informacion innecesaria
                                print(f"* {CantidadTradicional} Pizza Tradicional ${TotalTradicional}")
                            if CantidadPeperoni > 0:
                                print(f"* {CantidadPeperoni} Pizza Peperoni ${TotalPeperoni}")
                            if CantidadCarnes > 0:
                                print(f"* {CantidadCarnes} Pizza Todo Carnes ${TotalCarnes}")
                            print("-----------------------------")
                            SubTotal = TotalCarnes + TotalTradicional + TotalPeperoni #Almacena el subtotal
                            Total = SubTotal - (Descuento*SubTotal) #Almacena el Total
                            print(f"Subtotal: ${SubTotal}")
                            print(f"Descuento: ${Descuento * SubTotal}")
                            print("-----------------------------")
                            print(f"Total a Pagar : ${Total}")
                            print("Gracias por su compra")
                            menucompra = False #Sale del ciclo para volver al otro menu 
                        except ValueError:
                            print("Ingrese una opción valida")
                elif opcrapid == 3: #Salir del programa
                    menurapid = False
                    login = False
                    print("Saliendo del programa...")
                elif opcrapid == 4: #Cerrar sesion, Reinicia todos los valores para que en el siguiente inicio este limpio
                    CantidadCarnes = 0
                    CantidadPeperoni = 0
                    CantidadTradicional = 0
                    TotalCarnes = 0
                    TotalPeperoni = 0
                    TotalTradicional = 0
                    SubTotal = 0
                    Total = 0
                    print("Cerrando Sesion...")
                    menurapid = False #Sale de todo 
                else:
                    print("Ingrese una opción valida.")
            except ValueError:
                print("Ingrese un numero porfavor.")
    else:
        print("Datos Incorrectos intente de nuevo.")
print("Usted Salio del sistema.")
