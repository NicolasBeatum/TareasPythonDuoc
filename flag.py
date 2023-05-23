flag=False
print("Flags")
num=int(input("Ingrese un numero: \n"))
if num%2 == 0:
    flag=True

if flag==True:
    print(f"El numero {num} ingresado es par. ")
else :
    print(f"El numero {num} ingresado no es par. ")
