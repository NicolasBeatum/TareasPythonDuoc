# Crear un gato
turno = 1
gato = [["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]
menu = 1

# Función para imprimir el tablero
def imprimirTablero():
    for fila in gato:
        print("/".join(fila))

# Función para verificar si hay un ganador
def verificarGanador():
    for i in range(3):
        if gato[i][0] == gato[i][1] == gato[i][2]:  # Comprobar filas
            return True
        if gato[0][i] == gato[1][i] == gato[2][i]:  # Comprobar columnas
            return True
    if gato[0][0] == gato[1][1] == gato[2][2]:  # Comprobar diagonal principal
        return True
    if gato[0][2] == gato[1][1] == gato[2][0]:  # Comprobar diagonal inversa
        return True
    return False

print("Bienvenido al juego del gato")
print("El jugador 1 es X y el jugador 2 es O")

while menu == 1 and turno == 1 or menu == 1 and turno == 2:
    if turno == 1:
        # Turno J1
        print("Elige una posición para tu jugada")
        imprimirTablero()
        posicionj1 = int(input("Elige una posición para tu jugada jugador 1: "))
        fila = (posicionj1 - 1) // 3
        col = (posicionj1 - 1) % 3
        if gato[fila][col] == str(posicionj1):
            gato[fila][col] = "X"
        else:
            print("Esa posición ya está ocupada")
            continue
        turno = 2
        if verificarGanador():
            imprimirTablero()
            print("¡Jugador 1 (X) ha ganado!")
            break

    if turno == 2:
        # Turno J2
        imprimirTablero()
        posicionj2 = int(input("Elige una posición para tu jugada jugador 2: "))
        fila = (posicionj2 - 1) // 3
        col = (posicionj2 - 1) % 3
        if gato[fila][col] == str(posicionj2):
            gato[fila][col] = "O"
        else:
            print("Esa posición ya está ocupada")
            continue
        turno = 1
        if verificarGanador():
            imprimirTablero()
            print("¡Jugador 2 (O) ha ganado!")
            break

imprimirTablero()
print("Gracias por jugar")
