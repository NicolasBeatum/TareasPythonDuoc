amasado = 4000
molde = 1000
baguette = 2000
integral = 3000

print("Hola cuanto panes quieres")
camasado = int(input("Cuantos panes amasado quieres? 4000 c/u "))
cmolde = int(input("Cuantos panes molde quieres? 1000 c/u "))
cbaguette = int(input("Cuantos panes baguette quieres? 2000 c/u "))
cintegral = int(input("Cuantos panes integral quieres? 3000 c/u "))

resul_neto = (amasado*camasado) + (molde*cmolde) + (cbaguette*baguette) + (integral*cintegral)
if resul_neto > 5000:
    print(f"El envio es gratis, su compra es de {resul_neto}")
elif resul_neto <=5000:
    print(f"su compra es de {resul_neto+(resul_neto*0.1)}")
