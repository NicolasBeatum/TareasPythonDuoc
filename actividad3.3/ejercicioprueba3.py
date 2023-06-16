from funcioneprueba3 import *
id_producto = ["867961-B21", "840369-A2", "777876-H55-H6"]
nombre_producto = ["Servidor Huaweii Next Generation 2","Servidor Huaweii Generation One", "Servidor HP Proliant Inte"]
precio_producto = [5000, 3000, 400]
menun = True


while menun:
    menu()
    try:
        opc = int(input("Ingrese una opción: "))
        if opc == 1:
            numero_parte = input("Ingrese una ID para el nuevo producto: ")
            nombre = input("Ingrese un nombre para el nuevo producto: ")
            precio = int(input("Ingrese un precio para el nuevo producto: "))
            grabar(numero_parte,nombre,precio,id_producto,nombre_producto,precio_producto)
        elif opc == 2:
            id = input("Ingrese Numero de Parte: ")
            buscar(id,id_producto,precio_producto,nombre_producto)
        elif opc == 3:
            id = input("Ingrese Numero de Parte: ")
            imprimir(id,id_producto,precio_producto,nombre_producto)
        elif opc == 4:
            imprimir_todo(id_producto,precio_producto,nombre_producto)
        elif opc == 5:
            menun = False
        else:
            print("Ingrese un numero valido porfavor.")
    except ValueError:
        print("Ingrese un numero porfavor.")
        
print("-------------------------------------------------")
print("Salio del Programa")
print("Version 1.0")
print("By: Nicolas Hernandez")
print("-------------------------------------------------")

