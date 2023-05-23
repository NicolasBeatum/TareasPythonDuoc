zapatos = 20000
total = 0
print("Comprar Zapatos")
print("Cuantos Zapatos quiere comprar, los Zapatos cuestan $20000")
cant = int(input("Ingrese la cantidad de  zapatos a comprar\n"))
total = zapatos*cant
if total >= 40000:
    print(f"Felicidade su compra supero los 40000 pesos el envio es gratis, su total a pagar es {total}")
else:
    print(f"Su compra con el valor de envio(3000) es: {total+3000}")
