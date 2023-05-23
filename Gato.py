#Crear un gato
turno = 1
a1 = "1"
a2 = "2"
a3 = "3"
a4 = "4"
a5 = "5"
a6 = "6"
a7 = "7"
a8 = "8"
a9 = "9"
menu = 1

#funcion para verificar si hay un ganador
def verificarGanador(a1, a2, a3, a4, a5, a6, a7, a8, a9):
    global menu
    global turno
    if a1 == a2 and a1 == a3: #horizontal
        print("se acabo el juego")
        menu = menu + 1
        turno = 3
    elif a4 == a5 and a4 == a6: #horizontal
        print("se acabo el juego")
        menu = menu + 1
        turno = 3
    elif a7 == a8 and a7 == a9: #horizontal
        print("se acabo el juego")
        menu = menu + 1
        turno = 3
    elif a1 == a4 and a1 == a7: #vertical
        print("se acabo el juego")
        menu = menu + 1
        turno = 3
    elif a2 == a5 and a2 == a8: #vertical
        print("se acabo el juego")
        menu = menu + 1
        turno = 3
    elif a3 == a6 and a3 == a9: #vertical
        print("se acabo el juego")
        menu = menu + 1
        turno = 3
    elif a1 == a5 and a1 == a9: #diagonal
        print("se acabo el juego")
        menu = menu + 1
        turno = 3
    elif a3 == a5 and a3 == a7: #diagonal
        print("se acabo el juego")
        menu = menu + 1
        turno = 3
    elif a1 != "1" and a2 != "2" and a3 != "3" and a4 != "4" and a5 != "5" and a6 != "6" and a7 != "7" and a8 != "8" and a9 != "9":
        print("se acabo el juego en empate")
        menu = menu + 1
        turno = 3
    

print("Bienvenido al juego del gato")
print("El jugador 1 es X y el jugador 2 es O")
while menu == 1 and turno == 1 or menu == 1 and turno == 2: # comprueba si el juego sigue o no si turno = 3 se acaba el juego
    if turno == 1: #comprueba el turno
        #Turno J1
        print("Elige una posicion para tu jugada")
        print(a1 + "/" + a2 + "/" + a3)
        print(a4 + "/" + a5 + "/" + a6)
        print(a7 + "/" + a8 + "/" + a9)
        posicionj1 = int(input("Elige una posicion para tu jugada jugador1 \n"))
        if posicionj1 == 1 and a1 == "1":
            a1 = "X"
        elif posicionj1 == 2 and a2 == "2":
            a2 = "X"
        elif posicionj1 == 3 and a3 == "3":
            a3 = "X"
        elif posicionj1 == 4 and a4 == "4":
            a4 = "X"
        elif posicionj1 == 5 and a5 == "5":
            a5 = "X"
        elif posicionj1 == 6 and a6 == "6":
            a6 = "X"
        elif posicionj1 == 7 and a7 == "7":
            a7 = "X"
        elif posicionj1 == 8 and a8 == "8":
            a8 = "X"
        elif posicionj1 == 9 and a9 == "9":
            a9 = "X"
        else:
            print("Esa posicion ya esta ocupada")
            continue
        turno = 2
        resultado = verificarGanador(a1, a2, a3, a4, a5, a6, a7, a8, a9)

    
    if turno == 2: #comprueba el turno
        #Turno J2 
        print(a1 + "/" + a2 + "/" + a3)
        print(a4 + "/" + a5 + "/" + a6)
        print(a7 + "/" + a8 + "/" + a9)
        posicionj2 = int(input("Elige una posicion para tu jugada jugador2 \n"))
        if posicionj2 == 1 and a1 == "1":
            a1 = "O"
        elif posicionj2 == 2 and a2 == "2":
            a2 = "O"
        elif posicionj2 == 3 and a3 == "3":
            a3 = "O"
        elif posicionj2 == 4 and a4 == "4":
            a4 = "O"
        elif posicionj2 == 5 and a5 == "5":
            a5 = "O"
        elif posicionj2 == 6 and a6 == "6":
            a6 = "O"
        elif posicionj2 == 7 and a7 == "7":
            a7 = "O"
        elif posicionj2 == 8 and a8 == "8":
            a8 = "O"
        elif posicionj1 == 9 and a9 == "9":
            a9 = "O"
        else:
            print("Esa posicion ya esta ocupada")
            continue
        turno = 1
        resultado = verificarGanador(a1, a2, a3, a4, a5, a6, a7, a8, a9)
        
print(a1 + "/" + a2 + "/" + a3)
print(a4 + "/" + a5 + "/" + a6)
print(a7 + "/" + a8 + "/" + a9)
print("Gracias por jugar")
   