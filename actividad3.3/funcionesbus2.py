def menu():
    print("---Buses del Sur---")
    print("1) Ver Asientos")
    print("2) Comprar Asientos")
    print("3) Lista de Usuario")
    print("4) Buscar por Rut")
    print("5) Ganancias Totales")
    print("6) Salir")

def mostrar_Asientos(asientos):
    print(asientos)

def comprar_Asientos(rut_cliente,nombre_cliente,num,asientos,rut,nombre,asiento_cliente):
    ocupao = True     
    if num != "" and nombre_cliente != "" and rut_cliente != "":
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
    else:
            print("no puedes dejar en blanco")
    if ocupao == True:
        print("Esta ocupao")
        
        
def lista_usuario(rut, nombre, asiento_cliente):
    print(rut)
    print(nombre)
    print(asiento_cliente)

def buscar(rut_ing,lista_rut,lista_nombre,lista_cliente):
    try:
        pos = lista_rut.index(rut_ing)
        print("---Datos del Cliente---")
        print(f"Nombre del Cliente: {lista_nombre[pos]}")
        print(f"Rut del Cliente: {lista_rut[pos]}")
        print(f"Asiento del Cliente: {lista_cliente[pos]}")
    except ValueError:
        print("El Rut no se encuentra en la base de datos.")
        
        
def mostrar_ganancias(asiento_cliente):
    Ganancia_Total = 0
    for i in range(len(asiento_cliente)):
        if asiento_cliente[i] >= 1 and asiento_cliente[i] <= 20:
            Ganancia_Total = Ganancia_Total + 20000
        elif asiento_cliente[i] >= 21 and asiento_cliente[i] <= 50:
            Ganancia_Total = Ganancia_Total + 10000
        elif asiento_cliente[i] >= 51 and asiento_cliente[i] <= 100:
            Ganancia_Total = Ganancia_Total + 5000
    print(Ganancia_Total)