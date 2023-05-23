numero = int(input("Ingrese un número entre 103 y 997: "))

if numero < 103 or numero > 997:
    print("El número debe estar entre 103 y 997")
else:
    cientos = numero // 100
    decenas = (numero // 10) % 10
    unidades = numero % 10

    numero_invertido = unidades * 100 + decenas * 10 + cientos
    print("El número invertido es:", numero_invertido)