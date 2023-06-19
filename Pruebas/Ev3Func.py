import random as rd

def menu():
    print("-----Vida y Salud-----")
    print("1)Grabar")
    print("2)Buscar")
    print("3)Imprimir Certificado")
    print("4)Salir")

def grabar(Rut, Nombre, Apellido_Paterno, Edad, Fecha_Afiliacion, Lista_Rut, Lista_Nombre, Lista_ApPaterno, Lista_Edad, Lista_Fecha):
    largorut = len(str(Rut))
    if Edad > 18 and largorut == 8:
        Lista_Rut.append(Rut)
        Lista_Nombre.append(Nombre)
        Lista_ApPaterno.append(Apellido_Paterno)
        Lista_Edad.append(Edad)
        Lista_Fecha.append(Fecha_Afiliacion)
    elif largorut != 8:
        print("Ingresaste mal tu rut")
    elif Edad <= 18:
        print("Flaco sos menor")

def buscar(Rut,Lista_Rut, Lista_Nombre, Lista_ApPaterno, Lista_Edad, Lista_Fecha):
    try:
        pos = Lista_Rut.index(Rut)
        print(f"Rut: {Lista_Rut[pos]}")
        print(f"Nombre: {Lista_Nombre[pos]}")
        print(f"Apellido Paterno: {Lista_ApPaterno[pos]}")
        print(f"Edad: {Lista_Edad[pos]}")
        print(f"Fecha: {Lista_Fecha[pos]}")
    except ValueError:
        print("El rut ingresado no se encuentra en la base de datos")

def minimenu():
    print("-----Certificado-----")
    print("1)Certificado de Isapre")
    print("2)Certificado de Datos")
    print("3)Certificado de Estado Civil")
    
def Imprimir(opc2,Rut,Lista_Rut, Lista_Nombre, Lista_ApPaterno, Lista_Edad, Lista_Fecha, ):
    valor = rd.randint(1000, 1500)
    pos = Lista_Rut.index(Rut)
    if opc2 == 1:
        print("--------------")
        print("Certificado Tipo: Isapre")
        print(f"Precio: {valor}")
        print(f"Nombre Afiliado: {Lista_Nombre[pos]} {Lista_ApPaterno[pos]}")
        print("-------Datos-------")
        print(f"Rut: {Lista_Rut[pos]}")
        print(f"Nombre: {Lista_Nombre[pos]}")
        print(f"Apellido Paterno: {Lista_ApPaterno[pos]}")
        print(f"Edad: {Lista_Edad[pos]}")
        print(f"Fecha: {Lista_Fecha[pos]}")
    elif opc2 == 2:
        print("--------------")
        print("Certificado Tipo: Datos")
        print(f"Precio: {valor}")
        print(f"Nombre Afiliado: {Lista_Nombre[pos]} {Lista_ApPaterno[pos]}")
        print("-------Datos-------")
        print(f"Rut: {Lista_Rut[pos]}")
        print(f"Nombre: {Lista_Nombre[pos]}")
        print(f"Apellido Paterno: {Lista_ApPaterno[pos]}")
        print(f"Edad: {Lista_Edad[pos]}")
        print(f"Fecha: {Lista_Fecha[pos]}")
    elif opc2 == 3:
        print("--------------")
        print("Certificado Tipo: Estado Civil")
        print(f"Precio: {valor}")
        print(f"Nombre Afiliado: {Lista_Nombre[pos]} {Lista_ApPaterno[pos]}")
        print("-------Datos-------")
        print(f"Rut: {Lista_Rut[pos]}")
        print(f"Nombre: {Lista_Nombre[pos]}")
        print(f"Apellido Paterno: {Lista_ApPaterno[pos]}")
        print(f"Edad: {Lista_Edad[pos]}")
        print(f"Fecha: {Lista_Fecha[pos]}")