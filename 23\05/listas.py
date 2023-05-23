estudiante = ["Nicolas", "20.626.765-8", "Hernandez","18/10"]
#               0           1               2           3   Posiciones de la lista
print(f"Nombre: {estudiante[0]}") #Nombre
print(f"Rut: {estudiante[1]}") #Rut
print(f"Apellido: {estudiante[2]}") #Apellido
print(f"Cumpleaños: {estudiante[3]}") #Cumpleaños

print("---Recorrer Lista---")
for i in estudiante: #Recorrer la lista en un for
    print(i, end=",")

print("")
print("---Conseguir numero de la lista---") #Obtener Posición
for i in range(len(estudiante)):
    print(i, end=",")
print("")

#Uso de Append
print("---Append---")
Nombre = input("Ingrese un Nombre: ")
estudiante.append(Nombre) #append pone un elemento al final de la lista
Rut = input("Ingrese un Rut: ")
estudiante.append(Rut)
Apellido = input("Ingrese un Apellido: ")
estudiante.append(Apellido)
Cumple = input("Ingrese un Cumpleaños: ")
estudiante.append(Cumple)

print(f"Nombre: {estudiante[4]}") #Nombre
print(f"Rut: {estudiante[5]}") #Rut
print(f"Apellido: {estudiante[6]}") #Apellido
print(f"Cumpleaños: {estudiante[7]}") #Cumpleaños

#Uso de Extend
print("---Extend---")
AgendaNueva = [9423442, 52423412, 98323232]
AgendaVieja = [2312342, 32132141, 32132135]
print(f"Mi Agenda Tiene estos numeros{AgendaNueva}")
AgendaNueva.extend(AgendaVieja) #Permite añadir listas a una lista
print(f"Traspasare los numeros de mi agenda anterior que son: {AgendaVieja} ")
print(f"Ahora mi agenda tiene: {AgendaNueva}")

#Uso de Insert&Remove&Pop
print("----Insert&Remove&Pop")
Agenda = [9423442, 52423412, 98323232]
NumeroNuevo = 123456
print("Quiero agregar el numero nuevo en la segunda posiciojn de mi lista de contactos")
print(Agenda)
print(f"Agregare el numero nuevo {NumeroNuevo} en la segunda posición")
Agenda.insert(1, NumeroNuevo)
print(f"Ya esta en mi agenda: {Agenda}")
print(f"Quiero eliminar el {Agenda[2]}")
Agenda.remove(52423412)
print(f"Ya estaria mi agenda: {Agenda}")
print(f"Ahora quiero eliminar el ultimo numero de mi agenda {Agenda}")
Agenda.pop()
print(f"Mi Agenda: {Agenda}")

#Uso de Sort
Numeros=[3,4,2,5,20,13]
print("---Sort---")
print(f"mis nuemros: {Numeros}")
print("Quiero ordenar mis numeros de menor a mayor")
Numeros.sort()
print(Numeros)
print("los quiero en mayor a menor")
Numeros.sort(reverse=True)
print(Numeros)
