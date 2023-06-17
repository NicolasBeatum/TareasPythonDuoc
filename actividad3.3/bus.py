import numpy as np
from funcionesbus import * 
valor = np.arange(1, 101, dtype=object)
asientos = np.reshape(valor, (10,10))
rut = [] 
nombre = [] 
asiento_cliente = []
Ganancia_Total = 0

menun = True

while menun:
    menu()
    opc = int(input("Ingrese una opcion: "))
    if opc == 1: #1) Ver Asientos
        print(asientos)
    elif opc == 2: #2) Comprar Asientos
        ocupao = True
        rut_cliente = int(input("Ingrese su rut sin puntos, ni guion, ni dv: "))
        nombre_cliente = input("Ingrese su nombre: ")
        num = int(input("Ingrese un asiento: "))
        if num > 100:
            print("Asiento no existe")        
        elif num != "" and nombre_cliente != "" and rut_cliente != "":
            for f in range(10):
                for c in range(10):
                    if num == asientos[f,c]:
                        ocupao = False
                        num_cliente = num
                        print(f"Su asiento es: {num}")
                        asientos[f,c] = "X"
                        #Agrega a la lista
                        rut.append(rut_cliente)
                        nombre.append(nombre_cliente)
                        asiento_cliente.append(num_cliente)
                        print(asientos)
                        if num_cliente >= 1 and num_cliente <= 20:
                            Ganancia_Total = Ganancia_Total + 20000
                        elif num_cliente >= 21 and num_cliente <= 50:
                            Ganancia_Total = Ganancia_Total + 10000
                        elif num_cliente >= 51 and num_cliente <= 100:
                            Ganancia_Total = Ganancia_Total + 5000
        else:
            print("no puedes dejar en blanco")
        if ocupao == True:
            print("Esta ocupao")
    elif opc == 3: #3) Lista de Usuario
        print(rut)
        print(nombre)
        print(asiento_cliente)
    elif opc == 4: #4) Buscar por rut
        rut_ing = int(input("Ingrese el rut para buscar: "))
        buscar(rut_ing,rut,nombre,asiento_cliente)
    elif opc == 5: #5) Mostrar Ganancia
        print(f"El Bus ha ganado: {Ganancia_Total}")
    elif opc == 6:
        menun = False
        
print("Salio del programa")