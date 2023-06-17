def menu():
    print("---Buses del Sur---")
    print("1) Ver Asientos")
    print("2) Comprar Asientos")
    print("3) Lista de Usuario")
    print("4) Buscar por Rut")
    print("5) Ganancias Totales")
    print("6) Salir")

def buscar(rut_ing,lista_rut,lista_nombre,lista_cliente):
    pos = lista_rut.index(rut_ing)
    print("---Datos del Cliente---")
    print(f"Nombre del Cliente: {lista_nombre[pos]}")
    print(f"Rut del Cliente: {lista_rut[pos]}")
    print(f"Asiento del Cliente: {lista_cliente[pos]}")
        