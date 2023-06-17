import numpy as np
from funcionesbus2 import * 
valor = np.arange(1, 101, dtype=object)
asientos = np.reshape(valor, (10,10))
rut = [] 
nombre = [] 
asiento_cliente = []
menun = True

while menun:
    menu()
    opc = int(input("Ingrese una opcion: "))
    if opc == 1: #1) Ver Asientos
        mostrar_Asientos(asientos)
    elif opc == 2: #2) Comprar Asientos
        rut_cliente = int(input("Ingrese su rut sin puntos, ni guion, ni dv: "))
        nombre_cliente = input("Ingrese su nombre: ")
        num = int(input("Ingrese un asiento: "))
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
        
print("Salio del programa")