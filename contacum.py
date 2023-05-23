acumulador = 0
contador = 0
print("suma de Numeros pares")
num1 = int(input("Ingrese un numero\n"))
num2 = int(input("Ingrese un numero\n"))
num3 = int(input("Ingrese un numero\n"))

if num1%2==0:
    acumulador = acumulador + num1
    contador = contador + 1
if num2%2==0:
    acumulador = acumulador + num2
    contador = contador + 1
if num3%2==0:
    acumulador = acumulador + num3
    contador = contador + 1

print(f"la suma de los numeros pares fue: {acumulador}, y se ingresaron {contador} numeros pares")