#recrear el juego de la flor petalos
import random
petalos = random.randint(1, 20) #numero de petalos
print(f"La flores tiene los siguientes petalos: {petalos}")
i = 1

num = random.randint(1, 3)
for i in range(petalos):
    if num == 1:
        print(f"{i}.- Me quiere mucho")
        resul = "Me quiere mucho"
        num = num + 1
    elif num == 2:
        print(f"{i}.-Me quiere un poco")
        resul = "Me quiere un poco"
        num = num + 1
    elif num == 3:
        print(f"{i}.-No me quiere")
        resul = "No me quiere"
        num = 1

print("La flor se ha deshojado")
print("El resultado es: ", resul)