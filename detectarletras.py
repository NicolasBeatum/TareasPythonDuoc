contcons = 0
contvocal = 0
for n in range(10):
    letra = str.upper(input("Ingrese una letra \n"))
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        contvocal = contvocal + 1
    else:
        contcons = contcons + 1
print(f"Vocales Ingresadas: {contvocal}")
print(f"Vocales Ingresadas: {contcons}")