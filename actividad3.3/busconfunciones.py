import numpy as np
from funcionesbus2 import * 
# Crear la matriz de asientos
valor = np.arange(1, 101, dtype=object)
asientos = np.reshape(valor, (10,10))

# Variables para almacenar información
rut = [] 
nombre = [] 
asiento_cliente = []
# Variabl para el Ciclo
menun = True

while menun:
    menu()
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1: #1) Ver Asientos
            mostrar_Asientos(asientos)
        elif opc == 2: #2) Comprar Asientos
            try:
                rut_cliente = int(input("Ingrese su rut sin puntos, ni guion, ni dv: "))
            except ValueError:
                print("Rut no valido")
                continue #Sale del elif
            nombre_cliente = input("Ingrese su nombre: ")
            try:
                num = int(input("Ingrese un asiento: "))
            except ValueError:
                print("Ingrese un numero porfavor")
                continue #Sale del elif
            if num > 100 or num < 1: #Comprueba si el numero es mayor o menos a los Asientos disponible
                print("No existe ese asiento") #Si no se encuentra imprime un mensaje
            else: #Si se encuentra ejecuta la función
                comprar_Asientos(rut_cliente,nombre_cliente,num,asientos,rut,nombre,asiento_cliente) 
        elif opc == 3: #3) Lista de Usuario
            lista_usuario(rut, nombre, asiento_cliente)
        elif opc == 4: #4) Buscar por rut
            rut_ing = int(input("Ingrese el rut para buscar: "))
            buscar(rut_ing,rut,nombre,asiento_cliente)
        elif opc == 5: #5) Mostrar Ganancia
            mostrar_ganancias(asiento_cliente)
        elif opc == 6:
            menun = False
        else:
            print("Ingrese un numero valido.")
    except ValueError:
        print("Ingrese un numero porfavor.")
        
print("Salio del programa")