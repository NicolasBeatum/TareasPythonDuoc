#Ahorcado
menu = 1
dificultad = 0
vidas = 7
Primera_palabra = ["A", "Z", "U", "C", "A", "R"]
Facil_vacio = ["_", "_", "_", "_", "_", "_"]
Medio_Palabra = ["A","C","O","R","D","E","O","N"]
Medio_Vacio = ["_", "_", "_", "_", "_", "_", "_", "_"]
DificIl_Palabra = ["M","U","R","C","I","E","L","A","G","O"]
Dificil_Vacio = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

while menu == 1:
    print("Bienvenido al juego del ahorcado")
    print("1. Dificultad")
    print("2. Jugar")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print("1. Facil")
        print("2. Medio")
        print("3. Dificil")
        dificultad = int(input("Ingrese una opcion: "))
    elif opcion == 2:
        if dificultad == 1: #Facil
            while dificultad == 1:
                print("Facil") #Palabra de 6 Letras Azucar
                print(f"Tiene {vidas} vidas")
                print("Adivine la palabra")
                print(Facil_vacio)
                letra = str(input("Ingrese una letra: "))
                encontrada = False
                for i in range(0, 6):
                    if letra == Primera_palabra[i]:
                        print("Correcto")
                        Facil_vacio [i] = letra
                        encontrada = True
                if encontrada == False:
                        print("Incorrecto")
                        vidas = vidas - 1
                        print(f"Le quedan {vidas} vidas")
                if vidas == 0:
                    print("Perdiste, Eliga de nuevo la Dificultad")
                    dificultad = 0
                    vidas = 7
                    break
                if Facil_vacio == Primera_palabra:
                    print(Facil_vacio)
                    print("Ganaste, la palabra era Azucar")
                    dificultad = 0
                    vidas = 7
                    break
        elif dificultad == 2: #Medio
            while dificultad == 2:
                print("Medio")
                print(f"Tiene {vidas} vidas")
                print("Adivine la palabra")
                print(Medio_Vacio)
                letra = str(input("Ingrese una letra: "))
                encontrada = False
                for i in range(0, 8):
                    if letra == Medio_Palabra[i]:
                        print("Correcto")
                        Medio_Vacio [i] = letra
                        encontrada = True
                if encontrada == False:
                        print("Incorrecto")
                        vidas = vidas - 1
                        print(f"Le quedan {vidas} vidas")
                if vidas == 0:
                    print("Perdiste, Eliga de nuevo la Dificultad")
                    dificultad = 0
                    vidas = 7
                    break
                if Medio_Vacio == Medio_Palabra:
                    print(Medio_Vacio)
                    print("Ganaste, la palabra era Acordeon")
                    dificultad = 0
                    vidas = 7
                    break
        elif dificultad == 3: #Dificil
            while dificultad == 3:
                print("Dificil")
                print(f"Tiene {vidas} vidas")
                print("Adivine la palabra")
                print(Dificil_Vacio)
                letra = str.upper(input("Ingrese una letra: "))
                encontrada = False
                for i in range(0, 10):
                    if letra == DificIl_Palabra[i]:
                        print("Correcto")
                        Dificil_Vacio [i] = letra
                        encontrada = True
                if Dificil_Vacio == DificIl_Palabra or letra == "MURCIELAGO":
                    print(DificIl_Palabra)
                    print("Ganaste, la palabra era Murcielago")
                    dificultad = 0
                    vidas = 7
                    break
                if encontrada == False:
                        print("Incorrecto")
                        vidas = vidas - 1
                        print(f"Le quedan {vidas} vidas")
                if vidas == 0:
                    print("Perdiste, Eliga de nuevo la Dificultad")
                    dificultad = 0
                    vidas = 7
                    break
                