acumulador = 0 # acumulador de notas
i = 0 # contador
print("Promedio")
print("Ingrese 3 notas de los alumnos para sacar el promedio (del 1 al 7)")
while i < 3: # si el contador es menor a 3, se ejecuta el ciclo
    nota = int(input(f"Ingrese la nota {i+1}: ")) # se pide la nota
    if nota >= 1 and nota <= 7: # si la nota es mayor o igual a 1 y menor o igual a 7 esta se guarda
        acumulador = acumulador + nota #acumula la nota
        i = i + 1 # aumenta el contador
    elif nota < 1 or nota > 7: # si la nota es menor a 1 o mayor a 7 muestra un mensaje
        print("la nota no puede ser menos de 1 o mayor a 7") # no guarda nada se repite el ciclo y no aumenta el contador
promedio = acumulador / i #Calcula promedio
print("El promedio es:", promedio) #Muestra promedio