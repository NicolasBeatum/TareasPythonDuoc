def menu():
    print("---Menu MPN----")
    print("1)Grabar")
    print("2)Buscar")
    print("3)Imprimir")
    print("4)Imprimir Todo")
    print("5)Salir")

def grabar(numero_parte,nombre,precio, lista_id, lista_nombre, lista_precio):
    long = len(nombre)
    if long > 5:
        lista_id.append(numero_parte)
        lista_nombre.append(nombre)
        lista_precio.append(precio)
    else:
        print("El nombre del producto es muy corto.")

def buscar(id, lista_id, lista_precio, lista_nombre):
    try:
        pos = lista_id.index(id)
        if int(lista_precio[pos]) >= 500:
            print(f"ID del Producto: {lista_id[pos]}")   
            print(f"Nombre del Producto: {lista_nombre[pos]}")
            print(f"Precio del Producto: {lista_precio[pos]}")
        else:
            print("No hay stock")
    except ValueError:
        print("No ha sido encontrado")
        
def imprimir(id, lista_id, lista_precio, lista_nombre):
    try:
        pos = lista_id.index(id)
        print(f"ID del Producto: {lista_id[pos]}")   
        print(f"Nombre del Producto: {lista_nombre[pos]}")
        print(f"Precio del Producto: {lista_precio[pos]}")
        print("Descripcion: Servidor")
    except ValueError:
        print("No existe ningun producto con ese Numero de Parte")

    
def imprimir_todo(lista_id, lista_precio, lista_nombre):
    for i in range(len(lista_id)):
        print(f"--------")
        print(f"Posicion: {i}")
        print(f"ID del Producto: {lista_id[i]}")   
        print(f"Nombre del Producto: {lista_nombre[i]}")
        print(f"Precio del Producto: {lista_precio[i]}")
        print("---------")
