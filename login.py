#Crear sistema y comprobar si funciona

user_1_Registrado = "pedro" #Usuario registrado
user_1_Contraseña = "1234" #Contraseña registrada

user_2_Registrado = "juan" #Usuario registrado
user_2_contraseña = "a4s1" #Contraseña registrada

print("Bienvenido") 
user = input("Ingrese su usuario: ") #Se pide el usuario
contraseña = input("Ingrese su contraseña: ") #Se pide la contraseña

if user == user_1_Registrado and contraseña == user_1_Contraseña: #Comprueba si usuario y contraseña son correctos
    print("Bienvenido", user_1_Registrado) #si es correcto, escribe "Bienvenido" y el usuario
elif user == user_2_Registrado and contraseña == user_2_contraseña: #Comprueba si usuario y contraseña son correctos
    print("Bienvenido", user_2_Registrado) #si es correcto, escribe "Bienvenido" y el usuario
else:
    print("Usuario o Contraseña incorrectos") #Si no es correcto, escribe "Usuario o contraseña incorrectos"