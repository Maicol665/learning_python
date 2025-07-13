name = "michael"
edad = 24
birthday = False
money = 2000.53

name: str = "michael"
edad: int = 24
birthday: bool = False
money: float = 2000.53

print("Hola Mundo")
a = 3
b = 5
print (a+b)

intento hacer un codigo de una rifa 

# Número ganador fijo
numero_ganador = 61

# Pedimos al usuario que ingrese su número de la suerte
numero_usuario = int(input("Ingresa un número entre 1 y 100: "))

# Verificamos si el número ingresado es el ganador
if numero_usuario == numero_ganador:  # Comparación de los números
    print("¡Felicidades! Has ganado la rifa.")
else:
    print(f"Lo siento, el número ganador era {numero_ganador}.")