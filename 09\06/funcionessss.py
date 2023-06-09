def menu():
    print("------Menu------")
    print("1) Calcular IVA")
    print("2) Aplicar 30 de Dscto")
    print("3) Calcular IMC")
    print("4) Salir")

def IVA19(compra):
    iva = compra * 0.19
    print(f"El IVA de su compra es: {iva}")
def descuento30(compra):
    descuento = compra * 0.70
    print(f"La compra con el descuento aplicado: {descuento}")
def IMCc(peso, altura):
    imc = peso/(altura*altura)
    print(f"SU IMC es: {round(imc,2)}")