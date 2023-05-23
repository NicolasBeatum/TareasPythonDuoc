contador = 0
print("Contadores de Numeros pares")
num1 = int(input("Ingrese un numero\n"))
num2 = int(input("Ingrese un numero\n"))
num3 = int(input("Ingrese un numero\n"))

if num1%2==0:
    contador = contador + 1
if num2%2==0:
    contador = contador + 1
if num3%2==0:
    contador = contador + 1

print(f"fueron: {contador} numeros pares")