x = range(5)
cont0 = 0 
contpositivo = 0
contnegativo = 0
for n in x:
    num = int(input(f"Ingrese un numero en la posición {n}: \n"))
    if num>0:
        contpositivo = contpositivo + 1
    elif num<0:
        contnegativo = contnegativo + 1
    elif num == 0:
        cont0 = cont0 + 1
        
print(f"Numeros Positivos: {contpositivo}")
print(f"Numeros Iguales a 0: {cont0}")
print(f"NUmero Negativos: {contnegativo}")
print("Muchas gracias")
